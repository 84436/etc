################################################################################
# Constants and Helpers

import copy
import json
import string

import requests
import yaml


def transform_to_object_id(s):
    return { 'id': s }

def transform_to_object_id_active(s):
    if type(s) is str:
        return { 'id': s, 'active': True }
    elif type(s) is dict:
        id = list(s.keys())[0]
        active = s[id]
        return { 'id': id, 'active': active }

def apply_array_transformation(settings, path, transformer):
    _settings = copy.deepcopy(settings)
    c = _settings # cursor
    for path_fragment in path.split('.'):
        c = c[path_fragment]
    for (index, value) in enumerate(c):
        c[index] = transformer(value)
    return _settings

API_ENDPOINT = 'https://api.nextdns.io/profiles'
PROFILES_FILENAME = 'nextdns-profiles.yml'
SETTINGS_FILENAME = 'nextdns-settings.yml'

PNAME_ALLOWED_CHARACTERS = set(''.join([
    string.ascii_letters, # a-z, A-Z
    string.digits, # 0-9
    '-'
]))

TRANSFORMATIONS = [
    ('privacy.blocklists', transform_to_object_id),
    ('privacy.natives', transform_to_object_id),
    ('parentalControl.services', transform_to_object_id_active),
    ('parentalControl.categories', transform_to_object_id_active),
    ('denylist', transform_to_object_id_active),
    ('allowlist', transform_to_object_id_active),
]

################################################################################

profiles = None
shared_settings = None

with open(PROFILES_FILENAME, 'r', encoding='utf-8') as f:
    # Load profile list
    profiles = yaml.load(f, Loader=yaml.CLoader)
    for p in profiles:
        if set(p['profileName']) > PNAME_ALLOWED_CHARACTERS:
            print(f"Invalid profile name: {p['profileName']}")
            exit(-1)
    print(f'{PROFILES_FILENAME}: loaded')

with open(SETTINGS_FILENAME, 'r', encoding='utf-8') as f:
    # Load shared settings file
    shared_settings = yaml.load(f, Loader=yaml.CLoader)
    for (path, transformer) in TRANSFORMATIONS:
        shared_settings = apply_array_transformation(shared_settings, path, transformer)
    print(f'{SETTINGS_FILENAME}: loaded')

    # For each profile...
    for p in profiles:
        apiKey, pid, pname = p['apiKey'], p['profileId'], p['profileName']
        psettings = copy.deepcopy(shared_settings)

        # Rename the profile
        psettings['name'] = pname

        # Call the API
        psettings_json = json.dumps(psettings)
        r = requests.patch(
            f'{API_ENDPOINT}/{pid}',
            headers = {
                'Content-Type': 'application/json',
                'X-Api-Key': apiKey,
            },
            data = psettings_json,
        )
        if r.ok:
            print(f'{pname}: OK')
        else:
            print(f'{pname}: HTTP {r.status_code}: {r.text}')
