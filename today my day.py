import datetime

# Today
a = datetime.datetime.now()
print("Today is", a)

# Birthday
b = datetime.datetime(2021, 10, 12)
print("My birthday is", b)

# Is Today my day7
print("Is my birthday today?")
if a == 2021_10_12_19_00:
    print("This is your day")
else:
    print("Today is not my day")
# How many days are left until my birthday
c = (b-a)
print("Left days", c)