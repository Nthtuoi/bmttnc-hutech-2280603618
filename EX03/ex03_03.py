def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhap danh sach cac so , cac nhau bang dua phay: ")
numbers = list(map(int,input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("List: ",numbers)
print("Tuple tu list: ",my_tuple)