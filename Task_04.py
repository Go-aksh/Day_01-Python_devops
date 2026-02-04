#Q4.Search logs using a keyword provided by the user. 

keyword = input("Enter keyword to search: ")

with open("app.log", "r") as file:
    for line in file:
        if keyword.lower() in line.lower():
            print(line.strip())
                                        
