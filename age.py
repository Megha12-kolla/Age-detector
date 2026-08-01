print("Welcome to your age detector!")

date = int(input("Enter your Date of Birth (DD): "))
month = int(input("Enter your Month of Birth (MM): "))
year = int(input("Enter your Year of Birth (YYYY): "))

now_date = int(input("Enter today's Date (DD): "))
now_month = int(input("Enter today's Month (MM): "))
now_year = int(input("Enter today's Year (YYYY): "))

age_year = now_year - year
age_month = now_month - month
age_date = now_date - date

# Borrow days if needed
if age_date < 0:
    age_date += 30      # Assuming every month has 30 days
    age_month -= 1

# Borrow months if needed
if age_month < 0:
    age_month += 12
    age_year -= 1

print(f"\nYour age is {age_year} years, {age_month} months, and {age_date} days.")