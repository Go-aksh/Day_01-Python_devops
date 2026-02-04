# Q2. Display only ERROR log lines. 

with open("app.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())  
            

