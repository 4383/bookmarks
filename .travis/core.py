#!/usr/bin/python
import glob, os
import re
import sys


CWD = os.getcwd()
SECTIONS_PATH = os.path.join(CWD, 'sections')


def get_sections():
    os.chdir(SECTIONS_PATH)
    return glob.glob("*.md")


def get_links(section):
    section = os.path.join(SECTIONS_PATH, section)
    links = []
    with open(section) as content:
        for line in content.readlines():
            if "http" not in line:
                continue
            match = re.search("(?P<url>https?://[^\s]+)", line).group("url")
            links.append(match.replace(')', ''))
    return links


def fail(message, interupt=True):
    print("+" * 50)
    print(message)
    if interupt:
        print("execution interrupt")
    print("+" * 50)
    if interupt:
        sys.exit(1)
