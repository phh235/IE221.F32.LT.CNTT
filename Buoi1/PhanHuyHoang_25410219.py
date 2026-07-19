# Phan Huy Hoàng - 25410219
import random as rd

# 1. Viết chương trình nhập vào 4 số nguyên a, b, c, d. Tính trung bình cộng
# của 4 số trên và in kết quả ra màn hình.
def bai1():
    print("--- Bai 1: Trung binh cong 4 so ---")
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    c = int(input("Nhap c: "))
    d = int(input("Nhap d: "))
    trung_binh = (a + b + c + d) / 4
    print(f"Trung binh cong = {trung_binh}")

# 2. Viết chương trình nhập vào 2 số nguyên a, b. Tính tổng, hiệu, tích, thương, chia lấy dư, chia lấy nguyên
# của 2 số trên và in kết quả ra màn hình. Kết quả phép chia làm tròn 2, 3 chữ số sau dấu chấm
# (ví dụ kết quả 3.333333 thì làm tròn 3.333).
def bai2():
    print("--- Bai 2: Cac phep toan tren 2 so ---")
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    print(f"Tong: {a + b}")
    print(f"Hieu: {a - b}")
    print(f"Tich: {a * b}")
    print(f"Thuong: {round(a / b, 3)}")
    print(f"Chia lay du: {a % b}")
    print(f"Chia lay nguyen: {a // b}")

# 3. Viết chương trình cho phép nhập vào số nguyên dương N có 2 chữ số.
# Xuất ra màn hình tổng các chữ số của N. Ví dụ: Nhập N=48, kết quả xuất ra màn hình là 4 + 8 = 12
def bai3():
    print("--- Bai 3: Tong cac chu so cua N (2 chu so) ---")
    n = int(input("Nhap N: "))
    chuc = n // 10
    don_vi = n % 10
    print(f"{chuc} + {don_vi} = {chuc + don_vi}")

# 4. Viết chương trình cho phép nhập vào giờ, phút và giây
# (ví dụ: 8 39 50). Hãy đổi ra tổng số giây và in kết quả ra màn hình.
def bai4():
    print("--- Bai 4: Doi gio phut giay ra giay ---")
    gio = int(input("Nhap gio: "))
    phut = int(input("Nhap phut: "))
    giay = int(input("Nhap giay: "))
    tong_giay = gio * 3600 + phut * 60 + giay
    print(f"Tong so giay = {tong_giay}")

# 5. Viết chương trình nhập vào năm sinh, in ra tuổi.
# Ví dụ: nhập 1988 thì in ra: Ban sinh nam 1988 vay ban 38 tuoi.
def bai5():
    print("--- Bai 5: Tinh tuoi ---")
    nam_sinh = int(input("Nhap nam sinh: "))
    nam_hien_tai = 2026
    tuoi = nam_hien_tai - nam_sinh
    print(f"Ban sinh nam {nam_sinh} vay ban {tuoi} tuoi.")

# 6. Nhập vào 3 số a, b, c.
# Sau đó in ra phương trình bậc 2 dạng:
# aX^2 + bX + c = 0.
# Ví dụ: a = 2, b = 5, c = 4
# Kết quả: 2X^2 + 5X + 4 = 0.
def bai6():
    print("--- Bai 6: In phuong trinh bac 2 ---")
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    c = int(input("Nhap c: "))
    print(f"{a}X^2 + {b}X + {c} = 0")

# 7. Viết chương trình in ra menu lựa chọn sau:
# ============ MENU ============
# 1. Hu tieu
# 2. Chao long
# 3. Banh canh
# 4. Bun rieu
# 5. Pho bo
# ==============================
# Moi nhap lua chon:
# ==============================
def bai7():
    print("--- Bai 7: Menu lua chon ---")
    print("============ MENU ============")
    print("1. Hu tieu")
    print("2. Chao long")
    print("3. Banh canh")
    print("4. Bun rieu")
    print("5. Pho bo")
    print("==============================")
    print("Moi nhap lua chon: ")
    print("==============================")

