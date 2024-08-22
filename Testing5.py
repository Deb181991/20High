# import json

# file = open(".//TestData//screen.json", "r")
# finaldata = json.load(file)
# print(finaldata)
# print(finaldata['Numeric'])
# a = finaldata['Numeric']
# print(a)
# b = int(a) + 1
# print(b)
# data = {}
# data['Numeric'] = b
# j = json.dumps(data)
# with open(".//TestData//screen.json", "w") as f:
#     f.write(j)
import json


# function to add to JSON
def write_json(new_data, filename='.//TestData//screen.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=1)

    # python object to be appended


v = {"emp_name": "cavi",
     "email": "deb@geeksforgeeks.org"
     }
y = v

write_json(y)
