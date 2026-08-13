import math_utils
import math as m
import random as rd
from my_package import geometry, converter
from Game.Sound import play
from Game.Image import open as image_open
import matrix_ops


def main():
    print("BÀI 1 - MODULE TỰ ĐỊNH NGHĨA")
    print("Phép cộng:", math_utils.add(8, 2))
    print("Phép trừ:", math_utils.subtract(8, 2))
    print("Phép nhân:", math_utils.multiply(8, 2))
    print("Phép chia:", math_utils.divide(8, 2))

    print("\nBÀI 2 - MODULE CÓ SẴN")
    print("Căn bậc hai của 25:", m.sqrt(25))

    angle = m.radians(60)
    print("Cos của 60 độ:", m.cos(angle))
    print("Số ngẫu nhiên từ 1 đến 100:", rd.randint(1, 100))

    print("\nBÀI 3 - PACKAGE ĐƠN GIẢN")
    print("Diện tích hình vuông:", geometry.square_area(4))
    print("Chu vi hình vuông:", geometry.square_perimeter(4))
    print("Diện tích hình tròn:", geometry.circle_area(3))
    print("Chu vi hình tròn:", geometry.circle_perimeter(3))
    print("10 cm đổi ra mét:", converter.cm_to_m(10))
    print("2 m đổi ra kilômét:", converter.m_to_km(2))

    print("\nBÀI 4 - PACKAGE NHIỀU CẤP")
    play.play_sound()
    image_open.open_image()

    print("\nBÀI 5 - NUMPY")
    matrix = matrix_ops.create_random_matrix()

    print("Ma trận 3x3 ngẫu nhiên:")
    print(matrix)

    print("Định thức:", matrix_ops.determinant(matrix))

    print("Ma trận nghịch đảo:")
    print(matrix_ops.inverse(matrix))


if __name__ == "__main__":
    main()