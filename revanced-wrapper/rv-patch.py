#!/usr/bin/env python3
# Dirty ReVanced Script: apply patches against a package

import os
import subprocess
import sys

# Variables expected to be defined in the description file
APP_NAME = None
APP_DISPLAY_NAME = None
TARGET_VERSION = None
PATCHES = None

# Check for the path to a description file in the arguments,
# then execute it.
if len(sys.argv) != 2 or not sys.argv[1].endswith('.revanced.py'):
    print('Specify path to a description file (whose extension is .revanced.py) as the only argument to this script.')
    exit(-1)
description_file_path = sys.argv[1]
with open(description_file_path, 'r') as f:
    # security 100
    # what could possibly go wrong with executing a random script
    exec(f.read())

# Check if the variables are actually defined
assert type(APP_NAME) is str
assert type(APP_DISPLAY_NAME) is str
assert type(TARGET_VERSION) is str
assert type(PATCHES) is list

# Paths
THIS = os.path.abspath(os.path.dirname(__file__))
WORKING_FOLDER_PATH = f"{THIS}\\{APP_NAME}-{TARGET_VERSION}"
INPUT_FILE_PATH = f"{WORKING_FOLDER_PATH}\\original.apk"
OUTPUT_FILE_PATH = f"{WORKING_FOLDER_PATH}\\{APP_DISPLAY_NAME} ({TARGET_VERSION}-revanced).apk"

# Includes
included_patches = []
for patch in PATCHES: included_patches.extend(['--include', f'{patch}'])

# Helpers
def run_shell_command(*args): subprocess.call(args, shell=True)

# The main stuff: invoking the CLI with a bunch of arguments
run_shell_command(
    'java',
    '-jar', f'{THIS}\\cli.jar',
    'patch',
    '--patch-bundle', f'{THIS}\\patches.jar',
    '--merge', f'{THIS}\\integrations.apk',
    '--keystore', f'{THIS}\\revanced.keystore',
    '--alias', 'ReVanced Key',
    '--options', f'{WORKING_FOLDER_PATH}\\options.json',
    '--resource-cache', f'{WORKING_FOLDER_PATH}\\cache',
    '--purge',
    '--exclusive',
    *included_patches,
    '--out', f'{OUTPUT_FILE_PATH}',
    f'{INPUT_FILE_PATH}'
)
