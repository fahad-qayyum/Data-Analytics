import csv
import sys
import argparse
import numpy as np;
import matplotlib.pyplot as plt;


# to check whether the key exists in the dictionary
def checkKey(dict, key): 
      
    if key in dict.keys(): 
        return True 
    else: 
        return False 

def main():
    file = sys.argv[1]
    city = sys.argv[2]
    dict = {}
    stars = {}
    
    dictList = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['city'] == city):
                
                # if "Restaurants" is a category in the row
                if "Restaurants" in row['categories']:
                    
                    # splitting categories based on ;
                    for cat in row['categories'].split(';'):
                        
                        # if category not in list then add in the list as a dict element
                        if(checkKey(dict, cat)== False):
                            dict[cat] = [row['review_count'], row['stars']]
                            
                        # if category in the list then increase the count of it    
                        else:
                            reviewsCount = str(int(dict[cat][0]) + int(row['review_count']))
                            count = str(int(dict[cat][1]) + 1)
                            dict[cat] = [reviewsCount, count , ]
                
                # if restaurant is not a category in the row
                else:
                    
                    # adding category to the list
                    for cat in row['categories'].split(';'):
                        if (not cat in dictList):
                            dictList.append(cat)

    for cat in dictList:
        if cat in dict:
            del dict[cat]
    del dict['Restaurants']        
    #list(reversed(sorted(dictList.keys())))
    for i in sorted(dict, key=dict.get, reverse=True):
        print (i, dict[i])                 
    # for val in dict:
    #     print (val + ": " + str(dict[val]))

    # plot the results
    listObjects = []
    y = []
    tup = tuple(listObjects)
    x = np.arange(len(tub))

    fig, ax = plt.subplots()
    plt.bar(x, y, align='center', alpha=0.5)
    plt.xticks(y, tup)
    plt.xlabel('String')
    plt.ylabel('String')
    plt.title('String')
    fig.autofmt_xdate()

    plt.plot(indices, hinge_loss) 
    plt.show()

main()
