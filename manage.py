#!/usr/bin/env python
# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aurora.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
