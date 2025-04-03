import sys
from PIL import Image

def encode_image(image_path, message):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Marks the end of the message

    # Get the image pixels
    data_index = 0

    # Loop through every pixel
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))  # Get the RGB values of the pixel

            for color_channel in range(3):  # RGB channels
                if data_index < len(binary_message):
                    # Modify the least significant bit of each color channel
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1

            # Update the pixel with the new modified value
            img.putpixel((col, row), tuple(pixel))

            # If all data has been encoded, exit the loop
            if data_index >= len(binary_message):
                break

        if data_index >= len(binary_message):
            break

    # Save the encoded image
    encoded_image_path = "encoded_image.png"
    img.save(encoded_image_path)

    print(f"Steganography complete. Encoded image saved as {encoded_image_path}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image path> <message>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]

    encode_image(image_path, message)

if __name__ == "__main__":
    main()
