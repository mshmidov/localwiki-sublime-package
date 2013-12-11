import os
import re
import errno


LINK_REGEX = '\[(.+?)\](?:\((.+?)\))?'
LINK_PATTERN = re.compile(LINK_REGEX)

KEEP_CHARACTERS = (' ', '.', '_')


def safe_file_name(name):
    return "".join(c for c in name.lower() if c.isalnum() or c in KEEP_CHARACTERS) \
        .rstrip() \
        .replace(' ', '_')


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise