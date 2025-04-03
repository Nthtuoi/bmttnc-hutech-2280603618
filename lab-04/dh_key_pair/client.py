from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    try:
        # Đọc public key từ file
        with open("server_public_key.pem", "rb") as f:
            server_public_key = serialization.load_pem_public_key(f.read())

        # **Sửa lỗi ở đây**: lấy tham số từ khóa công khai của server
        parameters = server_public_key.parameters()

        # Tạo khóa client
        private_key, public_key = generate_client_key_pair(parameters)

        # Tạo khóa chung
        shared_secret = derive_shared_secret(private_key, server_public_key)

        print("Shared Secret:", shared_secret.hex())

    except FileNotFoundError:
        print("Error: server_public_key.pem not found. Run the server first!")

if __name__ == "__main__":
    main()
