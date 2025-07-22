#This project reads data from NEM13 xml file and parses it to extract specific information.
# The extracted data is then validated using the pyinputplus library.
#Also uses regex to validate message IDs
#some of the extracted data is written to a csv file.

import xml.etree.ElementTree as ET
import re
import csv
import pyinputplus as pyip  
import os

relative_path = "resources"
file_name = pyip.inputFilename("Enter your filename:")
# enter filename as NEM13.xml
print(f"You have entered: {file_name}")
xml_file_path = os.path.join(relative_path, file_name)
# Check if the file exists
if not os.path.isfile(xml_file_path):
    print(f"File {xml_file_path} does not exist.")
else:
    print(f"File {xml_file_path} exists.")

#xml_file_path = "resources/NEM13.xml"
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Extracting data from XML
mdp = root.find('Header/From')
print("MDP From : ", mdp.text)
messageIdRegex = re.compile(r'[A-Z]{6,8}-[A-Z]{3}-\d{12}')
message_id = root.find('Header/MessageID')
result = messageIdRegex.search(message_id.text)
if result:
    print("MDP from MessageId : ", result.group()[0:8])
else:
    print("No message ID found.")
assert mdp.text == result.group()[0:8], "MDP From does not match MessageId MDP"

passFile = open("resources/result_nem13.csv", "w")
passFile.write("MDP,MessageID\n")
passFile.write(f"{mdp.text},{message_id.text}\n")