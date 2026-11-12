import os
import pandas as pd
import numpy as np

DANH_SACH_DAC_TRUNG = [
    "diem_gpa",
    "diem_chuyen_can",
    "diem_giua_ky",
    "diem_do_an",
    "so_gio_hoc_tuan",
    "ty_le_diem_danh",
    "so_lan_tuong_tac_lms",
    "so_bai_tap_nop_dung_han",
    "so_cau_hoi_dien_dan"
]

ANH_XA_NHAN = {
    "Nguy cơ cảnh báo": 0,
    "Trung bình": 1,
    "Khá": 2,
    "Giỏi": 3,
    "Xuất sắc": 4
}

ANH_XA_NHAN_NGUOC = {v: k for k, v in ANH_XA_NHAN.items()}

def tai_du_lieu(duong_dan_file="data/du_lieu_sinh_vien.csv"):
    if not os.path.exists(duong_dan_file):
        from data.generate_data import sinh_bo_du_lieu
        sinh_bo_du_lieu(1500)
    df = pd.read_csv(duong_dan_file, encoding="utf-8-sig")
    return df

def chuan_bi_dac_trung_va_nhan(df):
    X = df[DANH_SACH_DAC_TRUNG].copy()
    y = df["trinh_do_hoc_tap"].map(ANH_XA_NHAN).values
    return X, y

