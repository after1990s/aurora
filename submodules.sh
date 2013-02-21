#!/bin/bash
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

rm vendors -rfv
mkdir vendors
cd vendors

grep 'url = ' ../.gitmodules | while read x; do
    REPO=$(echo $x | cut -d '=' -f 2)
    git clone $REPO &
done
