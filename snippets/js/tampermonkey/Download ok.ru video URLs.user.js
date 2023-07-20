// ==UserScript==
// @name         Download ok.ru video URLs
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Download ok.ru video URLs
// @match        https://ok.ru/*
// @grant        none
// ==/UserScript==


function scrollAndCheck() {
    var previousScroll = window.pageYOffset;
    window.scrollBy(0, 1000);

    var currentScroll = window.pageYOffset;
    var maxScroll = document.body.scrollHeight - window.innerHeight;

    if (currentScroll + 10 >= maxScroll && previousScroll == currentScroll) {
        clearInterval(scrollInterval);
        downloadURLs();
    }
}

function downloadURLs() {
    var elements = document.getElementsByClassName("video-card_img-w");

    if (elements.length === 0) {
        return;
    }

    var urls = [];

    for (var i = 0; i < elements.length; i++) {
        var element = elements[i];

        if (element.id) {
            var id = element.id.replace("video-card_img_", "");

            var url = "https://ok.ru/video/" + id;

            url = url.slice(0, -1);

            urls.push(url);
        }
    }

    var text = urls.join("\n");
    var blob = new Blob([text], {type: "text/plain"});

    var link = document.createElement("a");
    link.href = URL.createObjectURL(blob);

    var pageID = window.location.pathname.split("/").pop();

    link.download = pageID + ".txt";

    document.body.appendChild(link);
    link.click();

    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);
}

var scrollInterval = setInterval(scrollAndCheck, 1000);