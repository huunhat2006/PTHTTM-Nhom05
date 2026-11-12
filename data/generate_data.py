import os
import random
import csv

ho_list = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý"]
dem_list = ["Văn", "Thị", "Quang", "Minh", "Hồng", "Đức", "Thành", "Hoàng", "Ngọc", "Thanh", "Bảo", "Xuân", "Hải", "Tuấn"]
ten_list = ["An", "Bình", "Cường", "Dũng", "Hoa", "Hùng", "Linh", "Nam", "Nguyên", "Tuấn", "Thắng", "Lan", "Mai", "Tùng", "Khoa", "Trang", "Huy", "Hương", "Trâm", "Kiên", "Sơn", "Hà", "Phong", "Phúc", "Thảo", "Hạnh", "Đạt", "Long", "Vy", "Yến"]

chuyen_nganh_list = [
    "Công nghệ thông tin",
    "Khoa học máy tính",
    "Kỹ thuật phần mềm",
    "An toàn thông tin",
    "Hệ thống thông tin",
    "Mạng máy tính và truyền thông dữ liệu",
    "Trí tuệ nhân tạo"
]

def tao_ten_ngau_nhien():
    h = random.choice(ho_list)
    d = random.choice(dem_list)
    t = random.choice(ten_list)
    return f"{h} {d} {t}"

def sinh_bo_du_lieu(so_luong=1500):
    os.makedirs("data", exist_ok=True)
    danh_sach = []
    
    for i in range(1, so_luong + 1):
        ma_sv = f"B21DCCN{i:04d}"
        ho_ten = tao_ten_ngau_nhien()
        nganh = random.choice(chuyen_nganh_list)
        
        phan_nhom = random.choices(["xuat_sac", "gioi", "kha", "trung_binh", "nguy_co"], weights=[0.12, 0.28, 0.35, 0.15, 0.10])[0]
        
        if phan_nhom == "xuat_sac":
            diem_gpa = round(random.uniform(3.60, 4.00), 2)
            diem_chuyen_can = round(random.uniform(9.0, 10.0), 1)
            diem_giua_ky = round(random.uniform(8.5, 10.0), 1)
            diem_do_an = round(random.uniform(8.8, 10.0), 1)
            so_gio_hoc = round(random.uniform(25.0, 35.0), 1)
            ty_le_diem_danh = round(random.uniform(95.0, 100.0), 1)
            tuong_tac_lms = random.randint(160, 240)
            bai_tap_dung_han = random.randint(11, 12)
            cau_hoi_dien_dan = random.randint(15, 30)
            nhan = "Xuất sắc"
        elif phan_nhom == "gioi":
            diem_gpa = round(random.uniform(3.20, 3.59), 2)
            diem_chuyen_can = round(random.uniform(8.5, 9.5), 1)
            diem_giua_ky = round(random.uniform(8.0, 9.0), 1)
            diem_do_an = round(random.uniform(8.0, 9.0), 1)
            so_gio_hoc = round(random.uniform(20.0, 26.0), 1)
            ty_le_diem_danh = round(random.uniform(90.0, 98.0), 1)
            tuong_tac_lms = random.randint(120, 170)
            bai_tap_dung_han = random.randint(10, 12)
            cau_hoi_dien_dan = random.randint(10, 18)
            nhan = "Giỏi"
        elif phan_nhom == "kha":
            diem_gpa = round(random.uniform(2.50, 3.19), 2)
            diem_chuyen_can = round(random.uniform(7.5, 8.5), 1)
            diem_giua_ky = round(random.uniform(7.0, 8.2), 1)
            diem_do_an = round(random.uniform(7.0, 8.2), 1)
            so_gio_hoc = round(random.uniform(15.0, 21.0), 1)
            ty_le_diem_danh = round(random.uniform(80.0, 92.0), 1)
            tuong_tac_lms = random.randint(80, 130)
            bai_tap_dung_han = random.randint(8, 11)
            cau_hoi_dien_dan = random.randint(5, 12)
            nhan = "Khá"
        elif phan_nhom == "trung_binh":
            diem_gpa = round(random.uniform(2.00, 2.49), 2)
            diem_chuyen_can = round(random.uniform(6.5, 7.8), 1)
            diem_giua_ky = round(random.uniform(5.5, 7.0), 1)
            diem_do_an = round(random.uniform(5.5, 7.0), 1)
            so_gio_hoc = round(random.uniform(10.0, 16.0), 1)
            ty_le_diem_danh = round(random.uniform(70.0, 84.0), 1)
            tuong_tac_lms = random.randint(50, 90)
            bai_tap_dung_han = random.randint(5, 8)
            cau_hoi_dien_dan = random.randint(2, 6)
            nhan = "Trung bình"
        else:
            diem_gpa = round(random.uniform(1.00, 1.99), 2)
            diem_chuyen_can = round(random.uniform(4.0, 6.0), 1)
            diem_giua_ky = round(random.uniform(3.0, 5.0), 1)
            diem_do_an = round(random.uniform(3.0, 5.0), 1)
            so_gio_hoc = round(random.uniform(4.0, 9.0), 1)
            ty_le_diem_danh = round(random.uniform(45.0, 68.0), 1)
            tuong_tac_lms = random.randint(10, 45)
            bai_tap_dung_han = random.randint(1, 4)
            cau_hoi_dien_dan = random.randint(0, 2)
            nhan = "Nguy cơ cảnh báo"

        danh_sach.append({
            "ma_sinh_vien": ma_sv,
            "ho_ten": ho_ten,
            "chuyen_nganh": nganh,
            "diem_gpa": diem_gpa,
            "diem_chuyen_can": diem_chuyen_can,
            "diem_giua_ky": diem_giua_ky,
            "diem_do_an": diem_do_an,
            "so_gio_hoc_tuan": so_gio_hoc,
            "ty_le_diem_danh": ty_le_diem_danh,
            "so_lan_tuong_tac_lms": tuong_tac_lms,
            "so_bai_tap_nop_dung_han": bai_tap_dung_han,
            "so_cau_hoi_dien_dan": cau_hoi_dien_dan,
            "trinh_do_hoc_tap": nhan
        })
    
    random.shuffle(danh_sach)
    
    fields = list(danh_sach[0].keys())
    
    with open("data/du_lieu_sinh_vien.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(danh_sach)
        
    diem_cat = int(len(danh_sach) * 0.8)
    tap_huan_luyen = danh_sach[:diem_cat]
    tap_kiem_thu = danh_sach[diem_cat:]
    
    with open("data/du_lieu_huan_luyen.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(tap_huan_luyen)
        
    with open("data/du_lieu_kiem_thu.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(tap_kiem_thu)

if __name__ == "__main__":
    sinh_bo_du_lieu(1500)

