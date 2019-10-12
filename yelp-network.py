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
    filename = 'yelp-network.txt'
    

    # contains the "id" as the key and "list of friends" as values
    file = sys.argv[1]

    # opening file to read and write
    with open(filename, 'w') as file_object:
       
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # if the friends list of an id is NOT empty then spliting the friend list and putting it in the dictionary
            for row in reader:
                if row['friends'] != "None": 
                    all_friends_dict[row['user_id']] = row['friends'].split(', ')


        # checking if the friend in the list occurs at multiple places then writing it only once in the file
        for key, value in all_friends_dict.items():
            for friend in value:
                if friend in all_friends_dict.keys():
                    if key in all_friends_dict[friend]:
                        
                        # removing the friend from the dictionary
                        all_friends_dict[key].remove(friend)
                    elif not key in all_friends_dict[friend]:

                        # writin the ID and its friends ID
                        file_object.write(str(key + " " +  friend + "\n"))
                         
                # if the friend ID is not in the user ID dictionary key's       
                else:
                    file_object.write(str(key + " " +  friend + "\n")) 


if __name__ == "__main__":
    main()