def calculate_avg():
    student = {'ram': 20, 'sham': 30, 'kavi': 40}
    total_stu = len(student)
    total_marks = sum(student.values())
    avg = int(total_marks / total_stu)
    print(avg)


calculate_avg()


def multiply(*args):
    m = 1
    for x in args:
        m = m * x
    return m


print(multiply(1, 2, 3))
