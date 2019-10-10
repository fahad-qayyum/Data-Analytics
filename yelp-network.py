import pandas as pd
import argparse
import csv; import math; import sys; 
#from nltk.tokenize import word_tokenize
from string import punctuation
from operator import itemgetter
import re as re
csv.field_size_limit(sys.maxsize)






def main():
    file = sys.argv[1]
    #city = sys.argv[2]
    df = pd.read_csv(file)
    #print(df.head()) # print the first few rows of the data set
    # print(df) # print the first and last thirty rows of the data set
    # print(df.city) # print the city series(column series) of the data set
    # print(df['city'])  # print the city series(column series) of the data set
    # print(df[['city', 'categories']])  # print the city and categories series(column series) of the data set
    # print(df.shape) # print the dimention of the dataset frame
    # print(df.city.value_counts()) # print the count of a city in a descending order
    # print(df.categories.sort_values()) # print the sorted series in asceding order and return a new series
    # print(df.sort_values(by=['review_count', 'categories'])) sort by review_count and then by categories
    # print(df.city == 'Toronto') # print a series if the city is Toronto
    # print(df[df.city == 'Toronto']) # print a dataframe object only if the city is Toronto
    # print(df[(df.city == 'Toronto') & (df.stars > 4) ]) # print a dataframe object only if the city is Toronto and star is more that four
    # print(df.city.str.contains('Las')) # print a boolean value weather the city contains "Las"
    # print(df[df.city.str.contains('Las')]) # print a dataframe object of city that contains Las
    # print(df.set_index('name').head()) # set the name as the index, the dataset becomes indexable by name
    # print(df.reset_index(inplace=True) # will reset the index back to integer basd index
    # print(df.sort_index()) # will sort the dataset according to the index specified in set_index
    # df.set_index('name', inplace=True); print(df.loc['Lisa']) will locate Lisa in the index label
    # print(list(df.groupby('name'))) list the rows grouped by names
    # for group_key, group_value in df.groupby('city'):
    #     print((group_key))
    #     print((group_value))
    # print(df.groupby('business_id').size()) # print the number of rows each city has in the dataset
    #print(df.loc[df.city == 'Markham'].groupby('city')).agg({'review_count':['min', 'max', 'count']})


    all_friends_dict = {}
    id_name_dict = {}
    friends_dict = {}
    friends_list = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id_name_dict[row['user_id']] = row['name']
            friends_dict[row['name']] = row['friends'].split(';')
        for values in friends_dict.values():
            for v in values:
                if(v in id_name_dict.keys()):
                    print ("\n" + id_name_dict[v].title())

    
    # filename = 'yelp-network.txt'
    # with open(filename, 'w') as file_object:    
    #     file_object.write(str(id_name_dict))    
        


    
    #cities = df.groupby('city').get_group(city)
    #p = re.match(["Food"])
    #bussinessCity = cities.groupby('categories').get_group(p)
    #keys = bussinessCity
    #print(cities)
 

    
if __name__ == "__main__": 
    main()