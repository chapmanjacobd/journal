I made a little userscript to help me keep track of which items I've looked at before. It will set to 50% the opacity of rows that your browser has loaded before. I'm surprised how useful it has been so far

This probably doesn't work on all sites, but TamperMonkey makes it easy to exclude a site when it breaks something. Please share similar scripts

    // ==UserScript==
    // @name         Hide Seen Rows
    // @namespace    http://tampermonkey.net/
    // @version      0.2
    // @description  Remember and hide unique rows based on URL
    // @author       BuonaparteII
    // @match        *://*/*
    // @grant        none
    // ==/UserScript==
    
    (function() {
        'use strict';
    
        function getRowIdentifier(row) {
            // Assuming the URL is in an anchor tag within the row
            let link = row.querySelector('a');
            return link ? link.href : null;
        }
    
        function hideRows() {
            let rows = document.querySelectorAll('table tr');
            rows.forEach(row => {
                let identifier = getRowIdentifier(row);
                if (identifier && localStorage.getItem(identifier)) {
                    row.style.opacity = 0.5;
                }
            });
        }
    
        function markRowsAsSeen() {
            let rows = document.querySelectorAll('table tr');
            rows.forEach(row => {
                let identifier = getRowIdentifier(row);
                if (identifier && !localStorage.getItem(identifier)) {
                    localStorage.setItem(identifier, Date.now().toString());
                }
            });
        }
    
        hideRows();
        markRowsAsSeen();
    })();
