#!/bin/bash

if [ ! -d venv ] ; then
    virtualenv venv
    venv/bin/pip install -r requirements.txt
fi

venv/bin/python server.py
