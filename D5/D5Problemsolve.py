def parse_rules(file_path):
    """
    Parses the page ordering rules from a file.
    """
    with open(file_path, 'r') as file:
        rules = [tuple(map(int, line.strip().split("|"))) for line in file]
    return rules


def parse_updates(file_path):
    """
    Parses the updates from a file.
    """
    with open(file_path, 'r') as file:
        updates = [list(map(int, line.strip().split(","))) for line in file]
    return updates


def is_update_correct(rules, update):
    """
    Checks if an update is correctly ordered based on the given rules.
    """
    # Create a dictionary for the indices of each page in the update
    index_map = {page: i for i, page in enumerate(update)}
    
    # Check all applicable rules for this update
    for x, y in rules:
        if x in index_map and y in index_map:  
            print(index_map[x],",",index_map[y])
            if index_map[x] >= index_map[y]:  # x must appear before y
                return False
    return True


def reorder_update(rules, update):
    """
    Reorders an update based on the given rules.
    """
    
    graph = {page: [] for page in update}
    for x, y in rules:
        if x in graph and y in graph:
            graph[x].append(y)

    # Perform topological sort to find the correct order
    visited = {}
    stack = []

    def dfs(node):
        if node in visited:
            return visited[node]  
        visited[node] = False  #
        for neighbor in graph[node]:
            if not dfs(neighbor):  # If a cycle is detected, the order is invalid
                return False
        visited[node] = True  
        stack.append(node)  
        return True

    for node in graph:
        if node not in visited:
            if not dfs(node):
                raise ValueError("Cycle detected in ordering rules") 
    return stack[::-1]  

def find_middle_page(update):
    """
    Finds the middle page of an update.
    """
    mid = len(update) // 2
    return update[mid]


def process_updates(rules_file, updates_file):
    """
    Processes the updates to handles/ executes all other functions of the problem.
    """
    rules = parse_rules(rules_file)
    updates = parse_updates(updates_file)

    sum_correct = 0
    sum_corrected = 0

    for update in updates:
        if is_update_correct(rules, update):
            sum_correct += find_middle_page(update)
        else: 
            corrected_update = reorder_update(rules, update)
            sum_corrected += find_middle_page(corrected_update)

    return sum_correct, sum_corrected

rules_file = "./D5/pagenumber.txt"  
updates_file = "./D5/print_sequence.txt"  

part_one, part_two = process_updates(rules_file, updates_file)

print("P1",part_one)
print("P2",part_two)
