import datetime


num_y=int(input("Enter number of years։"))
num_d=int(input("Enter number of days։"))

current_date=datetime.datetime.today()
num_years=datetime.timedelta(days=num_y*365)
num_days=datetime.timedelta(days=num_d)   
final_date=current_date+num_years+num_days

print("Current date:",current_date)
print("Given years:",num_y)
print("Given days:",num_d)
print("Final date:",final_date)



