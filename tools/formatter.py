# !/usr/bin/env python3

"""
Preparing data fetched with tools/importer.py 
Data from http://www.manythings.org/anki/
"""

import argparse
import re
import string
from pickle import dump
from unicodedata import normalize
from numpy import array
import os
from pathlib import Path

from importer import LANG_DIR

parser = argparse.ArgumentParser(description=
                                 '''Cleaning language data. Expecting data to be in a <langdir> directory
                                 in the project's root. If not, provide --location flag. ''',
                                 epilog=
                                 """Thanks for using the formatter tool."""
                                 )

parser.add_argument('--location', type=str, default="", help='Langdir directory location')
parser.add_argument('--mto', type=bool, default=True, help='Data fetched from ManyThingsOrg')
args = parser.parse_args()


class MTO(object):
    def __init__(self, dn) -> None:
        data_version = None
        files = os.listdir(dn)
        files = self.prepend(files, dn)
        
        for f in files:
            name = Path(f).stem
            print(name)
            doc = self.load_doc(f)
            pairs = self.to_pairs(doc)
            clean_pairs = self.clean_pairs(pairs)
            self.save_clean_data(clean_pairs, dn + name + '.pkl')
            os.remove(f)
                    
       
    def prepend(self, list, str):
        str += '{0}'
        list =  [str.format(i) for i in list]
        
        return(list)
    
    def load_doc(self, filename):
        f = open(filename, mode='rt', encoding='utf-8')
        text = f.read()
        f.close()
        
        return text
    
    def to_pairs(self, doc):
        lines = doc.strip().split('\n')
        pairs = [line.split('\t') for line in lines]
        
        return pairs
    
    def clean_pairs(self, lines):
        cleaned = list()
        re_print = re.compile('[^%s]' % re.escape(string.printable))
        table = str.maketrans('', '', string.punctuation)
        for pair in lines:
            clean_pair = list()
            for line in pair:
                # normalize unicode characters
                line = normalize('NFD', line).encode('ascii', 'ignore')
                line = line.decode('UTF-8')
                # tokenize on white space
                line = line.split()
                # convert to lowercase
                line = [word.lower() for word in line]
                # remove punctuation from each token
                line = [word.translate(table) for word in line]
                # remove non-printable chars form each token
                line = [re_print.sub('', w) for w in line]
                # remove tokens with numbers in them
                line = [word for word in line if word.isalpha()]
                # store as string
                clean_pair.append(' '.join(line))
            cleaned.append(clean_pair)
        
        # Numpy array        
        return array(cleaned)
    
    
    def save_clean_data(self, sentences, filename):
       dump(sentences, open(filename, 'wb'))
       print('Saved: %s' % filename)
        
if __name__ == '__main__':
    # Decide on whether to process in MTO, or other fashion.
    if args.mto:
        formatter = MTO(LANG_DIR)
    else:
        # TODO: other formatters
        # use args.location for other formatters
        exit
