const homeWikilink = '@Index/Home';

const { Plugin, Notice } = require('obsidian');

module.exports = class JumpToHomePlugin extends Plugin {
    async onload() {
        this.addCommand({
            id: 'jump-to-home',
            name: 'Jump to Home',
            callback: this.jumpToHome.bind(this),
        });
    }
    async jumpToHome() {
        this.app.workspace.openLinkText(homeWikilink, '');
    }
}

