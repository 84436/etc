#!/usr/bin/env python3
# Dirty ReVanced Script: download CLI tool, patches and integration APK

import requests
import json

# Helpers
RELEASE_URL_TEMPLATE = 'https://api.github.com/repos/ReVanced/revanced-{repo}/releases/latest'
get_tag = lambda release: release['tag_name'].replace('v', '')
get_browser_download_url = lambda asset: asset['browser_download_url']
is_patch_bundle = lambda a: a['name'].endswith('.jar')
is_patch_info = lambda a: a['name'] == 'patches.json'
def fetch_release(repo):
    api_response = requests.get(RELEASE_URL_TEMPLATE.format(repo = repo))
    parsed_response = json.loads(api_response.text)
    return parsed_response
def download_file(url, filename):
    api_response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(api_response.content)

# CLI Tool
print('Fetching info: CLI')
cli = fetch_release('cli')
cli_tag = get_tag(cli)
cli_url = get_browser_download_url(cli['assets'][0])

# Patches
print('Fetching info: Patch Bundle & Patch Info')
patch = fetch_release('patches')
patch_tag = get_tag(patch)
patch_bundle_url = get_browser_download_url(
    next(a for a in patch['assets'] if is_patch_bundle(a))
)
patch_info_url = get_browser_download_url(
    next(a for a in patch['assets'] if is_patch_info(a))
)

# Integrations
print('Fetching info: Integrations')
integrations = fetch_release('integrations')
integrations_tag = get_tag(integrations)
integrations_url = get_browser_download_url(integrations['assets'][0])

# Downloads
print('Downloading CLI:', cli_tag)
download_file(cli_url, 'cli.jar')
print('Downloading Patch Bundle:', patch_tag)
download_file(patch_bundle_url, 'patches.jar')
print('Downloading Patch Info:', patch_tag)
download_file(patch_info_url, 'patches.json')
print('Downloading Integrations:', integrations_tag)
download_file(integrations_url, 'integrations.apk')
