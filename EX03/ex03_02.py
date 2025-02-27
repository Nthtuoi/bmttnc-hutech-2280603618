def daonguoclist (lst):
    return lst[::-1]
inputlist=input("Nhap danh sach cac so, cac nhau bang dau phay: ")
numbers = list(map(int ,inputlist.split(',')))
listdaonguoc = daonguoclist(numbers)
print("List sau khi dao nguoc la: ",listdaonguoc)