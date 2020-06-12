import argparse
from pathlib import Path
import re
import sys

import requests


BASEDIR = Path(".")


def check_link(link, bookmark_file, only_error=False):
    invalid = False
    msg = f"{bookmark_file}: {link} => OK"
    try:
        response = requests.get(link)
        status = response.status_code
        if status >= 400:
            msg = f"{bookmark_file}: {link} => KO ({status})"
            invalid = True
    except requests.exceptions.ConnectionError:
        msg = f"{bookmark_file}: {link} => KO (connection error)"
        invalid = True
    if only_error and not invalid:
        return invalid
    print(msg)
    return invalid


def check_file(bookmark_file, only_error=False):
    invalid = True
    with open(bookmark_file) as content:
        for line in content.readlines():
            if "http" not in line:
                continue
            match = re.search("(?P<url>https?://[^\s]+)", line).group("url")
            link = match.replace(')', '')
            check_link(link, bookmark_file, only_error)
    return invalid


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--only-error', action='store_true')
    args = parser.parse_args()
    invalid = False
    for bookmark_file in list(BASEDIR.glob('**/*.md')):
        invalid = check_file(
            bookmark_file,
            args.only_error)
    sys.exit(int(invalid))


if __name__ == "__main__":
    main()
