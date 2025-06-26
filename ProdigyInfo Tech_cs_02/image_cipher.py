from PIL import Image
import os

def encrypt_image(image_path, key, output_path="encrypted.png"):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )
    image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, key, output_path="decrypted.png"):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )
    image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("=== Image Encryption & Decryption Tool ===")
    path = input("Enter image path (PNG/JPG): ")
    key = int(input("Enter a numeric key (e.g., 10): "))
    choice = input("Encrypt or Decrypt (e/d): ").lower()

    if not os.path.exists(path):
        print("Image not found!")
        return

    if choice == 'e':
        encrypt_image(path, key)
    elif choice == 'd':
        decrypt_image(path, key)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
