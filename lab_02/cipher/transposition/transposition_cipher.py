import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        # Số cột trong lưới hoán vị
        num_cols = math.ceil(len(text) / key)
        # Số hàng trong lưới hoán vị
        num_rows = key
        # Số ô bị tô bóng (không dùng) ở cuối lưới
        num_shaded_boxes = (num_cols * num_rows) - len(text)

        # Mỗi chuỗi trong decrypted_text tương ứng với một cột trong lưới
        decrypted_text = [''] * num_cols
        
        col = 0
        row = 0
        
        for symbol in text:
            decrypted_text[col] += symbol
            col += 1

            # Nếu không còn hàng nào trong cột hiện tại
            # hoặc nếu đang ở cột có ít hàng hơn do ô bị tô bóng
            if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1
                
        return ''.join(decrypted_text)


# --- Ví dụ sử dụng ---
if __name__ == "__main__":
    cipher = TranspositionCipher()
    
    my_message = "Common sense is not so common."
    my_key = 8
    
    # Mã hóa
    encrypted = cipher.encrypt(my_message, my_key)
    print(f"Bản mã: {encrypted}|") # Thêm dấu | để thấy các khoảng trắng cuối
    
    # Giải mã
    decrypted = cipher.decrypt(encrypted, my_key)
    print(f"Bản rõ: {decrypted}|")