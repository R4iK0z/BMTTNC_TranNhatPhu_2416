from SinhVien import SinhVien

class QuanLySinhVien:
    # It's better practice to initialize listSinhVien in __init__
    # to avoid it being a class variable shared by all instances.
    # However, I will transcribe as shown in the image first, then suggest correction.
    # listSinhVien = [] # As per image, but this is a class variable

    def __init__(self): # Assuming an __init__ is needed for instance-specific lists
        self.listSinhVien = [] # Correct way to make it an instance variable

    def generateID(self):
        maxId = 1
        if (self.soluongSinhVien() > 0):
            # This assumes the first student has the lowest ID if not sorted,
            # or it's just a starting point to find the max.
            maxId = self.listSinhVien[0]._id 
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1 # Next ID will be max existing ID + 1
        return maxId

    def soluongSinhVien(self):
        return len(self.listSinhVien) # More Pythonic than __len__()

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if (sv != None):
            # Assuming these are the fields to update
            name = input(f"Nhap ten sinh vien moi (hien tai: {sv._name}): ")
            sex = input(f"Nhap gioi tinh sinh vien moi (hien tai: {sv._sex}): ")
            # The image showed major = int(input(...)) which is likely a typo. Major is usually a string.
            major = input(f"Nhap chuyen nganh cua sinh vien moi (hien tai: {sv._major}): ")
            diemTB = float(input(f"Nhap diem cua sinh vien moi (hien tai: {sv._diemTB}): "))
            
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv) # Re-calculate academic performance
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.") # Corrected format string

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        # Usually, scores are sorted high to low, so reverse=True would be common.
        # Transcribing as per image.
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False) 

    def findByID(self, ID):
        searchResult = None
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
                    break # Found, no need to continue loop
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()): # Case-insensitive search
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv: SinhVien): # Type hint is good
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        # Print header
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        
        if (len(listSV) > 0): # More Pythonic
            for sv in listSV:
                # sv._hocLuc is an attribute, not a method, so no ()
                print("{:<8} {:<18} {:<8} {:<8} {:<8.2f} {:<8}" 
                      .format(sv._id, sv._name, sv._sex, sv._major, 
                              sv._diemTB, sv._hocLuc)) 
        print("\n") # Add a newline for better separation

    def getListSinhVien(self):
        return self.listSinhVien