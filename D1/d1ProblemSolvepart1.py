import csv

def calculate_total_distance_from_csv(input_file):
    left_list = []
    right_list = []
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            
            left_list.append(int(row[0]))
            right_list.append(int(row[1]))
    left_list.sort()
    right_list.sort()

    # Calculate the total distance by summing up the absolute differences
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    
    return total_distance


input_file = './d1_data_output.csv'  
result = calculate_total_distance_from_csv(input_file)
print(result)
