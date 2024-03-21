#1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

average_grade = sum(grades)/len(grades)
print(average_grade)

for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"
        print("updated grades:", grades)

#2
        
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
both = set(submitted).intersection(attended)
print("Students who both submitted and attended:", list(both))

if submitted == attended:
    print("The lists are identical")
else:
    print("The lists are not identical")

attended = list(set(submitted).intersection(attended))
print("Updated attended list:", attended)

#3

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temp = temperatures[7:14]
print(second_week_temp)

above_100_temperatures = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100:", above_100_temperatures)

temperatures.reverse()
extracted_temperatures = temperatures[4:10]
print("Temperatures from the 5th to the 10th day of the reversed list:", extracted_temperatures)

#4

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

filtered_student = []
for i in range(len(students)):
    if grades[i] <= 80:
        filtered_student.append((students[i], grades[i], activities[i]))
for student in filtered_student:
    print(student)

students_approved = []
for i in range(len(students)):
    if grades[i] >= 80:
        students_approved.append(students[i],)
for student in students_approved:
    print(students_approved)

