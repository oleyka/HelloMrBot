#!/usr/bin/env python

import json
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
    print(CREDS)


def get_user(handle):
    pass


if __name__ == "__main__":
    load_creds("my-data/creds.json")
    get_user("oley")
