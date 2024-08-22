import datetime

# NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
# today_date = datetime.datetime.today().date()
# today_month = datetime.datetime.today().month
# print(today_month)
#
# datetime_object = datetime.datetime.strptime(str(today_month), "%m")
# month_name = datetime_object.strftime("%b")
# print(month_name)

NextDay_Date = datetime.datetime.today().date() + datetime.timedelta(days=1)
print(NextDay_Date)
# NextMonth = NextDay_Date.month
NextMonth1 = NextDay_Date.day
#
print(NextMonth1)
#
# datetime_object1 = datetime.datetime.strptime(str(NextMonth), "%m")
# month_name1 = datetime_object1.strftime("%b")
# print(month_name1)
#
# if today_month == NextMonth:
#     print(month_name1)
# elif today_month < NextMonth:
#     print(month_name1)

# full_month_name = datetime_object.strftime("%B")
# print("Full name: ", full_month_name)
