import collections

class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        # Chuyển "J" thành "I" trong khóa
        key = key.replace("J", "I")
        key = key.upper()
        
        # Dùng OrderedDict để giữ thứ tự và loại bỏ ký tự trùng lặp
        key_set = collections.OrderedDict.fromkeys(list(key))
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = []
        for letter in alphabet:
            if letter not in key_set:
                remaining_letters.append(letter)
        
        matrix_list = list(key_set.keys()) + remaining_letters
        
        # Đảm bảo ma trận có đúng 25 ký tự
        if len(matrix_list) > 25:
            matrix_list = matrix_list[:25]
        
        playfair_matrix = [matrix_list[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return -1, -1 # Trả về nếu không tìm thấy (trường hợp ký tự không hợp lệ)

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "J" thành "I" trong văn bản đầu vào
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        # Loại bỏ các ký tự không phải chữ cái
        plain_text = ''.join(filter(str.isalpha, plain_text))

        # Xử lý các cặp ký tự giống nhau bằng cách chèn 'X'
        processed_text = ""
        i = 0
        while i < len(plain_text):
            char1 = plain_text[i]
            if i + 1 < len(plain_text):
                char2 = plain_text[i+1]
                if char1 == char2:
                    processed_text += char1 + "X"
                    i += 1
                else:
                    processed_text += char1 + char2
                    i += 2
            else:
                processed_text += char1
                i += 1

        plain_text = processed_text
        
        # Thêm 'X' nếu độ dài văn bản là số lẻ
        if len(plain_text) % 2 != 0:
            plain_text += "X"

        encrypted_text = ""
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
        
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        # 1. Giải mã các cặp ký tự qua ma trận
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        # 2. Xử lý xóa bỏ các chữ 'X' độn dữ liệu
        banro = ""
        length = len(decrypted_text)
        i = 0
        while i < length:
            banro += decrypted_text[i]
            # Nếu ký tự tiếp theo là 'X' và ký tự sau 'X' giống ký tự hiện tại -> Bỏ qua 'X'
            if i + 2 < length and decrypted_text[i+1] == 'X' and decrypted_text[i] == decrypted_text[i+2]:
                banro += decrypted_text[i+2]
                i += 3  # Nhảy qua cả cụm (Ký tự + 'X' + Ký tự trùng)
            else:
                if i + 1 < length:
                    banro += decrypted_text[i+1]
                i += 2  # Nhảy sang cặp tiếp theo bình thường

        # Xử lý ký tự 'X' thừa ở cuối cùng (nếu có do chuỗi lẻ ban đầu)
        if banro.endswith("X"):
            banro = banro[:-1]

        return banro

# --- Ví dụ sử dụng ---
if __name__ == "__main__":
    cipher = PlayFairCipher()
    
    key = "MONARCHY"
    plain_text = "instruments"
    
    print(f"Khóa: {key}")
    print(f"Bản rõ gốc: {plain_text}")
    print("-" * 30)
    
    # 1. Tạo ma trận Playfair
    playfair_matrix = cipher.create_playfair_matrix(key)
    print("Ma trận Playfair:")
    for row in playfair_matrix:
        print(row)
    print("-" * 30)
    
    # 2. Mã hóa
    cipher_text = cipher.playfair_encrypt(plain_text, playfair_matrix)
    print(f"Bản mã: {cipher_text}")
    
    # 3. Giải mã
    decrypted_text = cipher.playfair_decrypt(cipher_text, playfair_matrix)
    print(f"Bản rõ sau giải mã: {decrypted_text.upper()}")