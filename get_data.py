#!/usr/bin/env python
"""
A script to downnload `the-counted.csv` dataset from http://interactive.guim.co.uk/2015/the-counted/thecounted-data.zip
"""

import os
import datetime
import zipfile

import requests

link = 'http://interactive.guim.co.uk/2015/the-counted/thecounted-data.zip'
counted_zip = 'thecounted-data.zip'
counted_csv = 'the-counted.csv'

with open(counted_zip, 'wb') as fi:
    print "Downloading {0}".format(link)
    r = requests.get(link)
    fi.write(r.content)

with zipfile.ZipFile(counted_zip) as fi:
    print "Unzipping {0}".format(counted_zip)
    fi.extract(counted_csv)
    os.remove(counted_zip)

with open('README.md', 'w') as fi:
    print "Updating README.md"
    dt = datetime.datetime.now()
    message = "\n- Updated csv on {0}".format(dt)
    fi.write(message)
