from QuanLySinhVien import QuanLySinhVien

glsv = QuanLySinhVien()

while (1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("************************MENU************************")
    print("**  1. Them sinh vien.")
    print("**  2. Cap nhat thong tin sinh vien boi ID.")
    print("**  3. Xoa sinh vien boi ID.")
    print("**  4. Tim kiem sinh vien theo ten.")
    print("**  5. Sap xep sinh vien theo diem trung binh.")
    print("**  6. Sap xep sinh vien theo ten chuyen nganh.")
    print("**  7. Hien thi danh sach sinh vien.")
    print("**  0. Thoat")
    print("****************************************************")
    
    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien.")
        glsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    
    elif (key == 2):
        if (glsv.soluongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien.")
            ID = int(input("Nhap ID: "))
            glsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh vien trong!")
    
    elif (key == 3):
        if (glsv.s1oluongSinhVien() > 0):
            print("\n3. Xoa sinh vien.")
            ID = int(input("Nhap ID: "))
            if (glsv.deleteById(ID)):
                print(f"\nSinh vien co ID = {ID} da bi xoa.")
            else:
                print(f"\nSinh vien co ID = {ID} khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")
    
    elif (key == 4):
        if (glsv.soluongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("Nhap ten de tim kiem: ")
            searchResult = glsv.findByName(name)
            glsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")
    
    elif (key == 5):
        if (glsv.soluongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            glsv.sortByDiemTB()
            glsv.showSinhVien(glsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    
    elif (key == 6):
        if (glsv.soluongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            glsv.sortByName()
            glsv.showSinhVien(glsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    
    elif (key == 7):
        if (glsv.soluongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            glsv.showSinhVien(glsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")