# 8. Nhập bán kính của đường tròn.
# Tính và in ra chu vi và diện tích hình tròn.
def bai8():
    print("--- Bai 8: Chu vi va dien tich hinh tron ---")
    r = float(input("Nhap ban kinh: "))
    pi = 3.14
    chu_vi = 2 * pi * r
    dien_tich = pi * r * r
    print(f"Chu vi = {chu_vi}")
    print(f"Dien tich = {dien_tich}")

# 9. Viết chương trình tính chỉ số BMI.
# Công thức: BMI = Can_nang (kg) / (Chieu_cao (m) ^ 2)
def bai9():
    print("--- Bai 9: Tinh BMI ---")
    can_nang = float(input("Nhap can nang (kg): "))
    chieu_cao = float(input("Nhap chieu cao (m): "))
    bmi = can_nang / (chieu_cao ** 2)
    print(f"BMI = {round(bmi, 2)}")

# 10. Nhập vào số xe gồm 5 chữ số. Cho biết số xe có mấy nút.
def bai10():
    print("--- Bai 10: Tinh so nut cua bien so xe ---")
    so_xe = input("Nhap so xe (5 chu so): ")
    tong = 0
    for chu_so in so_xe:
        tong += int(chu_so)
    so_nut = tong % 10
    print(f"So xe co {so_nut} nut")

# 11. Cho nhập vào một ký tự chữ thường. In ra ký tự chữ hoa tương ứng.
def bai11():
    print("--- Bai 11: Doi ky tu thuong sang hoa ---")
    ky_tu = input("Nhap 1 ky tu chu thuong: ")
    print(f"Ky tu chu hoa tuong ung: {ky_tu.upper()}")

# 12. Viết chương trình xuất ra số ngẫu nhiên (nguyên và thực)
# theo các khoảng sau:
# 0 đến 100
# 50 đến 99
# -39 đến 79
# -79 đến -39
def bai12():
    print("--- Bai 12: Xuat so ngau nhien ---")
    print("So nguyen tu 0 den 100:", rd.randint(0, 100))
    print("So nguyen tu 50 den 99:", rd.randint(50, 99))
    print("So nguyen tu -39 den 79:", rd.randint(-39, 79))
    print("So nguyen tu -79 den -39:", rd.randint(-79, -39))
    print("So thuc tu 0 den 100:", round(rd.uniform(0, 100), 2))
    print("So thuc tu 50 den 99:", round(rd.uniform(50, 99), 2))
    print("So thuc tu -39 den 79:", round(rd.uniform(-39, 79), 2))
    print("So thuc tu -79 den -39:", round(rd.uniform(-79, -39), 2))


def main():
    bai_tap = {
        "1": bai1,
        "2": bai2,
        "3": bai3,
        "4": bai4,
        "5": bai5,
        "6": bai6,
        "7": bai7,
        "8": bai8,
        "9": bai9,
        "10": bai10,
        "11": bai11,
        "12": bai12,
    }

    while True:
        print("\n===================== MENU =====================")
        print("1. Trung binh cong 4 so")
        print("2. Cac phep toan tren 2 so")
        print("3. Tong cac chu so cua N")
        print("4. Doi gio phut giay ra giay")
        print("5. Tinh tuoi")
        print("6. In phuong trinh bac 2")
        print("7. In menu mon an")
        print("8. Chu vi va dien tich hinh tron")
        print("9. Tinh BMI")
        print("10. Tinh so nut cua bien so xe")
        print("11. Doi ky tu thuong sang hoa")
        print("12. Xuat so ngau nhien")
        print("0. Thoat")
        print("===============================================")

        lua_chon = input("Moi nhap lua chon: ")

        if lua_chon == "0":
            print("Tam biet!")
            break
        elif lua_chon in bai_tap:
            print()
            bai_tap[lua_chon]()
        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()
