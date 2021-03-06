#!/usr/bin/env python

import json
import logging
import requests
import sys

import botometer


CREDS = {}


def load_creds(fname):
    global CREDS

    try:
        with open(fname) as f:
            CREDS = json.load(f)
    except OSError as err:
        print("OS error:", err)
    except ValueError:
        print("Data error: Could not load json data.")
    except:
        print("Some crappy error:", sys.exc_info()[0])
        raise
    logging.debug(CREDS)


def get_user(handle):
    pass


if __name__ == "__main__":
    logging.basicConfig(
        format='%(levelname)s:%(message)s',
        level=logging.DEBUG
    )

    load_creds("my-data/creds.json")
    get_user("oley")
