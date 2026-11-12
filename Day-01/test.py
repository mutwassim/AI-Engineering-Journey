# Print every number from 1 to 10 that is divisible by 3.
for i in range (1,10,3):
    print(i)

# Given nums = [3, 8, 5], build a new list doubled using a loop with append.

nums = [3, 8, 5]
doubled = []
for i in nums:
    doubled.append(i*2)

# Given names = ["Ali", "Sara"] and marks = [85, 78], print Ali 85 and Sara 78 using zip.

names = ["Ali", "Sara"] 
marks = [85, 78]

for name,mark in zip(names,marks):
    print(name,mark)

# Given d = {"x": 1, "y": 2}, print each key and value using .items().
d = {"x": 1, "y": 2}
for k,v in d.items():
    print(k,v)


#calculate_average(80, 90, 70) should return 80.0.

def calculate_average(*args):
    n = len(args)
    if n==0:
        return 0
    s = sum(args)
    avg = s/n
    return avg

#create_profile("Ali", "ali@x.com", 22, city="Lahore", role="Dev") should return a dictionary with all five items.

def create_profile(name, email, age, **kwargs):
    profile = {"name":name,"email":email,"age":age}
    profile.update(kwargs)
    return profile

# Write total_and_avg(*args) that returns both the sum and the average, then call it with a list numbers = 
# [10, 20, 30] using unpacking, and receive the two results into total and avg.

def total_and_avg(*args):
    total = sum(args)
    n = len(args)
    if n==0:
        return 0, 0 
    average = total/n

    return(total,average)
total,avg = total_and_avg(*[10,20,30])

# Given students = [("Ali", 85), ("Sara", 92), ("Hamza", 70)], write one line using sorted and a lambda that 
# sorts the students by marks from highest to lowest. (Hint: sorted has a reverse=True option.)

students = [("Ali", 85), ("Sara", 92), ("Hamza", 70)]

sort = sorted(students, key = lambda n:n[1],reverse=True)