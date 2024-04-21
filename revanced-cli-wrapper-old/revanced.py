# The real MVP:
# https://old.reddit.com/r/revancedapp/comments/va2dfg/how_to_use_cli_to_get_the_nonroot_version/ic26nxf/

################################################################################

import os
import sys

from helpers import paths
from helpers.patchList import printCompatibleApps, printCompatiblePatches
from helpers.updater import checkAndDownloadUpdate


def executeCommand(additionalArgs):
    COMMAND = [
        f'java',
        f'-jar "{paths.PATH_CLI}"',
        f'--bundle="{paths.PATH_PATCHES}"',
        f'--exclusive',
        f'--merge="{paths.PATH_INTEGRATIONS}"',
        f'--keystore="{paths.PATH_KEYSTORE}"',
        f'--temp-dir="{paths.PATH_TEMP}"'
    ]
    if len(additionalArgs) == 0:
        COMMAND.append('--help')
    else:
        COMMAND.extend(additionalArgs)
    os.system(' '.join(COMMAND))

################################################################################

def main():

    paths.createFoldersIfNotExist()

    if len(sys.argv) == 2:
        _, command = sys.argv
        
        if command == 'compat':
            printCompatibleApps()
            print('Specify a package name to check for patch availability.')
            exit()
        
        if command == 'patch':
            print('Specify a subfolder name in /apk to start patching.')
            print('Make sure original.apk and selectedPatches.txt is available.')
            exit()
        
        if command == 'update':
            checkAndDownloadUpdate()
            exit()

    if len(sys.argv) == 3:
        _, command, package = sys.argv

        if command == 'compat':
            WELL_KNOWN_PACKAGE_NAMES = {
                'youtube': 'com.google.android.youtube',
                'yt': 'com.google.android.youtube',
                'youtube-music': 'com.google.android.apps.youtube.music',
                'yt-music': 'com.google.android.apps.youtube.music',
                'twitter': 'com.twitter.android',
                'tiktok-m': 'com.zhiliaoapp.musically',
                'tiktok-t': 'com.ss.android.ugc.trill',
                'twitch': 'tv.twitch.android.app',
            }
            if package in WELL_KNOWN_PACKAGE_NAMES:
                printCompatiblePatches(WELL_KNOWN_PACKAGE_NAMES[package])
            else:
                printCompatiblePatches(package)
            exit()
        
        if command == 'patch':
            _PATH_PACKAGE = f"{paths.PATH_APK}/{package}"
            _PATH_PACKAGE_ORIGINAL_APK = f"{_PATH_PACKAGE}/original.apk"
            _PATH_PACKAGE_REVANCED_APK = f"{_PATH_PACKAGE}/revanced.apk"
            _PATH_PACKAGE_SELECTED_PATCHES = f"{_PATH_PACKAGE}/selectedPatches.txt"
            # check if subfolder exist and required files exist
            if not os.path.isdir(_PATH_PACKAGE):
                print(f"Package does not exist in /apk: {package}")
                exit(1)
            if not os.path.isfile(_PATH_PACKAGE_ORIGINAL_APK):
                print(f"original.apk does not exist in package: {package}")
                exit(1)
            if not os.path.isfile(_PATH_PACKAGE_SELECTED_PATCHES):
                print(f"selectedPatches.txt does not exist in package: {package}")
                exit(1)
            
            # if everything's ready, call the CLI
            SELECTED_PATCHES = []
            with open(_PATH_PACKAGE_SELECTED_PATCHES) as f:
                SELECTED_PATCHES = f.read().split()
            
            ADDITIONAL_FLAGS = [
                f'--apk="{_PATH_PACKAGE_ORIGINAL_APK}"',
                f'--out="{_PATH_PACKAGE_REVANCED_APK}"',
            ]
            ADDITIONAL_FLAGS.extend(map(
                lambda p: f"--include {p}",
                SELECTED_PATCHES
            ))
            executeCommand(ADDITIONAL_FLAGS)
            exit()

    executeCommand(sys.argv[1:])

if __name__ == "__main__":
    main()
