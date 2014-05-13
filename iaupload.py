#!/usr/bin/env python

###
# Script to upload to IA using the Python library
# Quick & dirty for now. Many TODO items below for future enhancement
###

import internetarchive
import yaml
import pprint

###
# TODO: Add some command line args; hard coding everything for now
# --config
# --access_key
# --secret_key
# --identifier
# --file (repeatable)
# --directory (repeatable; recursive; push to files)
# --verbose
# --metadata (YAML)
# --debug
# --log
# --logfile
# --help
###

config = "./iaupload.yaml"
identifier = "sfperlmongerslightningtalks2014"
mdfile = "/Users/brasseur/Desktop/md.yaml"
files = ['/Users/brasseur/Desktop/Lightning_Talk_Slides/02-Quinn_Weaver-Semantic_Versioning.pdf',
         '/Users/brasseur/Desktop/Lightning_Talk_Slides/03-Eric_Eslinger-Token-Based_Authentication_with_AngularJS.pdf',
         '/Users/brasseur/Desktop/Lightning_Talk_Slides/04-Daniel_Lieberman-Breaking_Habits.pdf',
         '/Users/brasseur/Desktop/Lightning_Talk_Slides/05-Asheesh_Laroia-Welcoming_New_Contributors_What_Ive_Learned_as_a_Debian_Developer.pdf',
         '/Users/brasseur/Desktop/Lightning_Talk_Slides/06-Josh_Berkus-Scale_Fail.pdf',
         '/Users/brasseur/Desktop/Lightning_Talk_Slides/07-Quinn_Weaver-Python_vs_Perl_Some_Gotchas.pdf',
         '/Users/brasseur/Desktop/Lightning_Talk_Slides/08-Eric_Eslinger-Big_Mistakes_in_Educational_Technology.pdf',
         '/Users/brasseur/Desktop/Lightning_Talk_Slides/09-Darin_Wilson-Coding_Calisthenics_with_Exercism.io.pdf',
         '/Users/brasseur/Desktop/Lightning_Talk_Slides/10-Mike_Covington-Improving_Reproducibility_and_Record_Keeping_with_Log_Reproducible.pdf',
         '/Users/brasseur/Desktop/Lightning_Talk_Slides/11-Caroline_Burns-Perl_Selenium.pdf',
         '/Users/brasseur/Desktop/Lightning_Talk_Videos/01-Fred_Moyer-Ready_Set_Go.mov',
         '/Users/brasseur/Desktop/Lightning_Talk_Videos/02-Quinn_Weaver-Semantic_Versioning.mov',
         '/Users/brasseur/Desktop/Lightning_Talk_Videos/03-Eric_Eslinger-Token-Based_Authentication_with_AngularJS.mov',
         '/Users/brasseur/Desktop/Lightning_Talk_Videos/05-Asheesh_Laroia-Welcoming_New_Contributors_What_Ive_Learned_as_a_Debian_Developer.mov',
         '/Users/brasseur/Desktop/Lightning_Talk_Videos/06-Josh_Berkus-Scale_Fail.mov',
         '/Users/brasseur/Desktop/Lightning_Talk_Videos/07-Quinn_Weaver-Python_vs_Perl_Some_Gotchas.mov',
         '/Users/brasseur/Desktop/Lightning_Talk_Videos/08-Eric_Eslinger-Big_Mistakes_in_Educational_Technology.mov',
         '/Users/brasseur/Desktop/Lightning_Talk_Videos/09-Darin_Wilson-Coding_Calisthenics_with_Exercism.io.mov',
         '/Users/brasseur/Desktop/Lightning_Talk_Videos/10-Mike_Covington-Improving_Reproducibility_and_Record_Keeping_with_Log_Reproducible.mov',
         '/Users/brasseur/Desktop/Lightning_Talk_Videos/11-Caroline_Burns-Perl_Selenium.mov',
         '/Users/brasseur/Desktop/Lightning_Talk_Videos/12-Stephen_Corona-Why_You_Should_Write_a_Tech_eBook.mov'
]

###
# For debug purposes
###
pp = pprint.PrettyPrinter(indent=2)

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
