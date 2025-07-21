import csv
import json
import xml.etree.ElementTree as ET

#read data from ~~XML~~ file and parse

xml_file_path = "resources/groceries.xml"
tree = ET.parse(xml_file_path)
root = tree.getroot()

items_over_6 = []

for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = item.find("price").text
    if float(price) > 6.00:
        items_over_6.append(name)
    print(name, price)

print("Items with price higher than 6 : ", items_over_6)
#read data from ~JSON~ file and parse

json_file_path = "resources/groceries.json"

with open(json_file_path, "r") as json_file:
    json_data = json_file.read()

parsed_json_data = json.loads(json_data)
print("apples qunatity: ", parsed_json_data["apples"])

#Read data from ~CSV~ file and parse
csv_file_path = "resources/groceries.csv"

with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    for row in csv_reader:
        row[1] = int(row[1])
        print(row)

#Read data from ~TXT~ file and parse
txt_file_path = "resources/groceries.txt"
with open(txt_file_path, "r") as txt_file:
    groceries_data = txt_file.read()

print(f"data : {groceries_data}")
parsed_data = groceries_data.split(", ")
print(f"parsed_data : {parsed_data}")
print(f"item at index 2: {parsed_data[2]}")