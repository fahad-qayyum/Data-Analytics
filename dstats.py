import csv
import sys
import argparse

# numOfBus: the number of businesses in the city
def numOfBus(file, city):
    # Return an int with number of busniesses in a city
    count = 0
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['city'] == city):
                count = count + 1
    return count

# avgStars: the average number of stars of a business in the city
def avgStars(file, city):
    sum = 0
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['city'] == city):
                sum = sum + float(row['stars'])
    return sum

# numOfRestaurants: the number of restaurants in the city
def numOfRestaurants(file, city):
    count = 0
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['city'] == city):
                if "Restaurants" in row['categories']:
                    count+=1
    return count
       
# avgStarsRestaurants: the average number of stars of restaurants in the city                    
def avgStarsRestaurants(file, city):
    sum = 0
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['city'] == city):
                if "Restaurants" in row['categories']:
                    sum = sum + float(row['stars'])
    return sum                
 
# avgNumOfReviews: the average number of reviews for all businesses in the city                
def avgNumOfReviews(file, city):
    sum = 0
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['city'] == city):
                sum = sum + int(row['review_count'])
    return sum                

# avgNumOfReviewsBus: the average number of reviews for restaurants in the city
def avgNumOfReviewsBus(file, city):
    sum = 0
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['city'] == city):
                if "Restaurants" in row['categories']:
                    sum = sum + int(row['review_count'])
    return sum  

def main():
    file = sys.argv[1]
    city = sys.argv[2]
    resCount = numOfRestaurants(file, city)
    busCount = numOfBus(file,city)
    avgBusStars =  avgStars(file, city)/busCount
    avgResStars =  avgStarsRestaurants(file, city)/resCount
    avgBusReviews = avgNumOfReviews(file,city)/busCount
    avgResReviews = avgNumOfReviewsBus(file, city)/resCount
    
    print("The number of Restaurants in " , city , " is: " , resCount)
    print("The number of Business in ", city, " is: ", busCount)
    print("The average number of stars of Business in ", city, " is: ", avgBusStars)
    print("The average number of stars of Restaurants in ", city, " is: ", avgResStars)
    print("The average number of reviews for all business in ", city, " is: ", avgBusReviews)
    print("The average number of reviews for all restaurants in ", city, " is: ", avgResReviews)

main()