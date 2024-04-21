## etc

My collection of hacky & miscellaneous things. There's nothing really interesting here, but feel free to look around. (Also please don't expect quality code here.)

- `inter-custom`: My custom version of Inter
    - Font name: `Inter` (everywhere)
    - Font version: `4.000;git-a52131595`

- `iosevka-custom`: My custom version of Iosevka
    - Font name: `Iosevka Web` (web/CSS), `Iosevka` (everywhere else)
    - Font version: `28.0.4`
    - ttfautohint version: `1.8.4`
    - Slightly more expanded than the original font (width = 525/1000em)
    - CSS meant to be used with Obsidian; WOFFs are served raw from this repo

- `iosevka-custom-builder`: Windows batch scripts to build my custom version of Iosevka
    - Execution order: `do-clone`, `do-build`, `do-get-output`
    - Adjust the number of build threads in `do-build`

- `nextdns-template`: My template, script and custom configuration file format for batch-updating NextDNS profiles

- `obsidian`: Obsidian-related things (currently only hotkey templates)

- `obsidian-at-jump-to-home`: A plugin to add a command to jump to a designated "home" page in the vault

- `revanced-cli-wrapper-old`: Python-based wrapper for ReVanced CLI (abandoned)
    - Abandoned: I don't have the effort to maintain this; also ReVanced CLI has gotten more user-friendly (though not TUI-level of friendly).
    - `compat`, `patch`, `update`
    - Hint (to get started): `revanced update`
    - Another hint:
        ```
        │   revanced.py
        ├───apk
        │   ├───yt
        │   │       original.apk
        │   │       selectedPatches.txt
        │   └───yt-music
        │           original.apk
        │           selectedPatches.txt
        ├───helpers
        │       patchList.py
        │       paths.py
        │       updater.py
        ├───runtimeData
        │       revanced.keystore
        ├───temp
        └───tools
                app-release-unsigned.apk
                patches.json
                revanced-cli.jar
                revanced-patches.jar
                _versions.ini
        ```

- `revanced-wrapper`: A bunch of dirty scripts to run ReVanced Patcher. Think of this as a dumbed-down, simplified implementation of `revanced-cli-wrapper-old`.
    - `rv-download` first before doing other things
    - Each script is standalone, with the exception of `rv-patch`, which requires a "description file" (actually another script). See `youtube.revanced.py` for example.

- `via-browser-userscripts`: Userscripts for [Via Browser on Android](https://play.google.com/store/apps/details?id=mark.via.gp)

- `windows-recovery-kitchen`: A bunch of tiny scripts and configuration files to create a _minimally modified_ WinPE image off of the original WinRE (Windows Recovery) image.
    - This was intended for WinRE from Windows 11, but WinRE from Windows 10 might also be OK.
    - Emphasis on "_minimally modified_": no flashy graphics (and probably network connections) included, no extensive tool suite, and no "debloating" the original WinRE.
    - [LaunchBar by Peter Lerup](https://www.lerup.com/LaunchBar/) is used as the "shell" or program launcher. A copy of LaunchBar.exe is included here for preservation purposes.
    - The shutdown (`shutdown.ico`) and reboot (`reboot.ico`) icons are provided by [Icons8](https://icons8.com/).
    - The program list in `launchbar.ini` is provided as a suggestion only. Bring your own programs.
    - Yes, the cursor will be stuck in the busy state for some time while hovering on the empty desktop. That is normal, just go ahead and do stuff.
