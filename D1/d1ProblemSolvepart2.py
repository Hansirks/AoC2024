import csv
from collections import Counter

def calculate_similarity_score_from_csv(input_file):
    left_list = []
    right_list = []
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            
            left_list.append(int(row[0]))
            right_list.append(int(row[1]))
    
   
    right_count = Counter(right_list)

    # Calculate the total similarity score
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_count[number]

    return similarity_score

input_file = './d1_data_output.csv'  
result = calculate_similarity_score_from_csv(input_file)
print(result)
