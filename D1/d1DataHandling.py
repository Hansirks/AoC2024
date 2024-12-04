import csv

def convert_to_csv(input_file, output_file):
    left_list = []
    right_list = []
    with open(input_file, 'r') as file:
        for line in file:
            # Split each line by spaces to get the two numbers
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Left List', 'Right List'])  
        for left, right in zip(left_list, right_list):
            writer.writerow([left, right])


input_file = './data.txt'  
output_file = './d1_data_output.csv'  

convert_to_csv(input_file, output_file)