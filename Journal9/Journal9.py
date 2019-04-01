######################################################################
# Project           : Journal9
#
# Program name      : Journal9.py
#
# Author            : Evan Kivolowitz
#
# Date created      : 03/31/2019
#
# Purpose           : Automate the deployment process to an s3 bucket of mine.
#
# Credit            :
#
# Use                                    Source
#
# Docstring template                     https://www.phusewiki.org/wiki/index.php?title=Program_Header
# Template creation                      https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal4/ 
#
# Revision History  :
#
# Date        Author     Ref    Revision 
# 03/31/2019  Author      1     Initial work.
#
######################################################################
import os
import argparse
import json
import os.path
def expand_path(path):
    return os.path.realpath(os.path.expandvars(os.path.expanduser(path)))
    
if __name__ == '__main__':
    jsonFile = expand_path("~") + "/.s3sync.json"
    print(jsonFile)
    if not os.path.isfile(jsonFile):
        print("Please create ~/.s3sync.json")
        exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=str, help="Directory to upload. Defaults to current working directory", default=os.getcwd())

    args = parser.parse_args()
    directory = expand_path(args.directory)

    with open(jsonFile, "r") as f:

        data = json.loads(f.read())
        if not data[directory]:
            print("No entry in ~/.s3sync.json for directory {}".format(data['directory']))
            exit(1)
        dist = data[directory]['DIST']
        bucket = data[directory]['BUCKET']
        ret = os.system("""
            set -e # Fail fast
            # Copy over pages - not static js/img/css/downloads
            aws s3 sync --acl "public-read" --sse "AES256" {} s3://{}

            # Invalidate root page and page listings
            aws cloudfront create-invalidation --distribution-id {} --paths /        
        """.format(directory, bucket, dist))

        

