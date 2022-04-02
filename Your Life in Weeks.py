Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

age = input("What is your current age?")

years = (int(age))
new_years = (90 - years)
months = (new_years * 12)
weeks = (new_years * 52)
days = (new_years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left ")
