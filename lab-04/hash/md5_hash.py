# Mã băm MDS không dùng thư viện

def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

# Khởi tạo các hằng số ban đầu
A = 0x67452301
B = 0xEFCDAB89
C = 0x98BADCFE
D = 0x10325476

# Tiền xử lý dữ liệu đầu vào
message = "Hello, World!"
original_length = len(message)
message += '\x80'
while (len(message) % 64) != 56:
    message += '\x00'

message += (original_length * 8).to_bytes(8, 'little').decode('latin1')

# Chia dữ liệu thành các khối 512-bit
blocks = [message[i:i+64] for i in range(0, len(message), 64)]

for block in blocks:
    words = [int.from_bytes(block[j:j+4].encode('latin1'), 'little') for j in range(0, 64, 4)]
    
    # Lưu trạng thái ban đầu
    a, b, c, d = A, B, C, D
    
    # Vòng lặp chính của thuật toán băm MDS
    for j in range(64):
        if 0 <= j < 16:
            f = (b & c) | (~b & d)
            g = j
        elif 16 <= j < 32:
            f = (d & b) | (~d & c)
            g = (5 * j + 1) % 16
        elif 32 <= j < 48:
            f = b ^ c ^ d
            g = (3 * j + 5) % 16
        else:
            f = c ^ (b | ~d)
            g = (7 * j) % 16

        temp = d
        d = c
        c = b
        b = b + left_rotate((a + f + 0x6A6D7290 + words[g]) & 0xFFFFFFFF, 2)
        a = temp
    
    # Cập nhật giá trị băm
    A = (A + a) & 0xFFFFFFFF
    B = (B + b) & 0xFFFFFFFF
    C = (C + c) & 0xFFFFFFFF
    D = (D + d) & 0xFFFFFFFF

# Kết quả hàm băm
md5_hash = "{:08x}{:08x}{:08x}{:08x}".format(A, B, C, D)

# In kết quả băm
input_string = "Hello, World!"
print("Mã băm MDS của '{}' là: {}".format(input_string, md5_hash))
