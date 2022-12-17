if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    array=(student_marks[query_name])
    sum=0.00
    for i in array:
        sum=sum+i
    avg=sum/3
    avg="{:.2f}".format(avg)
    print(avg)
