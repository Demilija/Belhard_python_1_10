"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""
import csv


def max_delta():
    year_percent = 0
    year = {}
    with open('world_population.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimitr=',')
        for row in reader:
            if float(row['ChangePerc']) > year_percent:
                year_percent = float(row['ChangePerc'])
                year[year_percent] = row['Year']
    return year[year_percent]
