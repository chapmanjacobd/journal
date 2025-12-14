Just in case someone comes along and sees this... After fiddling around with a few different ways I recommend downloading the Windows SUU iso, [for example here](https://www.dell.com/support/home/en-us/drivers/driversdetails?driverid=5r3n1). It has to be the Windows one, not Linux.

Then load up the iDRAC, login, go to Virtual Console settings, switch to HTML5 instead of Native/Java, and boot up the server into Lifecycle Controller mode. Launch the Virtual Console and click on Virtual Devices. Select the SUU iso file that you downloaded and map it as a CD/DVD. Click "Map Device". Close the Virtual Devices window.

Then in Lifecycle Controller select update, Local Drive, select the Virtual CD, and click next.
