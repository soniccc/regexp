# This script takes a history file output text file, removes the spaces and line numbers and then saves
# the output to another file in the filesystem
# re.sub(r"^ *\d* *", "", data, flags=re.MULTILINE) breaks down as follows: -
# re.sub this substitutes
# r" treats the input as raw 
# ^ * begining of the data of spaces until \d* a number of digits the  * a number of spaces
# flags=re.MULTILINE without this then only the first line is acted on





import re

def import_file(filename):
    with open(filename, "r") as file:
        data = file.read()
    return data

def filter(data):
    # screened_data = re.sub(r" *\d*", "", data)
    screened_data = re.sub(r"^ *\d* *", "", data, flags=re.MULTILINE)
    return screened_data

def export_file(data):
    with open("output.txt", "w") as text_file:
        text_file.write(data)

def data_entry():
    filename = input("Please enter the name of the file: ")
    return filename


if __name__ == "__main__":
    filename = data_entry()

    export_file(filter(import_file(filename)))
