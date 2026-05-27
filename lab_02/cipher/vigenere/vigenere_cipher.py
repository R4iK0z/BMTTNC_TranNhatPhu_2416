class VigenereCipher:
    def __init__(self):
        pass # Constructor có thể không cần làm gì đặc biệt nếu không có trạng thái cần khởi tạo

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                # Tính key_shift, đảm bảo key luôn là chữ hoa để lấy giá trị shift
                key_char = key[key_index % len(key)].upper()
                key_shift = ord(key_char) - ord('A')

                if char.isupper():
                    # Mã hóa chữ hoa
                    # (ord(char) - ord('A') + key_shift) % 26 tính toán vị trí mới trong bảng chữ cái (0-25)
                    # sau đó cộng với ord('A') để quay lại mã ASCII của chữ hoa
                    encrypted_char_code = (ord(char) - ord('A') + key_shift) % 26 + ord('A')
                    encrypted_text += chr(encrypted_char_code)
                else: # char.islower()
                    # Mã hóa chữ thường
                    encrypted_char_code = (ord(char) - ord('a') + key_shift) % 26 + ord('a')
                    encrypted_text += chr(encrypted_char_code)
                
                key_index += 1 # Chỉ tăng key_index khi xử lý một ký tự chữ cái
            else:
                # Giữ nguyên các ký tự không phải chữ cái
                encrypted_text += char
        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                # Tính key_shift, đảm bảo key luôn là chữ hoa
                key_char = key[key_index % len(key)].upper()
                key_shift = ord(key_char) - ord('A')

                if char.isupper():
                    # Giải mã chữ hoa
                    # (ord(char) - ord('A') - key_shift + 26) % 26 tính toán vị trí gốc
                    # (+26 để đảm bảo kết quả không âm trước khi lấy modulo)
                    decrypted_char_code = (ord(char) - ord('A') - key_shift + 26) % 26 + ord('A')
                    decrypted_text += chr(decrypted_char_code)
                else: # char.islower()
                    # Giải mã chữ thường
                    decrypted_char_code = (ord(char) - ord('a') - key_shift + 26) % 26 + ord('a')
                    decrypted_text += chr(decrypted_char_code)
                
                key_index += 1 # Chỉ tăng key_index khi xử lý một ký tự chữ cái
            else:
                # Giữ nguyên các ký tự không phải chữ cái
                decrypted_text += char
        return decrypted_text

# Ví dụ sử dụng:
if __name__ == "__main__":
    cipher = VigenereCipher()
    
    plain = "HELLO WORLD 123!"
    k = "KEY"
    
    print(f"Plain text:  {plain}")
    print(f"Key:         {k}")
    
    encrypted = cipher.vigenere_encrypt(plain, k)
    print(f"Encrypted:   {encrypted}")
    
    decrypted = cipher.vigenere_decrypt(encrypted, k)
    print(f"Decrypted:   {decrypted}")

    print("-" * 20)

    plain2 = "Attack at dawn"
    k2 = "LEMON"
    encrypted2 = cipher.vigenere_encrypt(plain2, k2) # Dự kiến: LXFOPVEFRNHR
    print(f"Plain text:  {plain2}")
    print(f"Key:         {k2}")
    print(f"Encrypted:   {encrypted2}")
    decrypted2 = cipher.vigenere_decrypt(encrypted2, k2)
    print(f"Decrypted:   {decrypted2}")