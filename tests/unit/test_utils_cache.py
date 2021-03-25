#!/usr/bin/env python3

from ..utils import cache


def test_create():
    assert cache.create() == 1


def test_clean():
    assert cache.clean() == 2
