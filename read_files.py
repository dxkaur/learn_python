inputFile = open("inputFile.txt", "r")
i = 0
passFile = open("passFile.txt", "w")
failFile = open("failFile.txt", "w")
for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
        i = i+1
    else:
        failFile.write(line)
print(f"Number of people passed = {i}")
#print(inputFile.read())
inputFile.close
passFile.close
failFile.close