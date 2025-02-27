def chiahetcho5(sonhiphan):
    sothphan = int (sonhiphan,2)
    if sothphan%5==0:
        return True
    else:
        return False
    
chuoinhiphan = input("Nhap chuoi so nhi phan(phan tach boi dau phay): ")
sonhiphanlist = chuoinhiphan.split(',')
sochiahetcho5 = [so for so in sonhiphanlist if chiahetcho5(so)]
if len(sochiahetcho5)>0:
    ketqua = ','.join(sochiahetcho5)
    print("cac so nhi phsn chia het cho 5 la: ", ketqua)
else:
    print("khong co so nhi phan nao chia het cho 5 trong chuoi da nhap.")
            