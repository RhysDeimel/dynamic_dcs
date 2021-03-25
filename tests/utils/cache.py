#!/usr/bin/env python3

"""
Script for unpacking assets and creating a cache of resouces to test against

Default behaviour is to unpack all resources on test run and leave them there.
This might cause issues if assets are updated, so `clean` removes the cache.
"""


def create():
    return 1


def clean():
    return 2
