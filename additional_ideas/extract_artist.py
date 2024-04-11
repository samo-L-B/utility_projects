Here's the Python code to achieve what you described:
Python

import csv

def extract_artist(row):
  """
  This function takes a row from a CSV file and extracts the artist name
  from the second part after the "-" symbol.

  Args:
      row: A list containing the values from a single row in the CSV file.

  Returns:
      A list with the original row and the extracted artist name added as the last element.
  """
  if len(row) > 0 and "-" in row[0]:  # Check if data exists and has "-"
    parts = row[0].split("-", 2)  # Split at most twice by "-"
    if len(parts) > 1:  # Check if there are at least 2 parts
      artist = parts[2].strip()  # Get the third part and remove leading/trailing spaces
      row.append(artist)
  return row

def main():
  """
  This function reads a CSV file, processes each row with the extract_artist function,
  and writes the results to a new CSV file.
  """
  input_file = "your_data.csv"  # Replace with your actual CSV file name
  output_file = "processed_data.csv"  # Replace with your desired output file name

  with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer.writerow(next(reader) + ["Artist"])  # Write header with "Artist" added
    for row in reader:
      writer.writerow(extract_artist(row.copy()))  # Process and write each row

if __name__ == "__main__":
  main()
