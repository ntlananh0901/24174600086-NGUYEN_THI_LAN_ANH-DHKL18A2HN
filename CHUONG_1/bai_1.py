# nHẬP ĐỘ DÀI  CHỮ NHẬT
d = int(input("Nhập chiều dài hình chữ nhật:" ))
r = int(input("Nhập chiều rộng của hình chữ nhật:"))
# Tính chu vi và diện tích hcn
cv = (d +r )*2
s = d * r
 
#IN chiều dài , chiều rộng, chu vi và diện tích
class Hinh_chu_nhat:
    def __init__(self, d, r, cv, s):
        self.d = d
        self.r = r
        self.cv = cv
        self.s = s

    def display(self):
        print("Các chỉ số tương ứng của hình chữ nhật:")
        print("Chiều dài:", self.d)
        print("Chiều rộng:", self.r)
        print("Chu vi:", self.cv)
        print("Diện tích:", self.s)

# Tạo đối tượng và hiển thị
hcn = Hinh_chu_nhat(d, r, cv, s)
hcn.display() 