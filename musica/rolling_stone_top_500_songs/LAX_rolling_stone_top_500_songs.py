import csv
import random

def pick_random_song(csv_filename):
  """  This function reads the CSV file and randomly picks a song (Song column value).  """
  songs = []
  with open(csv_filename, 'r', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
      songs.append(row[3])  # Assuming Song is at index 1
  return random.choice(songs)

def main():
  """
  This function calls the pick_random_song function to get a random song and prints it.
  """
  csv_filename = "rolling_stone_500_greatest_song.csv"
  random_song = pick_random_song(csv_filename)
  print(f"\n idiota - here's your daily random song of the list with the top 500 greatest songs of all time (published by rolling stone) you fucking dipshit: \n \n {random_song} \n")

if __name__ == "__main__":
 print("\n oie dipshit - hope we find a great track to match ur mood fuckhead!\n")
 main()
 print("enjoy ur day alegria!")