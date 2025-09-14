// https://sizeof.cat/post/tricks-with-web-browser-tabs/

function favicons () {
	this.hidden = "hidden";
	this.visibilityChange = "visibilitychange";
	this.favicon = document.querySelector("[rel='shortcut icon']").href;
	this.title = document.title;

	/* Define a list of "services", each being a pair of favicon URL and the tab title to show. */
	this.services = {
		/* Reddit */
		reddit: () => {
			let title = "Reddit - Dive into anything";
			let favicon = "/img/favicons/reddit.png";
			return {
	  			title, favicon
			}
		},
		/* X, formerly known as Twitter */
		x: () => {
			let title = "X. It's what's happening / X";
			let favicon = "/img/favicons/x.ico";
			return {
	  			title, favicon
			}
		},
		/* Bluesky */
		bluesky: () => {
			let title = "Discover - Bluesky";
			let favicon = "/img/favicons/bluesky.png";
			return {
	  			title, favicon
			}
		},
		/* Wikipedia */
		wikipedia: () => {
			let title = "Wikipedia";
			let favicon = "/img/favicons/wikipedia.ico";
			return {
	  			title, favicon
			}
		},
		/* TikTok, where the hip kids are hanging out */
		tiktok: () => {
			let title = "Explore - Find your favourite videos on TikTok";
			let favicon = "/img/favicons/tiktok.ico";
			return {
				title, favicon
			}
		},
		/* Facebook, your grandma is most likely here */
		facebook: () => {
			/* Pick a random notification number between 1 and 100 */
			let count = Math.round(Math.random() * 99) + 1;
			let title = "(" + count + ") Facebook";
			let favicon = "/img/favicons/facebook.ico";
			return {
				title, favicon
			}
		},
		/* Instagram */
		instagram: () => {
			/* Pick a random notification number between 1 and 100 */
			let count = Math.round(Math.random() * 99) + 1;
			let title = "(" + count + ") Instagram";
			let favicon = "/img/favicons/instagram.png";
			return {
				title, favicon
			}
		}
	}

	/* Those "services" are enabled, which means the web browser tab can change
		favicon/title using their data. */
	this.enabledServices = [
		'x',
		'reddit',
		'bluesky',
		'instagram',
		'tiktok',
		'facebook',
		'wikipedia'
	];

	/* Initialization function, checks if the web browser has the specified event
		listeners and binds a handler to the existing one. */
	this.init = function () {
		if (typeof document.mozHidden !== 'undefined') {
			this.hidden = "mozHidden";
			this.visibilityChange = "mozvisibilitychange";
		} else if (typeof document.msHidden !== 'undefined') {
			this.hidden = "msHidden";
			this.visibilityChange = "msvisibilitychange";
		} else if (typeof document.webkitHidden !== 'undefined') {
			this.hidden = "webkitHidden";
			this.visibilityChange = "webkitvisibilitychange";
		}
		document.addEventListener(this.visibilityChange, this.handler.bind(this), false);
	}

	/* The default function which returns the initial favicon/title pair of the
		page, so it can get swapped back upon tab activation. */
	this.default = function () {
		let title = this.title;
		let favicon = this.favicon;
		this.update({
			title, favicon
		});
	}

	/* This function updates the favicon/title pair of the web browser tab when
		the tab is not focused (hidden from view). We're using a cache-busting
		technique so that the favicon is freshly loaded and not cached. */
	this.update = function (data) {
		let cacheBuster = "?v=" + Math.round(Math.random() * 10000000);
		let link  = document.createElement('link');
		link.type = "image/x-icon";
		link.rel = "shortcut icon";
		link.href = data.favicon + cacheBuster;
		document.getElementsByTagName("head")[0].querySelector("[rel='shortcut icon']").remove();
		document.getElementsByTagName("head")[0].appendChild(link);
		document.title = data.title;
	}

	/* The spoof() function randomizes the enabled "services" and picks one from
		them, updating the tab favicon and title. */
	this.spoof = function () {
		let i = Math.round(Math.random() * (this.enabledServices.length - 1));
		let service = this.enabledServices[i];
		if (service && this.services[service]) {
			this.update(this.services[service]());
		}
	}

	/* The default event handler which checks whether the current tab is hidden,
		and if it is then it swaps the favicon/title pair with one from the
		enabled "services". Otherwise, it shows the default favicon and title. */
	this.handler = function () {
		if (document[this.hidden]) {
			this.spoof();
		} else {
			this.default();
		}
	}

	/* Autorun the initialization function. */
	this.init();
}

document.addEventListener("DOMContentLoaded", function(event) {
	favicons();
});
