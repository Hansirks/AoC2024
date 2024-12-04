import csv


input_file = './datad2.txt'  
output_file = './d2input.csv'  
with open(input_file, 'r') as file:
    lines = file.readlines()

csv_data = [line.strip().split() for line in lines]
csv_data = [[int(num) for num in row] for row in csv_data]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

