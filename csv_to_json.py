import csv
import json

def convert_csv_to_json(csv_file_path , json_file_path):
    try:
        # open with csv file
        with open(csv_file_path , mode='r' , newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file) #Automatically maps header to values
            data=list(reader) #convert to list of dictionaries

        # write to a json file
        with open (json_file_path , mode='w' , encoding='utf-8') as json_file:
            json.dump(data , json_file , indent = 4)

        print(f"successfully converted '{csv_file_path}' to '{json_file_path}'")

    except Exception as e:
        print(f"Error: {e}")

# call the Function
convert_csv_to_json('people.csv','people.json')
