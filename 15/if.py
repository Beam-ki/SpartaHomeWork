def get_grade(score):
    if  91 <=score <= 100:
        return print("A")
    elif  81 <=score <= 90:
        return print("B")
    elif  71 <=score <= 80:
        return print("C")
    else:
        return print("F")

score = int(input())
grade = get_grade(score)
print(grade) # A ~ F