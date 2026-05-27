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

    def split_pairs(self, plain_text):
        # 1. Chuyển "J" thành "I" và chuẩn hóa chuỗi dữ liệu đầu vào
        plain_text = plain_text.replace("J", "I").upper()
        plain_text = ''.join(filter(str.isalpha, plain_text))

        # 2. Xử lý chia cặp ký tự giống nhau bằng cách chèn 'X'
        processed_text = ""
        i = 0
        while i < len(plain_text):
            char1 = plain_text[i]
            if i + 1 < len(plain_text):
                char2 = plain_text[i+1]
                if char1 == char2:
                    processed_text += char1 + "X"
                    i += 1  # Tiến 1 bước để ký tự trùng tiếp theo đi với cặp sau
                else:
                    processed_text += char1 + char2
                    i += 2  # Tiến 2 bước lấy cặp bình thường
            else:
                processed_text += char1
                i += 1

        # 3. Thêm 'X' vào cuối nếu tổng độ dài văn bản là số lẻ
        if len(processed_text) % 2 != 0:
            processed_text += "X"
            
        return processed_text

    def playfair_encrypt(self, plain_text, matrix):
        # Gọi hàm split_pairs để xử lý chia cặp ký tự trước khi mã hóa
        processed_text = self.split_pairs(plain_text)

        encrypted_text = ""
        # Duyệt qua từng cặp 2 ký tự một để thực hiện biến đổi ma trận
        for i in range(0, len(processed_text), 2):
            pair = processed_text[i:i+2]
            
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Quy tắc cùng hàng
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Quy tắc cùng cột
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:  # Quy tắc hình chữ nhật (khác hàng khác cột)
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
        
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        # 1. Giải mã các cặp ký tự qua ma trận ngược (-1)
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

        # 2. XỬ LÝ SỬA LỖI: Duyệt tuần tự để khử chữ 'X' độn dữ liệu một cách chuẩn xác
        banro = ""
        length = len(decrypted_text)
        i = 0
        while i < length:
            # Kiểm tra xem chữ 'X' có nằm kẹp giữa 2 chữ cái giống nhau không (Ví dụ: L X L)
            if i > 0 and i + 1 < length and decrypted_text[i] == 'X' and decrypted_text[i-1] == decrypted_text[i+1]:
                # Đây là chữ X độn để tách từ trùng -> Bỏ qua không thêm vào bản rõ
                i += 1
            else:
                banro += decrypted_text[i]
                i += 1

        # Xử lý ký tự 'X' thừa ở cuối cùng (nếu có do chuỗi lẻ ban đầu độn vào cho chẵn cặp)
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
    print(f"Bản rõ sau giải mã: {decrypted_text}")