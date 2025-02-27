sogiolam = float(input("Nhap so gio lam moi tuan: "))
luonggio = float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
giotieuchuan = 44 #so gio lam tieu chuan moi tuan
giovuotchuan = max(0,sogiolam-giotieuchuan)
thuc_linh = giotieuchuan*luonggio+giovuotchuan*luonggio*1.5 #tinh tong thu nhap
print(f"tien luong cua nhan vien: {thuc_linh}")
