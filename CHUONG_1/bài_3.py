from math import gcd
class PS:
    def __init__(self, tu=0, mau=1):
        if mau == 0:
            raise ValueError("Mẫu số không được bằng 0")
        self.tu = tu
        self.mau = mau
        self.rut_gon()

    def is_valid(self):
        return self.mau != 0
    def rut_gon(self):
        if self.mau < 0:    # đổi dấu về mẫu dương
            self.tu = -self.tu
            self.mau = -self.mau
        ucln =  gcd(self.tu, self.mau) 
        if ucln != 0: 
            self.tu //= ucln 
            self.mau //= ucln
# Nhập phân số
    def nhap(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số : "))

        if self.mau == 0:  
            raise ValueError("Mẫu số ko được bằng 0")
        self.rut_gon()
# In phân số
    def xuat(self):
        if self.mau == 1:
            print(f"{self.tu}") 
        else:
            print(f"{self.tu}/{self.mau}")
if __name__ == "__main__":
    ps = PS(4, -8)
    print("Phân số khởi tạo: ", end="")
    ps.xuat()

    ps.nhap()
    print("Phân số sau khi nhập: ", end="")
    ps.xuat()                             