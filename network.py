import pandas as pd
import argparse
import csv; import math; import sys; 
from string import punctuation
from operator import itemgetter
import re as re
csv.field_size_limit(sys.maxsize)

def main():
    # contains the "id" as the key and "list of friends" as values
    all_friends_dict = {}
    file = sys.argv[1]
    with open(file, 'w') as file_object:       
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['friends'] != "None": 
                    all_friends_dict[row['user_id']] = row['friends'].split(', ')

        for key, value in all_friends_dict.items():
            for friend in value:
                if friend in all_friends_dict.keys():
                    if key in all_friends_dict[friend]:
                        all_friends_dict[key].remove(friend)
                    elif not key in all_friends_dict[friend]:
                        file_object.write(str(key + "-->" +  friend + "\n")) 
                        # print(key, "-->", friend)    
                else:
                    file_object.write(str(key +  "-->"+ friend + "\n")) 
                # print(key, "-->", friend)

if __name__ == "__main__":
    main()