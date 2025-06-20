student_list = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())

        student_list.append([name, score])

def myFunc(grade):
    return grade[1]

student_list.sort(key=myFunc)

students = []

second_highest = student_list[0][1]

for li in student_list:
    if second_highest < li[1]:
        second_highest = li[1]
        break

for li in student_list:
    if li[1] == second_highest:
        students.append(li[0])

students.sort()

for i in students:
    print(i)