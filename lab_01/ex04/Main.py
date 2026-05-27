from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while (1 == 1): # or while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU**************************")
    print("**  1. Them sinh vien.                               **")
    print("**  2. Cap nhat thong tin sinh vien boi ID.          **")
    print("**  3. Xoa sinh vien boi ID.                         **")
    print("**  4. Tim kiem sinh vien theo ten.                  **")
    print("**  5. Sap xep sinh vien theo diem trung binh (GPA). **") # GPA mentioned here
    print("**  6. Sap xep sinh vien theo ten chuyen nganh.      **") # Text says "chuyen nganh" but code calls sortByName
    print("**  7. Hien thi danh sach sinh vien.                 **")
    print("**  0. Thoat                                         **")
    print("*****************************************************")

    key = int(input("Nhap tuy chon: "))

    if (key == 1):
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        if (qlsv.soluongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien.")
            print("\nNhap ID: ") # Prompt before input
            ID = int(input()) # Assuming ID is an integer
            qlsv.updateSinhVien(ID)
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 3):
        if (qlsv.soluongSinhVien() > 0):
            print("\n3. Xoa sinh vien.")
            print("\nNhap ID: ") # Prompt before input
            ID = int(input()) # Assuming ID is an integer
            if (qlsv.deleteById(ID)):
                print(f"\nSinh vien co id = {ID} da bi xoa.") # Using f-string for clarity
            else:
                print(f"\nSinh vien co id = {ID} khong ton tai.") # Using f-string
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 4):
        if (qlsv.soluongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem: ") # Prompt before input
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 5):
        if (qlsv.soluongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB() # This sorts the internal list
            qlsv.showSinhVien(qlsv.getListSinhVien()) # Then displays it
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 6): # Menu says "theo ten chuyen nganh", but code calls sortByName
        if (qlsv.soluongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten.") # Corrected print to match sortByName
            qlsv.sortByName() # This sorts the internal list by name
            qlsv.showSinhVien(qlsv.getListSinhVien()) # Then displays it
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 7):
        if (qlsv.soluongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")