import pandas as pd
import argparse
import csv; import math; import sys; 
#from nltk.tokenize import word_tokenize
from string import punctuation
from operator import itemgetter
import re as re
csv.field_size_limit(sys.maxsize)

def main():
    all_friends_dict = {}
    name_mapper = {}
    file = sys.argv[1]
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name_mapper[row['user_id']] = row['name']
            all_friends_dict[row['user_id']] = row['friends'].split(', ')



    for item in all_friends_dict:
        for friend in all_friends_dict[item]:
            print(name_mapper[item], name_mapper[friend])




if __name__ == "__main__":
  main()