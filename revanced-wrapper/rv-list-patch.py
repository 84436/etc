#!/usr/bin/env python3
# Dirty ReVanced Script: List packages with package-specific patches

import json
import sys

# Get specified package name from the arguments if available
specified_package = None
if len(sys.argv) == 2:
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

# Read patch file
f = open('patches.json', 'r')
patches = json.load(f)
f.close()

# Get all supported packages
supported_packages = set(
    package['name']
    for patch in patches
    if 'compatiblePackages' in patch and patch['compatiblePackages'] is not None
    for package in patch['compatiblePackages']
)

# If there's no specific package name, list all supported packages
if specified_package is None:
    for package in sorted(supported_packages):
        print(f'- {package}')
    print(f'{len(supported_packages)} packages.')
    print('To list compatible patches for a specific package, pass the package ID as the only argument to this script.')

# If the specified package name is not in the supported list, exit
elif specified_package not in supported_packages:
    print(f'Package "{specified_package}" not supported.') 

# List compatible patches for the specified package name
else:
    compatible_patches = [
        patch
        for patch in patches
        if 'compatiblePackages' in patch and patch['compatiblePackages'] is not None
        if specified_package in [
            package['name']
            for package in patch['compatiblePackages']
        ]
    ]
    for patch in sorted(
        compatible_patches,
        key = lambda patch: patch['name']
    ):
        print(f"\"{patch['name']}\", # {patch['description']}")
    print(f'{len(compatible_patches)} patches for package "{specified_package}".')
