import os
import json
from typing import List
from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from web_app.schemas import YeuCauDuDoanSinhVien, KetQuaDuDoan, YeuCauNhacNhoCoVan
from ml_engine.recommender import du_doan_trinh_do
from ml_engine.data_loader import tai_du_lieu
from database.db_connection import get_db

app = FastAPI(
    title="Hệ thống Gợi ý Lộ trình Học tập Sinh viên",
    description="Hệ thống AI phân loại trình độ và gợi ý lộ trình học tập cá nhân hóa",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="web_app/static"), name="static")
templates = Jinja2Templates(directory="web_app/templates")

@app.get("/api/suc-khoe")
def kiem_tra_suc_khoe():
    return {
        "trang_thai": "Hoạt động bình thường",
        "dich_vu": "Hệ thống Gợi ý Lộ trình Học tập Sinh viên",
        "phien_ban": "1.0.0",
        "cong_nghe": "FastAPI, PostgreSQL, XGBoost, Docker Swarm"
    }

@app.get("/", response_class=HTMLResponse)
def trang_chu(request: Request):
    df = tai_du_lieu()
    tong_sv = len(df)
    sv_xuat_sac = len(df[df["trinh_do_hoc_tap"] == "Xuất sắc"])
    sv_gioi = len(df[df["trinh_do_hoc_tap"] == "Giỏi"])
    sv_kha = len(df[df["trinh_do_hoc_tap"] == "Khá"])
    sv_trung_binh = len(df[df["trinh_do_hoc_tap"] == "Trung bình"])
    sv_canh_bao = len(df[df["trinh_do_hoc_tap"] == "Nguy cơ cảnh báo"])
    gpa_trung_binh = round(float(df["diem_gpa"].mean()), 2)
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "tong_sv": tong_sv,
        "sv_xuat_sac": sv_xuat_sac,
        "sv_gioi": sv_gioi,
        "sv_kha": sv_kha,
        "sv_trung_binh": sv_trung_binh,
        "sv_canh_bao": sv_canh_bao,
        "gpa_trung_binh": gpa_trung_binh
    })

@app.get("/sinh-vien", response_class=HTMLResponse)
def cong_sinh_vien(request: Request, ma_sv: str = "B24DTCN260"):
    df = tai_du_lieu()
    sv_record = df[df["ma_sinh_vien"] == ma_sv]
    if sv_record.empty:
        sv_data = df.iloc[0].to_dict()
    else:
        sv_data = sv_record.iloc[0].to_dict()
        
    ket_qua = du_doan_trinh_do(sv_data)
    
    return templates.TemplateResponse("sinh_vien.html", {
        "request": request,
        "sv": sv_data,
        "ket_qua": ket_qua,
        "danh_sach_ma_sv": df["ma_sinh_vien"].head(20).tolist()
    })

@app.get("/co-van", response_class=HTMLResponse)
def bang_dieu_khien_co_van(request: Request):
    df = tai_du_lieu()
    danh_sach_canh_bao = df[df["trinh_do_hoc_tap"].isin(["Nguy cơ cảnh báo", "Trung bình"])].to_dict(orient="records")
    toan_bo_sv = df.head(30).to_dict(orient="records")
    
    so_sv_canh_bao = len(df[df["trinh_do_hoc_tap"] == "Nguy cơ cảnh báo"])
    ty_le_canh_bao = round((so_sv_canh_bao / len(df)) * 100, 1)
    
    return templates.TemplateResponse("co_van.html", {
        "request": request,
        "toan_bo_sv": toan_bo_sv,
        "danh_sach_canh_bao": danh_sach_canh_bao,
        "tong_sv": len(df),
        "so_sv_canh_bao": so_sv_canh_bao,
        "ty_le_canh_bao": ty_le_canh_bao
    })

@app.get("/mo-hinh-clo1", response_class=HTMLResponse)
def trang_mo_hinh_clo1(request: Request):
    duong_dan_kq = "ml_engine/models/ket_qua_so_sanh.json"
    duong_dan_dg = "ml_engine/models/danh_gia_chuyen_sau.json"
    
    if not os.path.exists(duong_dan_kq):
        from ml_engine.train_models import huan_luyen_tat_ca_mo_hinh
        huan_luyen_tat_ca_mo_hinh()
        
    if not os.path.exists(duong_dan_dg):
        from ml_engine.evaluate_models import danh_gia_chuyen_sau
        danh_gia_chuyen_sau()
        
    with open(duong_dan_kq, "r", encoding="utf-8") as f:
        ket_qua_so_sanh = json.load(f)
        
    with open(duong_dan_dg, "r", encoding="utf-8") as f:
        danh_gia_chuyen_sau_data = json.load(f)
        
    return templates.TemplateResponse("mo_hinh_clo1.html", {
        "request": request,
        "so_sanh": ket_qua_so_sanh,
        "danh_gia": danh_gia_chuyen_sau_data
    })

@app.post("/api/du-doan", response_model=KetQuaDuDoan)
def api_du_doan_trinh_do(du_lieu: YeuCauDuDoanSinhVien):
    chi_so = du_lieu.model_dump()
    ket_qua = du_doan_trinh_do(chi_so)
    return {
        "ma_sinh_vien": du_lieu.ma_sinh_vien,
        "ho_ten": du_lieu.ho_ten,
        "trinh_do_du_doan": ket_qua["trinh_do_du_doan"],
        "xac_suat_du_doan": ket_qua["xac_suat_du_doan"],
        "mo_hinh_su_dung": ket_qua["mo_hinh_su_dung"],
        "nguy_co_canh_bao": ket_qua["nguy_co_canh_bao"],
        "lo_trinh": ket_qua["lo_trinh"]
    }

@app.get("/api/danh-sach-sinh-vien")
def api_lay_danh_sach_sinh_vien(limit: int = 50):
    df = tai_du_lieu()
    return df.head(limit).to_dict(orient="records")

@app.get("/api/so-sanh-mo-hinh")
def api_so_sanh_mo_hinh():
    duong_dan_kq = "ml_engine/models/ket_qua_so_sanh.json"
    if not os.path.exists(duong_dan_kq):
        from ml_engine.train_models import huan_luyen_tat_ca_mo_hinh
        huan_luyen_tat_ca_mo_hinh()
    with open(duong_dan_kq, "r", encoding="utf-8") as f:
        return json.load(f)

@app.post("/api/ghi-nhan-co-van")
def api_ghi_nhan_co_van(nhac_nho: YeuCauNhacNhoCoVan):
    return {
        "thong_bao": "Đã lưu phiếu hỗ trợ sinh viên thành công",
        "ma_sinh_vien": nhac_nho.ma_sinh_vien,
        "co_van": nhac_nho.ten_co_van,
        "hinh_thuc": nhac_nho.hinh_thuc_ho_tro,
        "trang_thai": "Đã tiếp nhận xử lý"
    }

