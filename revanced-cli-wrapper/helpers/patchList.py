import json

from . import paths


def _getCompatiblePatches(patches, targetPackageName):
    compatiblePatches = []
    for patch in patches:
        for package in patch['compatiblePackages']:
            if package['name'] == targetPackageName:
                if len(package['versions']) == 0: # Any version
                    compatiblePatches.append((patch['name'],))
                else:
                    compatiblePatches.append((patch['name'], max(package['versions'])))
    return compatiblePatches

def printCompatiblePatches(targetPackageName):
    patches = []
    with open(paths.PATH_PATCHES_INFO) as f:
        patches = json.load(f)
    compatiblePatches = _getCompatiblePatches(
        patches, targetPackageName
    )
    if len(compatiblePatches) == 0:
        print(f'Either there\'s no patches for "{targetPackageName}", or that package does not exist.')
    else:
        print(f"{len(compatiblePatches)} patches compatible with package: {targetPackageName}")
        for patch in compatiblePatches:
            if len(patch) == 1:
                print(f"* {patch[0]}: any")
            else:
                print(f"* {patch[0]}: {patch[1]}")

def _getCompatibleApps(patches):
    allApps = set()
    for patch in patches:
        for package in patch['compatiblePackages']:
            allApps.add(package['name'])
    allApps = list(sorted(allApps))
    return allApps

def printCompatibleApps():
    patches = []
    with open(paths.PATH_PATCHES_INFO) as f:
        patches = json.load(f)
    packages = _getCompatibleApps(patches)
    print(f'ReVanced is currently compatible with {len(packages)} packages:')
    for package in packages:
        print(f'* {package}')
