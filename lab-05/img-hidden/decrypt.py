import sys
from PIL import Image

def decode_image(encoded_image_path):
    # Open the image
    img = Image.open(encoded_image_path)
    width, height = img.size

    binary_message = ""

    # Extract the least significant bit (LSB) of each color channel in each pixel
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):  # RGB channels
                binary_message += format(pixel[color_channel], '08b')[-1]  # Get LSB

    # Convert binary to text
    message = ""
    for i in range(0, len(binary_message), 8):  # Read 8-bit chunks
        char = chr(int(binary_message[i:i+8], 2))
        if char == '\x0E':  # Stop decoding when end marker (1111111111111110) is encountered
            break
        message += char

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)

    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()
