import csv

def is_safe(report):
    increasing = decreasing = True

    for i in range(1, len(report)):
        diff = abs(report[i] - report[i-1])
        if diff < 1 or diff > 3:
            return False
        if report[i] < report[i-1]:
            increasing = False
        elif report[i] > report[i-1]:
            decreasing = False

    return increasing or decreasing

def count_safe_reports(filename):
    safe_count = 0
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            levels = list(map(int, row))
            
            # Check if the report is safe
            if is_safe(levels):
                safe_count += 1
    
    return safe_count

filename = './d2input.csv'
safe_reports = count_safe_reports(filename)
print(safe_reports)




#PART 2

def corrected_is_safe(report):
    """Check if a report is safe with stricter monotonicity rules."""
    if len(report) < 2:
        return True  
    diff = report[1] - report[0]
    if diff > 0:
        direction = "increasing"
    elif diff < 0:
        direction = "decreasing"
    else:
        return False  

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if diff == 0 or abs(diff) > 3:
            return False  
        if direction == "increasing" and diff < 0:
            return False  
        if direction == "decreasing" and diff > 0:
            return False

    return True

def count_safe_reports_with_dampener(filename):
    """Count safe reports including those made safe by the Problem Dampener."""
    safe_count = 0

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            report = list(map(int, row))
            
            # Case 1: Report is already safe
            if corrected_is_safe(report):
                safe_count += 1
            # Case 2: Use the Problem Dampener (remove one level and check safety)
            else:
                for i in range(len(report)):
                    modified_report = report[:i] + report[i + 1:]
                    if corrected_is_safe(modified_report):
                        safe_count += 1
                        break  

    return safe_count

filename = './d2input.csv'
safe_reports = count_safe_reports_with_dampener(filename)
print(safe_reports)





