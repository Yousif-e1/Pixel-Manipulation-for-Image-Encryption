from PIL import Image
import numpy as np

input_image_path = r'C:\Users\youssef\Downloads\Mini_Projects\introduction_to_cip.png'

def load_image(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = np.array(image)
    return pixels

def encrypt(pixels):
    encrypted_pixels = pixels.copy()
    encrypted_pixels[:, :, 0], encrypted_pixels[:, :, 1] = encrypted_pixels[:, :, 1], encrypted_pixels[:, :, 0]
    return encrypted_pixels

def decrypt(encrypted_pixels):
    decrypted_pixels = encrypted_pixels.copy()
    decrypted_pixels[:, :, 0], decrypted_pixels[:, :, 1] = decrypted_pixels[:, :, 1], decrypted_pixels[:, :, 0]
    return decrypted_pixels

def save_image(pixels, output_path):
    image = Image.fromarray(pixels.astype(np.uint8))
    image.save(output_path)

pixels = load_image(input_image_path)

encrypted_pixels = encrypt(pixels)
output_encrypted_path = r'C:\Users\youssef\Downloads\Mini_Projects\encrypted_image.png'
save_image(encrypted_pixels, output_encrypted_path)

decrypted_pixels = decrypt(encrypted_pixels)
output_decrypted_path = r'C:\Users\youssef\Downloads\Mini_Projects\decrypted_image.png'
save_image(decrypted_pixels, output_decrypted_path)
