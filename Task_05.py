#Q5. Raise an alert if ERROR count exceeds a threshold. 

threshold = 2
error_count = 0

with open("app.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count +=1

if error_count > threshold:
    print("🚨 ALERT! ERROR count exceeded:", error_count)
else:
    print("✅ System stable. ERROR count:", error_count)