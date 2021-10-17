# !/usr/bin/env python3

"""
Fetching language data from remote location.
Using http://www.manythings.org/anki/
"""

import argparse
import requests
import git
from pathlib import Path
import zipfile
import os

parser = argparse.ArgumentParser(description=
                                 '''Fetching language data from manythings.org/anki/. Use supported language 
                                  combination i.e bel-eng''',
                                 epilog=
                                 """Thanks for using the importer tool."""
                                 )

parser.add_argument('--pair', type=str, default="ell-eng", help='Language pair')
args = parser.parse_args()

BASE_URL = 'http://www.manythings.org/anki/'


def get_lang_dir(path='.'):
    git_repo = git.Repo(path, search_parent_directories=True)
    git_root = git_repo.git.rev_parse('--show-toplevel')

    return git_root


LANG_DIR = get_lang_dir() + '/langdir/'
Path(LANG_DIR).mkdir(parents=True, exist_ok=True)

class Importer(object):
    def __init__(self):
        data_version = None
        url = BASE_URL + args.pair + '.zip'
        datafile = LANG_DIR + args.pair + '.zip'
        garbage = LANG_DIR + '_about.txt'

        # Fetching the archive
        r = requests.get(url, stream=True)
        with open(datafile, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)


        self.fixBadZipfile(datafile)
        # Unzipping and throwing away archive
        with zipfile.ZipFile(datafile, 'r') as zip_ref:
            zip_ref.extractall(LANG_DIR)

        os.remove(datafile)
        os.remove(garbage)

        print('Done.')


    def fixBadZipfile(self, zipFile):  
        f = open(zipFile, 'r+b')  
        data = f.read()  
        pos = data.find(b'\x50\x4b\x05\x06') # End of central directory signature  
        if (pos > 0):  
            print("Trancating file at location " + str(pos + 22)+ ".")  
            f.seek(pos + 22)   # size of 'ZIP end of central directory record' 
            f.truncate()  
            f.close()  
        else:  
            raise ValueError('The downloaded file is truncated.')
            exit

if __name__ == '__main__':
    I = Importer()
