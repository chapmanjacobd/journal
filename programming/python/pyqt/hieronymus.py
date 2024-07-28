#!/usr/bin/env python3
# this file is under the WTFPLv2 license, see COPYING.WTFPL

import sys

from PyQt5.QtCore import (
	pyqtSlot as Slot, QPointF, QRectF,
)
from PyQt5.QtGui import (
	QPainter, QPixmap,
)
from PyQt5.QtWidgets import (
	QAction, QActionGroup, QApplication, QMainWindow, QToolBar, QWidget,
)

MODE_PANSCAN = 0
MODE_CURTAIN = 1
MODE_FADE = 2

MODE_HORIZONTAL = 0
MODE_VERTICAL = 1
MODE_GRID = 2

# TODO add option for visual splitter?
# TODO option for tint images?
# TODO grid for more than 2 images
# TODO do a kind of diff?


class MainWindow(QMainWindow):
	def __init__(self, viewer=None, **kwargs):
		super(MainWindow, self).__init__(**kwargs)
		self.viewer = viewer
		self.setCentralWidget(viewer)

		tb = QToolBar()
		tb.addAction(viewer.panScanAction)
		tb.addAction(viewer.curtainAction)
		tb.addAction(viewer.lockAction)
		self.addToolBar(tb)


class CurtainViewer(object):
	def __init__(self, **kwargs):
		super(CurtainViewer, self).__init__(**kwargs)
		self.__mouse = QPointF()

	def disable(self):
		self.setMouseTracking(False)

	def enable(self):
		self.setMouseTracking(True)

	def _rect(self, rect, image_index):
		irect = QRectF(rect)
		irect.translate(-self.rect().center())
		irect.setTopLeft(irect.topLeft() * self.zoom[image_index])
		irect.setBottomRight(irect.bottomRight() * self.zoom[image_index])
		irect.translate(self.centers[image_index])
		return irect

	def paintEvent(self, ev):
		painter = QPainter(self)
		if len(self.images) == 2:
			if self.orientation == MODE_HORIZONTAL:
				wrects = [
					QRectF(0, 0, self.__mouse.x(), self.height()),
					QRectF(self.__mouse.x(), 0, self.width() - self.__mouse.x(), self.height()),
				]
			else:
				wrects = [
					QRectF(0, 0, self.width(), self.__mouse.y()),
					QRectF(0, self.__mouse.y(), self.width(), self.height() - self.__mouse.y()),
				]
		else:
			wrects = [QRectF(self.rect())]
		irects = [self._rect(r, n) for n, r in enumerate(wrects)]
		for img, wrect, irect in zip(self.images, wrects, irects):
			painter.drawPixmap(wrect, img, irect)

	def mousePressEvent(self, ev):
		pass

	def mouseMoveEvent(self, ev):
		self.__mouse = ev.pos()
		self.update()

	def mouseReleaseEvent(self, ev):
		pass

	def wheelEvent(self, ev):
		pass


class MultiViewer(object):
	def __init__(self, **kwargs):
		super(MultiViewer, self).__init__(**kwargs)

	def disable(self):
		pass

	def enable(self):
		pass

	def paintEvent(self, ev):
		painter = QPainter(self)

		iw = self.width() / len(self.images)
		sx = 0
		for img, zoom, center in zip(self.images, self.zoom, self.centers):
			wrect = QRectF(sx, 0, iw, self.height())
			irect = QRectF(0, 0, iw, self.height())
			irect.setSize(irect.size() * zoom)
			irect.moveCenter(QPointF(center))
			painter.drawPixmap(wrect, img, irect)
			sx += iw

	def mousePressEvent(self, ev):
		self.__point = ev.pos()
		self.__clicked = self.imageAt(ev.pos())

	def mouseMoveEvent(self, ev):
		mv = QPointF(ev.pos() - self.__point)

		indexes = [self.__clicked]
		if self.lock:
			indexes = range(len(self.images))

		for index in indexes:
			img_mv = mv * self.zoom[index]
			self.centers[index] -= img_mv

		self.__point = ev.pos()
		self.update()

	def mouseReleaseEvent(self, ev):
		pass

	def imageAt(self, pos):
		iw = self.width() / len(self.images)
		return int(pos.x() / iw)

	def wheelEvent(self, ev):
		idx = self.imageAt(ev.pos())
		if idx >= len(self.images):
			return

		d = ev.angleDelta().y()
		if d:
			d *= 0.2
			d /= 120
			d = 1 - d
			if self.lock:
				for idx in range(len(self.zoom)):
					self.zoom[idx] *= d
			self.update()


class Hieronymus(QWidget, MultiViewer, CurtainViewer):
	def __init__(self, **kwargs):
		super(Hieronymus, self).__init__(**kwargs)

		self.images = []
		self.zoom = []
		self.centers = []

		self.mode = MODE_PANSCAN
		self.orientation = MODE_HORIZONTAL
		self.lock = False

		self.panScanAction = QAction('Move/Zoom', self)
		self.panScanAction.setCheckable(True)
		self.panScanAction.setChecked(True)
		self.panScanAction.triggered.connect(self.setPanScan)

		self.curtainAction = QAction('Curtain', self)
		self.curtainAction.setCheckable(True)
		self.curtainAction.triggered.connect(self.setCurtain)

		self.actionGroup = QActionGroup(self)
		self.actionGroup.addAction(self.panScanAction)
		self.actionGroup.addAction(self.curtainAction)

		self.lockAction = QAction('Sync move/zoom', self)
		self.lockAction.setCheckable(True)
		self.lockAction.triggered.connect(self.triggerLock)

	def addImage(self, image):
		# TODO avoid loading full QPixmap?
		image = QPixmap(image)
		self.images.append(image)
		self.zoom.append(1.)
		self.centers.append(QPointF(image.rect().center()))

	@Slot()
	def setPanScan(self):
		self.modeClass().disable(self)
		self.mode = MODE_PANSCAN
		self.modeClass().enable(self)
		self.update()

	@Slot()
	def setCurtain(self):
		self.modeClass().disable(self)
		self.mode = MODE_CURTAIN
		self.modeClass().enable(self)
		self.update()

	@Slot(bool)
	def triggerLock(self, b):
		self.lock = b

	def modeClass(self):
		if self.mode == MODE_PANSCAN:
			return MultiViewer
		elif self.mode == MODE_CURTAIN:
			return CurtainViewer

	def paintEvent(self, ev):
		self.modeClass().paintEvent(self, ev)

	def mousePressEvent(self, ev):
		self.modeClass().mousePressEvent(self, ev)

	def mouseMoveEvent(self, ev):
		self.modeClass().mouseMoveEvent(self, ev)

	def mouseReleaseEvent(self, ev):
		self.modeClass().mouseReleaseEvent(self, ev)

	def wheelEvent(self, ev):
		self.modeClass().wheelEvent(self, ev)


if __name__ == '__main__':
	app = QApplication(sys.argv)

	viewer = Hieronymus()

	files = app.arguments()
	del files[0]  # first arg is executable
	if not files:
		print('usage: hieronymus FILE1 FILE2', file=sys.stderr)
		sys.exit(1)

	for img in files:
		viewer.addImage(img)

	win = MainWindow(viewer=viewer)
	win.show()

	sys.exit(app.exec_())
