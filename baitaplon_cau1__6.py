# Khai báo từ điển để lưu trữ dữ liệu môn học và sinh viên
mon_hoc = {}
sinh_vien = {}

def them_mon_hoc(ma_mon_hoc, ten_mon_hoc, so_sv_toi_da=60):
    try:
        if ma_mon_hoc in mon_hoc:
            raise ValueError("Môn học đã tồn tại!")
        mon_hoc[ma_mon_hoc] = {
            "ten": ten_mon_hoc,
            "sinh_vien": [],
            "so_sv_toi_da": so_sv_toi_da
        }
        print("Đã thêm môn học mới!")
    except ValueError as e:
        print(e)

def xem_danh_sach_mon_hoc(sap_xep_theo="ma"):
    try:
        if sap_xep_theo == "ma":
            mon_hoc_sap_xep = sorted(mon_hoc.items(), key=lambda x: x[0])
        elif sap_xep_theo == "ten":
            mon_hoc_sap_xep = sorted(mon_hoc.items(), key=lambda x: x[1]["ten"])
        else:
            raise ValueError("Lựa chọn không hợp lệ!")
        
        for ma_mon_hoc, chi_tiet in mon_hoc_sap_xep:
            print(f"Mã môn học: {ma_mon_hoc}, Tên môn học: {chi_tiet['ten']}, Số lượng sinh viên: {len(chi_tiet['sinh_vien'])}")
    except ValueError as e:
        print(e)

def tim_kiem_mon_hoc(yeu_cau, tim_theo="ma"):
    try:
        if tim_theo == "ma":
            if yeu_cau in mon_hoc:
                chi_tiet = mon_hoc[yeu_cau]
                print(f"Mã môn học: {yeu_cau}, Tên môn học: {chi_tiet['ten']}, Số lượng sinh viên: {len(chi_tiet['sinh_vien'])}")
            else:
                raise KeyError("Không tìm thấy môn học!")
        elif tim_theo == "ten":
            found = False
            for ma_mon_hoc, chi_tiet in mon_hoc.items():
                if chi_tiet["ten"] == yeu_cau:
                    print(f"Mã môn học: {ma_mon_hoc}, Tên môn học: {chi_tiet['ten']}, Số lượng sinh viên: {len(chi_tiet['sinh_vien'])}")
                    found = True
                    break
            if not found:
                raise KeyError("Không tìm thấy môn học!")
        else:
            raise ValueError("Lựa chọn không hợp lệ!")
    except (KeyError, ValueError) as e:
        print(e)

def chinh_sua_mon_hoc(yeu_cau, ten_moi, chinh_sua_theo="ma"):
    try:
        if chinh_sua_theo == "ma":
            if yeu_cau in mon_hoc:
                mon_hoc[yeu_cau]["ten"] = ten_moi
                print("Đã cập nhật tên môn học!")
            else:
                raise KeyError("Không tìm thấy môn học!")
        elif chinh_sua_theo == "ten":
            found = False
            for ma_mon_hoc, chi_tiet in mon_hoc.items():
                if chi_tiet["ten"] == yeu_cau:
                    mon_hoc[ma_mon_hoc]["ten"] = ten_moi
                    print("Đã cập nhật tên môn học!")
                    found = True
                    break
            if not found:
                raise KeyError("Không tìm thấy môn học!")
        else:
            raise ValueError("Lựa chọn không hợp lệ!")
    except (KeyError, ValueError) as e:
        print(e)

def xoa_mon_hoc(yeu_cau, xoa_theo="ma"):
    try:
        if xoa_theo == "ma":
            if yeu_cau in mon_hoc:
                if len(mon_hoc[yeu_cau]["sinh_vien"]) == 0:
                    del mon_hoc[yeu_cau]
                    print("Đã xóa môn học!")
                else:
                    raise ValueError("Không thể xóa môn học có sinh viên đang học!")
            else:
                raise KeyError("Không tìm thấy môn học!")
        elif xoa_theo == "ten":
            found = False
            for ma_mon_hoc, chi_tiet in mon_hoc.items():
                if chi_tiet["ten"] == yeu_cau:
                    if len(chi_tiet["sinh_vien"]) == 0:
                        del mon_hoc[ma_mon_hoc]
                        print("Đã xóa môn học!")
                    else:
                        raise ValueError("Không thể xóa môn học có sinh viên đang học!")
                    found = True
                    break
            if not found:
                raise KeyError("Không tìm thấy môn học!")
        else:
            raise ValueError("Lựa chọn không hợp lệ!")
    except (KeyError, ValueError) as e:
        print(e)

def xem_danh_sach_sinh_vien_theo_mon(ma_mon_hoc, sap_xep_theo="id"):
    try:
        if ma_mon_hoc not in mon_hoc:
            raise KeyError("Môn học không tồn tại!")
        danh_sach_sinh_vien = mon_hoc[ma_mon_hoc]["sinh_vien"]
        sinh_vien_sap_xep = sorted(danh_sach_sinh_vien, key=lambda ma_sv: (sinh_vien[ma_sv]["diem_trung_binh"], ma_sv))
        
        print(f"Danh sách sinh viên trong môn học {ma_mon_hoc}:")
        for ma_sv in sinh_vien_sap_xep:
            sv = sinh_vien[ma_sv]
            print(f"Mã sinh viên: {ma_sv}, Tên sinh viên: {sv['ten']}, Điểm trung bình: {sv['diem_trung_binh']}")
    except KeyError as e:
        print(e)

# Ví dụ sử dụng các chức năng đã định nghĩa
them_mon_hoc("CSE101", "Lập trình Cơ bản")
them_mon_hoc("MAT202", "Toán Cao cấp")

sinh_vien["SV001"] = {"ten": "Nguyen Van A", "diem_trung_binh": 3.8}
sinh_vien["SV002"] = {"ten": "Le Thi B", "diem_trung_binh": 3.5}
sinh_vien["SV003"] = {"ten": "Tran Van C", "diem_trung_binh": 4.0}

mon_hoc["CSE101"]["sinh_vien"].extend(["SV001", "SV002"])
mon_hoc["MAT202"]["sinh_vien"].append("SV003")

print("Danh sách môn học sắp xếp theo mã môn học:")
xem_danh_sach_mon_hoc(sap_xep_theo="ma")

print("\nThông tin môn học CSE101:")
tim_kiem_mon_hoc("CSE101", tim_theo="ma")

print("\nChỉnh sửa tên môn học CSE101 thành 'Lập trình Python':")
chinh_sua_mon_hoc("CSE101", "Lập trình Python", chinh_sua_theo="ma")
tim_kiem_mon_hoc("CSE101", tim_theo="ma")

print("\nDanh sách sinh viên trong môn học CSE101:")
xem_danh_sach_sinh_vien_theo_mon("CSE101")
