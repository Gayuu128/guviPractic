from datetime import datetime

currentDate = datetime.now()

# Lambda function to extract year, month, and day
extractDate = lambda d: (d.year, d.month, d.day)

print("Year, Month, Day:", extractDate(currentDate))

