# Q1. Count how many ERROR logs are present.


error_count = 0

with open("app.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
            
print("Total ERROR logs:", error_count)
            
            
