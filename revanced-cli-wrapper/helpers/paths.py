#!/usr/bin/python3
# ReVanced Wrapper - Path list

import os

# Root of everything
# Go one level up, because we're in /tools
PATH_BASE = os.path.dirname(__file__) + '/..'

# Roots
PATH_APK = f"{PATH_BASE}/apk"
PATH_TOOLS = f"{PATH_BASE}/tools"
PATH_RUNTIME_DATA = f"{PATH_BASE}/runtimeData"
PATH_TEMP = f"{PATH_BASE}/temp"

# The real ReVanced stuff
PATH_CLI = f"{PATH_TOOLS}/revanced-cli.jar"
PATH_PATCHES = f"{PATH_TOOLS}/revanced-patches.jar"
PATH_PATCHES_INFO = f"{PATH_TOOLS}/patches.json"
PATH_INTEGRATIONS = f"{PATH_TOOLS}/app-release-unsigned.apk"
PATH_VERSION = f"{PATH_TOOLS}/_versions.ini"

# Runtime data
PATH_KEYSTORE = f"{PATH_RUNTIME_DATA}/revanced.keystore"

# API for version checking
API_BASE = 'https://api.github.com/repos/revanced/revanced-{part}/releases'
API_V_CLI = API_BASE.format(part='cli')
API_V_PATCHES = API_BASE.format(part='patches')
API_V_INTEGRATIONS = API_BASE.format(part='integrations')

def createFoldersIfNotExist():
    if not os.path.isdir(PATH_TOOLS): os.mkdir(PATH_TOOLS)
    if not os.path.isdir(PATH_APK): os.mkdir(PATH_APK)
    if not os.path.isdir(PATH_RUNTIME_DATA): os.mkdir(PATH_RUNTIME_DATA)
    if not os.path.isdir(PATH_TEMP): os.mkdir(PATH_TEMP)
