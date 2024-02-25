// ==UserScript==
// @name        AMOLED black background + no-script
// @namespace   https://viayoo.com/
// @version     1
// @run-at      document-start
// @match       https://*/*
// @grant       none
// ==/UserScript==

(function() {
    'use strict';
    
    // no-script: Remove all <script> tags in the document
    document.querySelectorAll('script').forEach(e => e.remove());
    
    // Force AMOLED black background
    const customCssTag = document.createElement('style');
    customCssTag.type = 'text/css';
    customCssTag.innerHTML = [
        '* {',
            'background-color: #000 !important;',
            'border-color: #000 !important;',
            'outline-color: #000 !important;',
        '}',
    ].join('');
    document.querySelector('head').appendChild(customCssTag);
})();