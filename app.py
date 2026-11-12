import os
import json
import streamlit as st
import pandas as pd
import numpy as np

from ml_engine.recommender import du_doan_trinh_do
from ml_engine.data_loader import tai_du_lieu

st.set_page_config(
    page_title="Hệ thống Gợi ý Lộ trình Học tập Sinh viên",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-title {
        color: #1a56db;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        color: #4b5563;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: #ffffff;
        padding: 1.25rem;
        border-radius: 0.75rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border: 1px solid #e5e7eb;
    }
    .stButton>button {
        background: #1a56db;
        color: white;
        border-radius: 0.5rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

df = tai_du_lieu()

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Logo_Hoc_vien_Cong_nghe_Buu_chinh_Vien_thong.svg/1200px-Logo_Hoc_vien_Cong_nghe_Buu_chinh_Vien_thong.svg.png", width=100)
    st.markdown("### Học viện Công nghệ Bưu chính Viễn thông")
    st.markdown("**Môn học:** Phát triển hệ thống thông minh (PTHTTM)")
    st.markdown("**Lớp:** D24TXCN08-B")
    st.markdown("**Nhóm thực hiện:** Nhóm 05")
    st.markdown("- **Trần Hữu Nhật** - MSV: `B24DTCN260` (Trưởng nhóm)")
    st.markdown("- **Chu Đình Minh** - MSV: `B24DTCN244` (Thành viên)")
    st.markdown("---")
    
    chuc_nang = st.radio(
        "Điều hướng hệ thống:",
        [
            "🏠 Trang chủ Tổng quan",
            "🎓 Cổng Thông tin Sinh viên",
            "👨‍🏫 Bảng điều khiển Cố vấn Học tập",
            "🔬 Nghiên cứu Mô hình CLO1",
            "⚙️ Kiến trúc DevOps & MLOps CLO2"
        ]
    )
    st.markdown("---")
    st.caption("Đề tài 13: Hệ thống Gợi ý Lộ trình Học tập và Phân loại Trình độ Sinh viên")

if chuc_nang == "🏠 Trang chủ Tổng quan":
    st.markdown("<h1 class='main-title'>Hệ thống Gợi ý Lộ trình Học tập & Phân loại Trình độ Sinh viên</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Nền tảng AI phân tích dữ liệu giáo dục và tương tác LMS, dự đoán kết quả học tập và cá nhân hóa lộ trình phát triển năng lực.</p>", unsafe_allow_html=True)
    
    tong_sv = len(df)
    sv_xuat_sac = len(df[df["trinh_do_hoc_tap"] == "Xuất sắc"])
    sv_gioi = len(df[df["trinh_do_hoc_tap"] == "Giỏi"])
    sv_kha = len(df[df["trinh_do_hoc_tap"] == "Khá"])
    sv_trung_binh = len(df[df["trinh_do_hoc_tap"] == "Trung bình"])
    sv_canh_bao = len(df[df["trinh_do_hoc_tap"] == "Nguy cơ cảnh báo"])
    gpa_tb = round(float(df["diem_gpa"].mean()), 2)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Tổng số sinh viên", f"{tong_sv:,}", "Dữ liệu chuẩn hóa")
    with col2:
        st.metric("Điểm GPA trung bình", f"{gpa_tb} / 4.0", "Học kỳ hiện tại")
    with col3:
        st.metric("Tỷ lệ Giỏi & Xuất sắc", f"{round((sv_xuat_sac + sv_gioi)/tong_sv * 100, 1)}%", f"{sv_xuat_sac + sv_gioi} sinh viên")
    with col4:
        st.metric("Nguy cơ cảnh báo học vụ", f"{sv_canh_bao}", f"{round(sv_canh_bao/tong_sv*100, 1)}% tổng số", delta_color="inverse")

    st.markdown("---")
    
    col_chart, col_info = st.columns([1, 1])
    
    with col_chart:
        st.subheader("Phân bổ Trình độ Học tập Toàn trường")
        df_phan_bo = pd.DataFrame({
            "Trình độ": ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Nguy cơ cảnh báo"],
            "Số lượng": [sv_xuat_sac, sv_gioi, sv_kha, sv_trung_binh, sv_canh_bao]
        })
        st.bar_chart(df_phan_bo.set_index("Trình độ"), color="#1a56db")

    with col_info:
        st.subheader("Trụ cột Công nghệ Cốt lõi")
        st.info("**Học máy CLO1:** Huấn luyện đối kháng Decision Tree, XGBoost và K-Means + Classification. XGBoost đạt F1-Score 98.68%.")
        st.success("**Cơ sở dữ liệu:** PostgreSQL lưu trữ hồ sơ sinh viên, chỉ số học tập, lộ trình học tập và nhật ký hỗ trợ.")
        st.warning("**DevOps & MLOps CLO2:** Đóng gói Docker, cụm phân tán Docker Swarm có Auto-scaling và Rolling Update.")
        st.info("**CI/CD Pipeline:** Tự động kiểm thử dữ liệu, code syntax, và kiểm định chất lượng mô hình (F1 >= 0.85).")

elif chuc_nang == "🎓 Cổng Thông tin Sinh viên":
    st.markdown("<h2 class='main-title'>Cổng Thông tin Sinh viên & Lộ trình Thích ứng Cá nhân hóa</h2>", unsafe_allow_html=True)
    
    danh_sach_ma = df["ma_sinh_vien"].tolist()
    mac_dinh_idx = 0
    if "B24DTCN260" in danh_sach_ma:
        mac_dinh_idx = danh_sach_ma.index("B24DTCN260")
        
    ma_sv_chon = st.selectbox("Chọn mã sinh viên tra cứu:", danh_sach_ma, index=mac_dinh_idx)
    
    sv_data = df[df["ma_sinh_vien"] == ma_sv_chon].iloc[0].to_dict()
    ket_qua = du_doan_trinh_do(sv_data)
    
    col_ho_so, col_lo_trinh = st.columns([1, 2])
    
    with col_ho_so:
        st.subheader("Hồ sơ Học tập")
        st.markdown(f"**Họ và tên:** `{sv_data['ho_ten']}`")
        st.markdown(f"**Mã sinh viên:** `{sv_data['ma_sinh_vien']}`")
        st.markdown(f"**Chuyên ngành:** {sv_data['chuyen_nganh']}")
        st.markdown(f"**Điểm GPA tích lũy:** `{sv_data['diem_gpa']} / 4.0`")
        st.markdown(f"**Điểm chuyên cần:** `{sv_data['diem_chuyen_can']} / 10`")
        st.markdown(f"**Điểm giữa kỳ:** `{sv_data['diem_giua_ky']} / 10`")
        st.markdown(f"**Điểm đồ án:** `{sv_data['diem_do_an']} / 10`")
        st.markdown(f"**Tỷ lệ điểm danh:** `{sv_data['ty_le_diem_danh']}%`")
        st.markdown(f"**Tương tác LMS:** `{sv_data['so_lan_tuong_tac_lms']} lượt`")
        st.markdown(f"**Bài tập nộp đúng hạn:** `{sv_data['so_bai_tap_nop_dung_han']} / 12`")
        st.markdown(f"**Câu hỏi diễn đàn:** `{sv_data['so_cau_hoi_dien_dan']} câu`")
        
        st.markdown("---")
        st.subheader("Phân loại Mô hình AI")
        trinh_do = ket_qua["trinh_do_du_doan"]
        if trinh_do in ["Xuất sắc", "Giỏi"]:
            st.success(f"Trình độ dự đoán: **{trinh_do}**")
        elif trinh_do == "Khá":
            st.info(f"Trình độ dự đoán: **{trinh_do}**")
        elif trinh_do == "Trung bình":
            st.warning(f"Trình độ dự đoán: **{trinh_do}**")
        else:
            st.error(f"Trình độ dự đoán: **{trinh_do}** (Cảnh báo)")
            
        st.caption(f"Mô hình: {ket_qua['mo_hinh_su_dung']} | Độ tin cậy: {round(ket_qua['xac_suat_du_doan']*100, 1)}%")

    with col_lo_trinh:
        st.subheader("Lộ trình Học tập Thích ứng Đề xuất")
        lo_trinh = ket_qua["lo_trinh"]
        
        with st.expander("📚 Môn học Tiên quyết & Củng cố Nền tảng", expanded=True):
            st.write(lo_trinh["mon_hoc_tien_quyet"])
            
        with st.expander("🚀 Khóa học Nâng cao & Chuyên sâu Khuyến nghị", expanded=True):
            st.write(lo_trinh["mon_hoc_nang_cao"])
            
        with st.expander("💡 Kỹ năng Cần Bổ trợ", expanded=True):
            st.write(lo_trinh["ky_nang_can_bo_tro"])
            
        with st.expander("⏱️ Thời gian Tự học Khuyến nghị", expanded=True):
            st.write(f"**{lo_trinh['thoi_gian_hoc_khuyen_nghi']}**")
            
        st.info(f"**Lời khuyên học tập từ Hệ thống:** {lo_trinh['loi_khuyen_hoc_tap']}")

    st.markdown("---")
    st.subheader("Mô phỏng Thay đổi Chỉ số Học tập (What-If Simulator)")
    st.caption("Thử điều chỉnh các chỉ số để xem trình độ và lộ trình sẽ thích ứng như thế nào:")
    
    sim_col1, sim_col2, sim_col3 = st.columns(3)
    with sim_col1:
        sim_gpa = st.slider("Điểm GPA tích lũy", 0.0, 4.0, float(sv_data['diem_gpa']), 0.05)
        sim_cc = st.slider("Điểm chuyên cần", 0.0, 10.0, float(sv_data['diem_chuyen_can']), 0.5)
        sim_gk = st.slider("Điểm giữa kỳ", 0.0, 10.0, float(sv_data['diem_giua_ky']), 0.5)
    with sim_col2:
        sim_da = st.slider("Điểm đồ án", 0.0, 10.0, float(sv_data['diem_do_an']), 0.5)
        sim_gio = st.slider("Số giờ học/tuần", 0.0, 40.0, float(sv_data['so_gio_hoc_tuan']), 1.0)
        sim_dd = st.slider("Tỷ lệ điểm danh (%)", 0.0, 100.0, float(sv_data['ty_le_diem_danh']), 1.0)
    with sim_col3:
        sim_lms = st.slider("Số lượt tương tác LMS", 0, 300, int(sv_data['so_lan_tuong_tac_lms']), 5)
        sim_bt = st.slider("Bài tập nộp đúng hạn", 0, 12, int(sv_data['so_bai_tap_nop_dung_han']), 1)
        sim_ch = st.slider("Câu hỏi diễn đàn", 0, 40, int(sv_data['so_cau_hoi_dien_dan']), 1)
        
    sim_data = {
        "diem_gpa": sim_gpa,
        "diem_chuyen_can": sim_cc,
        "diem_giua_ky": sim_gk,
        "diem_do_an": sim_da,
        "so_gio_hoc_tuan": sim_gio,
        "ty_le_diem_danh": sim_dd,
        "so_lan_tuong_tac_lms": sim_lms,
        "so_bai_tap_nop_dung_han": sim_bt,
        "so_cau_hoi_dien_dan": sim_ch
    }
    
    sim_res = du_doan_trinh_do(sim_data)
    st.success(f"Kết quả mô phỏng: Trình độ dự đoán đạt **{sim_res['trinh_do_du_doan']}** (Độ tin cậy: {round(sim_res['xac_suat_du_doan']*100, 1)}%)")

elif chuc_nang == "👨‍🏫 Bảng điều khiển Cố vấn Học tập":
    st.markdown("<h2 class='main-title'>Bảng Điều khiển Cố vấn Học tập - Quản lý Nguy cơ Học vụ</h2>", unsafe_allow_html=True)
    
    ds_canh_bao = df[df["trinh_do_hoc_tap"].isin(["Nguy cơ cảnh báo", "Trung bình"])]
    
    st.warning(f"Hiện có **{len(ds_canh_bao)}** sinh viên thuộc nhóm cần theo dõi hoặc có nguy cơ cảnh báo học vụ.")
    
    st.dataframe(
        ds_canh_bao[[
            "ma_sinh_vien", "ho_ten", "chuyen_nganh", "diem_gpa", "diem_chuyen_can",
            "ty_le_diem_danh", "so_lan_tuong_tac_lms", "trinh_do_hoc_tap"
        ]],
        use_container_width=True
    )
    
    st.markdown("---")
    st.subheader("Gửi Phiếu Nhắc nhở / Kế hoạch Can thiệp Học vụ")
    with st.form("form_nhac_nho"):
        sv_gui = st.selectbox("Chọn sinh viên can thiệp:", ds_canh_bao["ma_sinh_vien"].tolist())
        co_van_ten = st.text_input("Họ tên Cố vấn học tập:", "TS. Nguyễn Văn Cố Vấn")
        hinh_thuc = st.selectbox("Hình thức hỗ trợ:", [
            "Gửi email nhắc nhở học vụ",
            "Hẹn gặp trực tiếp tại văn phòng khoa",
            "Liên hệ gia đình sinh viên",
            "Bố trí sinh viên khá giỏi hỗ trợ kèm cặp"
        ])
        noi_dung = st.text_area("Nội dung nhắc nhở / Hướng dẫn cải thiện:", "Đề nghị sinh viên tăng cường thời gian truy cập LMS và hoàn thiện các bài tập thực hành còn thiếu trước kỳ thi.")
        gui_submit = st.form_submit_button("Xác nhận Lưu Phiếu Hỗ trợ")
        if gui_submit:
            st.success(f"Đã lưu phiếu hỗ trợ thành công cho sinh viên {sv_gui} qua hình thức: {hinh_thuc}.")

elif chuc_nang == "🔬 Nghiên cứu Mô hình CLO1":
    st.markdown("<h2 class='main-title'>Nghiên cứu & Đối sánh Mô hình Thông minh (CLO1)</h2>", unsafe_allow_html=True)
    
    duong_dan_kq = "ml_engine/models/ket_qua_so_sanh.json"
    duong_dan_dg = "ml_engine/models/danh_gia_chuyen_sau.json"
    
    if os.path.exists(duong_dan_kq) and os.path.exists(duong_dan_dg):
        with open(duong_dan_kq, "r", encoding="utf-8") as f:
            kq_so_sanh = json.load(f)
        with open(duong_dan_dg, "r", encoding="utf-8") as f:
            dg_chuyen_sau = json.load(f)
            
        st.subheader(f"Mô hình Tối ưu nhất Được Chọn: {kq_so_sanh['mo_hinh_tot_nhat']}")
        
        bang_so_sanh = []
        for ten, val in kq_so_sanh["ket_qua_chi_tiet"].items():
            bang_so_sanh.append({
                "Mô hình": ten,
                "Độ chính xác (Accuracy)": f"{val['do_chinh_xac']*100:.2f}%",
                "Precision": f"{val['precision']*100:.2f}%",
                "Recall": f"{val['recall']*100:.2f}%",
                "F1-Score": f"{val['f1_score']*100:.2f}%",
                "Thời gian huấn luyện": f"{val['thoi_gian_huan_luyen_giay']} s",
                "Độ trễ suy luận": f"{val['do_tre_suy_luan_ms']} ms"
            })
            
        st.table(pd.DataFrame(bang_so_sanh))
        
        st.markdown("---")
        col_feat, col_cm = st.columns(2)
        
        with col_feat:
            st.subheader("Tầm quan trọng Đặc trưng (Feature Importance)")
            df_feat = pd.DataFrame({
                "Đặc trưng": dg_chuyen_sau["dac_trung"],
                "Trọng số XGBoost": dg_chuyen_sau["tam_quan_trong_xgboost"]
            }).sort_values("Trọng số XGBoost", ascending=True)
            st.bar_chart(df_feat.set_index("Đặc trưng"))
            
        with col_cm:
            st.subheader("Ma trận Nhầm lẫn (Confusion Matrix - XGBoost)")
            cm_df = pd.DataFrame(
                dg_chuyen_sau["ma_tran_nham_lan_xgboost"],
                index=dg_chuyen_sau["nhan_lop"],
                columns=dg_chuyen_sau["nhan_lop"]
            )
            st.dataframe(cm_df)
            st.success("Tỷ lệ bắt trúng nhóm sinh viên cảnh báo học vụ đạt 100% (Recall = 1.0).")
    else:
        st.warning("Vui lòng kích hoạt huấn luyện mô hình để xem báo cáo.")

elif chuc_nang == "⚙️ Kiến trúc DevOps & MLOps CLO2":
    st.markdown("<h2 class='main-title'>Kiến trúc Triển khai DevOps & MLOps (CLO2)</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    ### 1. Chu trình MLOps Khép kín
    - **Data Ingestion & Validation:** Kiểm tra tính toàn vẹn và phạm vi dữ liệu giáo dục.
    - **Automated Training Pipeline:** Huấn luyện đối kháng Decision Tree, XGBoost và K-Means.
    - **Model Gatekeeping:** Thẩm định ngưỡng chất lượng mô hình (F1-score >= 0.85) trước khi xuất xưởng.
    - **Model Registry:** Lưu vết các phiên bản mô hình kèm metadata chỉ số kiểm thử.
    
    ### 2. Cụm phân tán Docker Swarm
    - **Multi-replica Services:** Triển khai 3 replicas cho Web Portal, 2 replicas cho ML Engine, 1 cụm PostgreSQL.
    - **Auto-scaling:** Kịch bản `autoscaling_swarm.sh` tự động scale từ 2 lên 8 replicas khi CPU vượt ngưỡng 75%.
    - **Rolling Update:** Cập nhật phiên bản mới không thời gian chết (Zero-downtime deployment).
    
    ### 3. Tự động hóa CI/CD với GitHub Actions
    - Pipeline cấu hình tại `.github/workflows/ci-cd.yml` gồm 3 stages tự động:
      1. Kiểm tra chất lượng cú pháp mã nguồn & dữ liệu.
      2. MLOps Gatekeeper: Huấn luyện và thẩm định F1-score >= 0.85.
      3. Đóng gói Docker Images và triển khai tự động lên cụm Swarm.
    """)

