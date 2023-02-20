n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    print(name, *line)
print(student_marks)
query_name = input()
for key in student_marks:
    if key == query_name:
        value = student_marks[query_name]
        s = sum(value)/3
        print(s)
        tw_decimal = '{:.2f}'.format(s)
        print('{:.2f}'.format(s))


s = 80.0
two_decimal = '{:.2f}'.format(s)
print(two_decimal)