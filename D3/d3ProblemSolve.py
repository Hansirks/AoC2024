import re

def compute_mul_sum_from_file(file_path):
    """
    Reads corrupted memory data from a file and computes the sum of results from valid mul(X,Y) instructions.
    """
    
    with open(file_path, 'r') as file:
        memory_input = file.read()
    
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    
    matches = re.findall(pattern, memory_input)
    
    
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum


file_path = "./datad3.txt"


result = compute_mul_sum_from_file(file_path)
print(result)





#PART2

def compute_conditional_mul_sum_from_file(file_path):
    """
    Reads corrupted memory data from a file and computes the sum of results from enabled mul(X,Y) instructions.
    """
    
    with open(file_path, 'r') as file:
        memory_input = file.read()
    
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    
    instructions = re.findall(pattern, memory_input)
    
    total_sum = 0
    enabled = True  # Multiplications are enabled by default
    
    for instr, x, y in instructions:
        if instr == "do()":
            enabled = True 
        elif instr == "don't()":
            enabled = False  # Disable multiplications
        elif "mul" in instr and enabled:
            total_sum += int(x) * int(y)
    
    return total_sum

file_path = "./datad3.txt"
result = compute_conditional_mul_sum_from_file(file_path)
print(result)
