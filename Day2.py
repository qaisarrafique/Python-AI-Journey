# my_tuple = (10, 20, 30, 40)
# print(my_tuple)
# print(my_tuple[0])
# print(my_tuple[2])


# student = ("Qaisar", 21, "Vehari", 99.06)
# print(student)
# print(len(student))

# student_list = list(student)
# student_list[1] = 22
# print(student_list)

# my_set = {10, 20, 30, 40, 40, 20}
# print(my_set)
# my_set.add(50)
# print(my_set)

# my_set.remove(20)
# print(my_set)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.union(set2))
# print(set1.intersection(set2))


# age = 18

# if age >= 18:
#     print("Eligible for voting")
# else:
#     print("Not Eligible for voting")


# marks = 85

# if marks >= 80:
#     print("Grade: A")
#     if marks >= 90:
#         print("Excellent")
#     else:
#         print("Very Good")
# else:
#     print("Work Hard")


# temperature = 35

# if temperature > 40:
#     print("Hot Day")
# elif temperature > 25:
#     print("Normal Day")
# else:
#     print("Cold Day")


# a = 10 
# b = 20 
# if a > 5 and b > 15:
#     print("Both conditions True")

for i in range(5):
    print("Hello Python")

for i in range(1, 6):
    print(i)

subjects = ["English", "Math", "Physics"]
for sub in subjects:
    print(sub)


count = 1
while count <= 5:
    print("count is:", count)
    count += 1

for i in range(1, 6):
    if i == 3:
        continue
    if i == 3:
        break
    print(i)