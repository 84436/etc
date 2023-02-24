import configparser
import json
import os

import pkg_resources
import requests

from . import paths


def checkLocal():
    cli_version, patches_version, integrations_version = None, None, None
    config = configparser.ConfigParser()
    try:
        config.read(paths.PATH_VERSION)
        cli_version = config['Versions']['CLI']
        patches_version = config['Versions']['Patches']
        integrations_version = config['Versions']['Integration']
    except:
        pass
    return cli_version, patches_version, integrations_version

def checkRemote():
    # CLI
    cli = [
        version
        for version in json.loads(requests.get(paths.API_V_CLI).text)
        if version['prerelease'] == False
    ][0]
    cli_version = cli['tag_name']
    cli_download = [file for file in cli['assets'] if file['content_type'] == 'application/java-archive'][0]['browser_download_url']

    # Patches
    patches = [
        version
        for version in json.loads(requests.get(paths.API_V_PATCHES).text)
        if version['prerelease'] == False
    ][0]
    patches_version = patches['tag_name']
    patches_download = [file for file in patches['assets'] if file['content_type'] == 'application/java-archive'][0]['browser_download_url']
    patches_info_version = patches_version
    patches_info_download = [file for file in patches['assets'] if file['content_type'] == 'application/json'][0]['browser_download_url']

    # Integration
    integrations = [
        version
        for version in json.loads(requests.get(paths.API_V_INTEGRATIONS).text)
        if version['prerelease'] == False
    ][0]
    integrations_version = integrations['tag_name']
    integrations_download = [file for file in integrations['assets'] if file['content_type'] == 'application/vnd.android.package-archive'][0]['browser_download_url']

    return (
        (cli_version, cli_download),
        (patches_version, patches_download),
        (patches_info_version, patches_info_download),
        (integrations_version, integrations_download)
    )

def downloadFile(url, targetPath):
    file = requests.get(url)
    if file.ok:
        if os.path.isfile(targetPath):
            os.remove(targetPath)
        with open(targetPath, 'wb') as f:
            f.write(file.content)
    else:
        return RuntimeError(f'Failed to download file: {url} -> {targetPath}')

def checkAndDownloadUpdate():
    # Helper
    parse_version = lambda v: pkg_resources.packaging.version.parse(v)
    rewrite_version_file = False

    # Check for local version
    cli_v_local, patches_v_local, integrations_v_local = checkLocal()
    print('\n'.join([
        'Local version:',
        f"CLI: {cli_v_local}",
        f"Patches: {patches_v_local}",
        f"Integrations: {integrations_v_local}"
    ]))

    # In case the versions are empty,
    # assign an empty string so that they can be parsed by parse_version()
    if (cli_v_local == None): cli_v_local = ''
    if (patches_v_local == None): patches_v_local = ''
    if (integrations_v_local == None): integrations_v_local = ''

    # Check for remote version
    (cli_v_remote, cli_url_remote), (patches_v_remote, patches_url_remote), (patches_info_v_remote, patches_info_url_remote), (integrations_v_remote, integrations_url_remote) = checkRemote()
    if (parse_version(cli_v_remote) > parse_version(cli_v_local)):
        rewrite_version_file = True
        print(f"Downloading new version for CLI: {cli_v_remote}")
        downloadFile(cli_url_remote, paths.PATH_CLI)
    if (parse_version(patches_v_remote) > parse_version(patches_v_local)):
        rewrite_version_file = True
        print(f"Downloading new version for Patches: {patches_v_remote}")
        downloadFile(patches_url_remote, paths.PATH_PATCHES)
        print(f"Downloading new version for Patch Info: {patches_v_remote}")
        downloadFile(patches_info_url_remote, paths.PATH_PATCHES_INFO)
    if (parse_version(integrations_v_remote) > parse_version(integrations_v_local)):
        rewrite_version_file = True
        print(f"Downloading new version for Integrations: {integrations_v_remote}")
        downloadFile(integrations_url_remote, paths.PATH_INTEGRATIONS)
    
    # If there were new versions, update the file
    if rewrite_version_file:
        config = configparser.ConfigParser()
        config.add_section('Versions')
        config['Versions']['CLI'] = cli_v_remote
        config['Versions']['Patches'] = patches_v_remote
        config['Versions']['Integration'] = integrations_v_remote
        with open(paths.PATH_VERSION, 'w') as f:
            config.write(f)

    print('Everything up-to-date.')
