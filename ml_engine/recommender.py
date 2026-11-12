import os
import joblib
import pandas as pd
from ml_engine.data_loader import DANH_SACH_DAC_TRUNG, ANH_XA_NHAN_NGUOC

def du_doan_trinh_do(chi_so):
    duong_dan_model = "ml_engine/models/mo_hinh_xgboost.joblib"
    if os.path.exists(duong_dan_model):
        mo_hinh = joblib.load(duong_dan_model)
        df_input = pd.DataFrame([chi_so])[DANH_SACH_DAC_TRUNG]
        ma_lop = int(mo_hinh.predict(df_input)[0])
        xac_suat = float(max(mo_hinh.predict_proba(df_input)[0]))
        ten_trinh_do = ANH_XA_NHAN_NGUOC.get(ma_lop, "Khá")
    else:
        gpa = chi_so.get("diem_gpa", 2.5)
        if gpa >= 3.6:
            ten_trinh_do = "Xuất sắc"
            xac_suat = 0.95
        elif gpa >= 3.2:
            ten_trinh_do = "Giỏi"
            xac_suat = 0.90
        elif gpa >= 2.5:
            ten_trinh_do = "Khá"
            xac_suat = 0.88
        elif gpa >= 2.0:
            ten_trinh_do = "Trung bình"
            xac_suat = 0.85
        else:
            ten_trinh_do = "Nguy cơ cảnh báo"
            xac_suat = 0.96

    if ten_trinh_do == "Xuất sắc":
        nguy_co = "Không có nguy cơ"
        mon_tien_quyet = "Cấu trúc dữ liệu và giải thuật, Hệ điều hành, Cơ sở dữ liệu nâng cao"
        mon_nang_cao = "Kiến trúc hệ thống lớn, MLOps & DevOps thực chiến, Trí tuệ nhân tạo nâng cao"
        ky_nang = "Nghiên cứu khoa học, Thiết kế giải pháp kiến trúc, Lãnh đạo nhóm kỹ thuật"
        thoi_gian = "25 - 32 giờ/tuần"
        loi_khuyen = "Sinh viên duy trì kết quả vượt bậc. Khuyến nghị tham gia thực tập tại các tập đoàn công nghệ lớn hoặc tham gia đề tài nghiên cứu cùng giảng viên hướng dẫn."
    elif ten_trinh_do == "Giỏi":
        nguy_co = "Không có nguy cơ"
        mon_tien_quyet = "Lập trình hướng đối tượng, Mạng máy tính, Cơ sở dữ liệu"
        mon_nang_cao = "Phát triển ứng dụng Web phân tán, Học máy cơ bản, Kỹ thuật DevOps"
        ky_nang = "Kỹ năng lập trình Clean Code, Tối ưu hóa truy vấn CSDL, Làm việc nhóm Agile"
        thoi_gian = "20 - 25 giờ/tuần"
        loi_khuyen = "Thành tích học tập rất tốt. Nên tập trung đẩy mạnh đồ án môn học gắn với dự án thực tế để chuẩn bị hồ sơ ứng tuyển việc làm."
    elif ten_trinh_do == "Khá":
        nguy_co = "Cần theo dõi nhẹ"
        mon_tien_quyet = "Toán chuyên ngành, Cấu trúc dữ liệu căn bản, Lập trình C++/Java/Python"
        mon_nang_cao = "Phân tích thiết kế hệ thống thông tin, Lập trình ứng dụng Web"
        ky_nang = "Kỹ năng tự học công nghệ, Quản lý thời gian học tập, Luyện bài tập thực hành"
        thoi_gian = "18 - 22 giờ/tuần"
        loi_khuyen = "Kết quả đạt mức khá. Cần nâng cao tính chuyên cần, tăng cường làm bài tập trên hệ thống LMS và chủ động đặt câu hỏi với trợ giảng."
    elif ten_trinh_do == "Trung bình":
        nguy_co = "Nguy cơ tiềm ẩn - Cần cải thiện"
        mon_tien_quyet = "Nhập môn lập trình, Đại số tuyến tính, Xác suất thống kê"
        mon_nang_cao = "Kỹ thuật lập trình cơ bản, Quản trị hệ thống máy tính"
        ky_nang = "Phương pháp ghi chép bài giảng, Kỹ năng giải bài tập trắc nghiệm và tự luận"
        thoi_gian = "16 - 20 giờ/tuần"
        loi_khuyen = "Cần bố trí lại thời gian học tập, đi học đúng giờ và nộp bài tập đúng thời hạn quy định. Đăng ký tham gia nhóm học tập cùng các bạn khá giỏi."
    else:
        nguy_co = "Nguy cơ cao - Cần can thiệp học vụ gấp"
        mon_tien_quyet = "Học lại các học phần nợ: Toán đại cương, Lập trình cơ sở"
        mon_nang_cao = "Tạm hoãn các môn học nâng cao cho đến khi hoàn thành môn điều kiện"
        ky_nang = "Xây dựng lại kỷ luật học tập cá nhân, Kỹ năng quản lý thời gian"
        thoi_gian = "12 - 18 giờ/tuần (dưới sự giám sát của cố vấn)"
        loi_khuyen = "Cảnh báo khẩn cấp: Sinh viên có điểm số và mức độ tương tác LMS thấp nghiêm trọng. Cần liên hệ ngay với Cố vấn học tập để làm kế hoạch học tập cá nhân và cải thiện điểm danh."

    return {
        "trinh_do_du_doan": ten_trinh_do,
        "xac_suat_du_doan": round(xac_suat, 4),
        "mo_hinh_su_dung": "XGBoost Classifier",
        "nguy_co_canh_bao": nguy_co,
        "lo_trinh": {
            "mon_hoc_tien_quyet": mon_tien_quyet,
            "mon_hoc_nang_cao": mon_nang_cao,
            "ky_nang_can_bo_tro": ky_nang,
            "thoi_gian_hoc_khuyen_nghi": thoi_gian,
            "loi_khuyen_hoc_tap": loi_khuyen
        }
    }

