import argparse
import csv;
import math;
import sys;
# from nltk.tokenize import word_tokenize
from string import punctuation;
from operator import itemgetter;
import re;


def numOfBus(file, city):
    # Return an int with number of busniesses in a city
    count = 0
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['city'] == city):
                count = count + 1
    return count


def avgNumberStars(file, city):
    sum = 0
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['city'] == city):
                sum = sum + float(row['stars'])
    return sum


def get_dict(file):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # rows = csv.DictReader(csvfile)
        next(reader)
        d = {}
        for row in reader:
            if row[0] not in d:
                d[row[0]] = []
            d[row[0]].append(row[1:])
    return d


def main():
    file = sys.argv[1]
    city = sys.argv[2]
    dict = get_dict(file)

    numofBusinesses = numOfBus(file, city)
    avgStars = avgNumberStars(file, city) / numofBusinesses
    print(numofBusinesses, avgStars)


if __name__ == "__main__":
    main()