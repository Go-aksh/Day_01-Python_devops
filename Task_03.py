# Count INFO, WARN, and ERROR logs separately

error_count = 0
info_count = 0
warn_count = 0

with open("app.log", "r") as file:
    for line in file:
        if "INFO" in line:
            info_count += 1
        elif "WARN" in line:
            warn_count += 1
        elif "ERROR" in line:
            error_count += 1

print("Error:", error_count)
print("Info:", info_count)
print("Warn:", warn_count)