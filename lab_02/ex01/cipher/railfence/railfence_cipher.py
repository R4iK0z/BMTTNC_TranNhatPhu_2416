class RailFenceCipher:
    def __init__(self):
        """
        Hàm khởi tạo, không cần làm gì ở đây.
        """
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        """
        Hàm mã hóa văn bản bằng thuật toán Rail Fence.
        :param plain_text: Văn bản gốc cần mã hóa.
        :param num_rails: Số lượng "hàng rào".
        :return: Văn bản đã được mã hóa.
        """
        # Nếu chỉ có 1 hàng rào, không cần mã hóa
        if num_rails <= 1:
            return plain_text

        # Tạo các hàng rào rỗng
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1 = đi xuống, -1 = đi lên

        # Điền các ký tự vào hàng rào theo đường zig-zag
        for char in plain_text:
            rails[rail_index].append(char)
            
            # Đổi hướng khi chạm đến hàng rào trên cùng hoặc dưới cùng
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            
            rail_index += direction

        # Nối các ký tự từ các hàng rào lại với nhau
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        """
        Hàm giải mã văn bản đã được mã hóa bằng Rail Fence.
        :param cipher_text: Văn bản đã được mã hóa.
        :param num_rails: Số lượng "hàng rào" đã dùng để mã hóa.
        :return: Văn bản gốc.
        """
        # Nếu chỉ có 1 hàng rào, không cần giải mã
        if num_rails <= 1:
            return cipher_text

        # --- Bước 1: Tính độ dài của mỗi hàng rào ---
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # --- Bước 2: Xây dựng lại các hàng rào từ bản mã ---
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start : start + length]))
            start += length

        # --- Bước 3: Đọc các hàng rào theo đường zig-zag để lấy lại bản rõ ---
        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            # Lấy ký tự đầu tiên từ hàng rào hiện tại
            plain_text += rails[rail_index].pop(0)
            
            # Di chuyển đến hàng rào tiếp theo
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        return plain_text

