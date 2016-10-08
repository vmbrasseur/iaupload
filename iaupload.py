#!/usr/bin/env python

###
# Script to upload to IA using the Python library
# Quick & dirty for now. Many TODO items below for future enhancement
###

import internetarchive
import yaml
import pprint
import argparse

###
# TODO: Add some command line args; hard coding everything for now
# --access_key
# --secret_key
# --directory (repeatable; recursive; push to files)
# --verbose
# --debug
# --log
# --logfile
###

###
# For debug purposes
###
pp = pprint.PrettyPrinter(indent=2)


ap = argparse.ArgumentParser(description="Upload files to Internet Archive.")
ap.add_argument('--config',
                dest="config",
                default="./iaupload.yaml",
                help="Path and filename of YAML config file"
               )
ap.add_argument('--metadata',
                dest="metadata",
                default="./md.yaml",
                help="Path and filename of YAML metadata file"
               )
ap.add_argument('--identifier',
                dest='identifier',
                help="Identifier of Internet Archive item to which to upload the file(s)",
                required=True
               )
ap.add_argument('file',
                nargs='+',
                help="File to upload (repeatable)"
               )
args = ap.parse_args()

config = args.config
identifier = args.identifier
mdfile = args.metadata
files = args.file
itemurlbase = "https://archive.org/details/"

###
# Load the authorization keys
###

# TODO: check for error on open
f = open(config)
auths = yaml.safe_load(f)
f.close()
aws_access_key_id = auths['aws_access_key_id']
aws_secret_access_key = auths['aws_secret_access_key']

###
# Build metadata dict
###
f = open(mdfile)
md = yaml.safe_load(f)
f.close()
# TODO: Check for required fields.
#pp.pprint(md)


###
# Connect to IA
###
# TODO: Assumes new item. Can check for exists by getting the item
#       then seeing the value of the 'exists' key:
#       print item
#       Item(identifier='sfperlmongerslightningtalks2014', exists=False)
item = internetarchive.get_item(identifier)

# TODO: change this to a boolean to avoid the +=1 each iteration of the loop
#       just set it to FALSE at the end of its if block
num = 1

print "There are", len(files), "files to upload.\n"

###
# Loop through files to allow for progress printing
###
# TODO: Add some sort of simple/basic progress indicator (. every 30s?)
for file in files:
  print "Uploading ", file, "\n"
  if num == 1:
    # Only the first file needs to send metadata
    item.upload(file, access_key=aws_access_key_id, secret_key=aws_secret_access_key, metadata=md)
  else:
    item.upload(file, access_key=aws_access_key_id, secret_key=aws_secret_access_key)
  num += 1

### item.upload(files, access_key=aws_access_key_id, secret_key=aws_secret_access_key, metadata=md)

###
# TODO: Add unit tests
###

###
# All done
###
print "Item URL is: ", itemurlbase + identifier, "\n"
