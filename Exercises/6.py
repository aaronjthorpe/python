#Exercise 6
#6.py
#Calculate employee pay

hourly_wage = float(input("What is the hourly wage? "))  # Can convert immediately on providing input
regular_hours = float(input("How many regular hours worked? "))
overtime_hours = float(input("How many overtime hours worked? "))

#Option 1
regular_pay = regular_hours * hourly_wage
overtime_pay = overtime_hours * hourly_wage * 1.5
total_weekly_pay = regular_pay + overtime_pay
print(f"\nEmployee Pay Summary:\
      \n---------------------\
      \n\
      \nHourly Wage: {hourly_wage}\
      \nRegular Hours: {regular_hours}\
      \nOvertime Hours: {overtime_hours}\
      \n\
      \nRegular Pay: ${regular_pay:.2f}\
      \nOvertime Pay: ${overtime_pay:.2f}\
      \n\
      \nTotal weekly Pay: ${total_weekly_pay:.2f}\
      \n---------------------")

#Option 2, Pay only, inline calculation.
print((regular_hours * hourly_wage) + (overtime_hours * hourly_wage * 1.5))
