#!/usr/bin/python
import requests
import core


def dead_links():
    links = []
    errors = []
    sections = core.get_sections()
    for section in sections:
        for link in core.get_links(section):
            error_msg = "error in {}\n{} not found".format(section, link)
            try:
                response = requests.get(link)
                if response.status_code < 400:
                    print("{}: {} => OK".format(section, link))
                    continue
                errors.append(link)
                core.fail(error_msg, interupt=False)
            except requests.exceptions.ConnectionError:
                core.fail(error_msg, interupt=False)
    if errors:
        core.fail("{} dead link found", interupt=True)

