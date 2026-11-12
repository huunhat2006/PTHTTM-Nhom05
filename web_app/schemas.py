from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class YeuCauDuDoanSinhVien(BaseModel):
    ma_sinh_vien: str = Field(..., description="Mã sinh viên")
    ho_ten: str = Field(..., description="Họ và tên")
    chuyen_nganh: str = Field(..., description="Chuyên ngành đào tạo")
    diem_gpa: float = Field(..., ge=0.0, le=4.0, description="Điểm trung bình tích lũy GPA")
    diem_chuyen_can: float = Field(..., ge=0.0, le=10.0, description="Điểm chuyên cần")
    diem_giua_ky: float = Field(..., ge=0.0, le=10.0, description="Điểm kiểm tra giữa kỳ")
    diem_do_an: float = Field(..., ge=0.0, le=10.0, description="Điểm bài tập lớn hoặc đồ án")
    so_gio_hoc_tuan: float = Field(..., ge=0.0, description="Số giờ tự học mỗi tuần")
    ty_le_diem_danh: float = Field(..., ge=0.0, le=100.0, description="Tỷ lệ tham gia điểm danh (%)")
    so_lan_tuong_tac_lms: int = Field(..., ge=0, description="Số lần truy cập tương tác LMS")
    so_bai_tap_nop_dung_han: int = Field(..., ge=0, description="Số bài tập nộp đúng hạn")
    so_cau_hoi_dien_dan: int = Field(..., ge=0, description="Số câu hỏi trao đổi trên diễn đàn")

class ChiTietLoTrinh(BaseModel):
    mon_hoc_tien_quyet: str
    mon_hoc_nang_cao: str
    ky_nang_can_bo_tro: str
    thoi_gian_hoc_khuyen_nghi: str
    loi_khuyen_hoc_tap: str

class KetQuaDuDoan(BaseModel):
    ma_sinh_vien: str
    ho_ten: str
    trinh_do_du_doan: str
    xac_suat_du_doan: float
    mo_hinh_su_dung: str
    nguy_co_canh_bao: str
    lo_trinh: ChiTietLoTrinh

class YeuCauNhacNhoCoVan(BaseModel):
    ma_sinh_vien: str
    ten_co_van: str
    noi_dung_nhac_nho: str
    hinh_thuc_ho_tro: str

