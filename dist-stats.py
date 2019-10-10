import csv
import sys
import argparse
import matplotlib.pyplot as plt

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
    sum = 0.0
    avg = 0.0
    
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
                        if(checkKey(dict, cat) == False):
                            dict[cat] = [float(row['review_count']), [float(row['stars'])] , 1]
                            
                        # if category in the list then increase the count of it    
                        elif(checkKey(dict, cat) == True): 
                            dict[cat][0] = float(dict[cat][0]) + float(row['review_count'])
                            dict[cat][1].append(float(row['stars']))
                            dict[cat][2] = float(dict[cat][2]) + 1

                
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


    sortedDict = {}

    for item in sorted(dict, key=dict.get, reverse=True):
        sum = 0.0
        for element in dict[item][1]:
            sum = sum + element
 
        avg = sum/dict[item][2]
        sortedDict[item] = int(dict[item][0])           
        # print (item, ":", int(dict[item][0]) , ":%.2f" % avg) 

    




    x = list(sortedDict)[:10]
    y = list(sortedDict.values())[:10]

    # tup = tuple(listObjects)
    # x = np.arange(len(tub))
    fig, ax = plt.subplots()
    plt.bar(x, y, align='center', alpha=0.5)
    #plt.xticks(y, x)
    plt.xlabel('Category')
    plt.ylabel('Reviews')
    plt.title('Top 10 Restaurants Category by reviews')
    #fig.autofmt_xdate()
    #plt.plot(x, y) 
    plt.show()
   

if __name__ == "__main__":
    main()