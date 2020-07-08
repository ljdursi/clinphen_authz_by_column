#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tests for `clinphen_service` package."""

import subprocess


def test_dredd():
    subprocess.check_call(['dredd', '--language=python',
                           '--hookfiles=./dreddhooks.py'],
                          cwd='./tests')
