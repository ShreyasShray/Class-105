import csv
import math

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
# print(data)

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean

# squaring and getting the values

squarList = []

for number in data:
    a = int(number) - mean(data)
    a = a**2
    squarList.append(a)

# get the sum of all the elements from the squared list

sum = 0

for i in squarList:
    sum = sum + i

# Dividing the sum by total values

result = sum/(len(data) - 1)

standardDeviation = math.sqrt(result)

print(standardDeviation)