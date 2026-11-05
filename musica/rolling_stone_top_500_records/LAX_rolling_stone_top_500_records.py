import csv
import random
import sys
import os

def choose_random_record(csv_filename):
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        records = list(reader)
        random_record = random.choice(records)
        return random_record

def main():
    csv_filename = 'rolling_stone_top_500_albums_2020.csv'
    random_record = choose_random_record(csv_filename)

    print(f"\n idiota - here's your daily random record of the list with the top 500 greatest records of all time (published by rolling stone) you fucking dipshit: \n \n")
    print("RECORD:", random_record['Album'])
    print("Artists:", random_record['Artist'])
    print("Cover:", random_record['Cover'])
    print("Info:", random_record['Info'])
    print("Rank:", random_record['Rank'])
    print("\nDescription:")
    print(random_record['Description'])

    print("\n enjoy ur day alegria:")

if __name__ == "__main__":
    print("\n oie dipshit - hope we find a great record to match ur mood fuckhead!\n")
    main()
