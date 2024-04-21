#!/usr/bin/env python3
# Dirty ReVanced Script: count number of patches available for each versions of a given package
# (basically a thin wrapper for the list-versions command in the CLI)

import os
import subprocess
import sys

# Get specified package name
if len(sys.argv) != 2:
    print('Specify the package name as the only argument to this script.')
    exit(1)
specified_package = sys.argv[1]

# Define shorthands for common packages
PACKAGE_SHORTHANDS = {
    'youtube': 'com.google.android.youtube',
    'yt': 'com.google.android.youtube',
    'youtube-music': 'com.google.android.apps.youtube.music',
    'yt-music': 'com.google.android.apps.youtube.music',
    'ytm': 'com.google.android.apps.youtube.music',
    'instagram': 'com.instagram.android',
    'reddit': 'com.reddit.frontpage',
    'spotify': 'com.spotify.music',
    'twitter': 'com.twitter.android',
}
if specified_package in PACKAGE_SHORTHANDS:
    specified_package = PACKAGE_SHORTHANDS[specified_package]

# Paths
THIS = os.path.abspath(os.path.dirname(__file__))

# Helpers
def run_shell_command(*args): subprocess.call(args, shell=True)

# The main stuff
run_shell_command(
    'java',
    '-jar', f'{THIS}\\cli.jar',
    'list-versions',
    '--filter-package-names', f'{specified_package}',
    f'{THIS}\\patches.jar',
)