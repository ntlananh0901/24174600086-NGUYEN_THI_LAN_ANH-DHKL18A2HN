# câu 6
# Khai báo từ điển để lưu trữ dữ liệu môn học và sinh viên
mon_hoc = {
    "MATH101": {
        "ten": "Toán Cao cấp",
        "sinh_vien": ["SV001", "SV002"]
    },
    "PHY101": {
        "ten": "Vật lý Cơ bản",
        "sinh_vien": ["SV003", "SV004"]
    }
}

sinh_vien = {
    "SV001": {"ten": "Nguyễn Văn A", "diem_trung_binh": 8.0, "nam_hoc": 2021},
    "SV002": {"ten": "Trần Thị B", "diem_trung_binh": 7.5, "nam_hoc": 2021},
    "SV003": {"ten": "Lê Văn C", "diem_trung_binh": 9.0, "nam_hoc": 2022},
    "SV004": {"ten": "Phạm Thị D", "diem_trung_binh": 6.5, "nam_hoc": 2022}
}

def xem_danh_sach_sinh_vien_theo_mon(ma_mon_hoc):
    try:
        if ma_mon_hoc not in mon_hoc:
            raise KeyError("Môn học không tồn tại!")
        
        danh_sach_sinh_vien = mon_hoc[ma_mon_hoc]["sinh_vien"]
        
        # In ra danh sách sinh viên
        print(f"Danh sách sinh viên trong môn học {ma_mon_hoc} - {mon_hoc[ma_mon_hoc]['ten']}:")
        for ma_sv in danh_sach_sinh_vien:
            sv = sinh_vien[ma_sv]
            print(f"Mã sinh viên: {ma_sv}, Tên sinh viên: {sv['ten']}, Điểm trung bình: {sv['diem_trung_binh']}, Năm học: {sv['nam_hoc']}")
    except KeyError as e:
        print(e)

def menu():
    print("""
    Vui lòng lựa chọn chức năng (bằng số):
    1- Xem danh sách sinh viên theo mã môn học
    2- Kết thúc chương trình
    """)

while True:
    menu()
    lua_chon = input("Nhập vào lựa chọn của bạn: ")

    if lua_chon == "1":
        ma_mon_hoc = input("Nhập mã môn học: ")
        xem_danh_sach_sinh_vien_theo_mon(ma_mon_hoc)
    
    elif lua_chon == "2":
        print("Kết thúc chương trình!")
        break
    
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại!")



