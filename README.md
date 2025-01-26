# Pixel-Manipulation-for-Image-Encryption
This Program performs a simple encryption and decryption on an image by swapping the red and green channels of each pixel.

# Here's a breakdown of how it works:
1 Loading the Image:**
   - The `load_image(image_path)` function opens an image using `PIL.Image.open()` and converts it into RGB format. Then it uses `numpy.array()` to get the pixel data in a NumPy array, where each pixel is represented by three values (for Red, Green, and Blue channels).

2 Encryption:**
   - In the `encrypt(pixels)` function, the red and green color channels of the image pixels are swapped. This creates a basic "encryption" by altering the pixel colors without affecting the blue channel.

3 Decryption:**
   - The `decrypt(encrypted_pixels)` function simply swaps the red and green channels back to their original state, undoing the encryption.

4 Saving the Image:**
   - The `save_image(pixels, output_path)` function takes the modified pixels, converts them back into an image using `Image.fromarray()`, and saves the result using `.save()`.

### Example of the process:
- Input Image**: The original image (`input_image_path`).
- Encryption**: Swaps the red and green channels, and saves the encrypted image to `output_encrypted_path`.
- Decryption**: Swaps the red and green channels back to their original state, and saves the decrypted image to `output_decrypted_path`.

### How to Use:
1. Make sure the `input_image_path` points to an existing image file on your system.
2. The encrypted and decrypted images will be saved to the paths specified in `output_encrypted_path` and `output_decrypted_path`.
