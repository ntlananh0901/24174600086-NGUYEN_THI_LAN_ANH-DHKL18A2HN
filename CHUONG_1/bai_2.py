class ThiSinh:
    def __init__(self, ho_ten="", diem_toan=0.0, diem_ly=0.0, diem_hoa=0.0):
        self.ho_ten = ho_ten
        self.diem_toan = float(diem_toan)
        self.diem_ly = float(diem_ly)
        self.diem_hoa = float(diem_hoa)

    def nhap(self):
        self.ho_ten = input("Họ tên: ").strip()
        self.diem_toan = float(input("Điểm Toán: "))
        self.diem_ly = float(input("Điểm Lý: "))
        self.diem_hoa = float(input("Điểm Hóa: "))

    def tinh_tong(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def in_thong_tin(self, chuan):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Toán: {self.diem_toan:.2f}, Lý: {self.diem_ly:.2f}, Hóa: {self.diem_hoa:.2f}")
        print(f"Tổng điểm: {self.tinh_tong():.2f}")
        print("Kết quả: ", "ĐẬU" if self.tinh_tong() >= chuan else "RỚT")
        print("---------------")


def main():
    CHUAN = 20   # điểm chuẩn
    n = int(input("Số lượng thí sinh: "))
    ds = []
    for i in range(n):
        print(f"\n--- Nhập thí sinh {i+1} ---")
        ts = ThiSinh()
        ts.nhap()
        ds.append(ts)

    # Sắp xếp giảm dần theo tổng điểm
    ds.sort(key=lambda x: x.tinh_tong(), reverse=True)

    print("\n=== Danh sách thí sinh (sắp xếp từ cao xuống thấp) ===")
    for ts in ds:
        ts.in_thong_tin(CHUAN)


if __name__ == "__main__":
    main()