import math

# 1. Nhập GPA và xếp loại học lực
gpa = float(input("Nhập GPA: "))

if gpa < 0 or gpa > 10:
    print("GPA không hợp lệ!")
elif gpa < 3.5:
    print("Học lực: Kém")
elif gpa < 5.0:
    print("Học lực: Yếu")
elif gpa < 7.0:
    print("Học lực: Trung bình")
elif gpa < 8.0:
    print("Học lực: Khá")
elif gpa < 9.0:
    print("Học lực: Giỏi")
else:
    print("Học lực: Xuất sắc")

# 2. Giải phương trình bậc nhất: ax + b = 0
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("Nghiệm x =", x)

# 3. Giải phương trình bậc hai: ax² + bx + c = 0

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    # Chuyển về phương trình bậc nhất
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Nghiệm x =", x)
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)