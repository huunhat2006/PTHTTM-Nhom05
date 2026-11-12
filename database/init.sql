CREATE TABLE IF NOT EXISTS sinh_vien (
    ma_sinh_vien VARCHAR(20) PRIMARY KEY,
    ho_ten VARCHAR(100) NOT NULL,
    gioi_tinh VARCHAR(10) NOT NULL,
    ngay_sinh DATE NOT NULL,
    chuyen_nganh VARCHAR(100) NOT NULL,
    khoa_hoc VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    trang_thai VARCHAR(50) DEFAULT 'Đang học'
);

CREATE TABLE IF NOT EXISTS chi_so_hoc_tap (
    id SERIAL PRIMARY KEY,
    ma_sinh_vien VARCHAR(20) REFERENCES sinh_vien(ma_sinh_vien) ON DELETE CASCADE,
    hoc_ky VARCHAR(20) NOT NULL,
    diem_gpa NUMERIC(4, 2) NOT NULL,
    diem_chuyen_can NUMERIC(4, 2) NOT NULL,
    diem_giua_ky NUMERIC(4, 2) NOT NULL,
    diem_do_an NUMERIC(4, 2) NOT NULL,
    so_gio_hoc_tuan NUMERIC(5, 1) NOT NULL,
    ty_le_diem_danh NUMERIC(5, 2) NOT NULL,
    so_lan_tuong_tac_lms INTEGER NOT NULL,
    so_bai_tap_nop_dung_han INTEGER NOT NULL,
    so_cau_hoi_dien_dan INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS phan_loai_trinh_do (
    id SERIAL PRIMARY KEY,
    ma_sinh_vien VARCHAR(20) REFERENCES sinh_vien(ma_sinh_vien) ON DELETE CASCADE,
    trinh_do_du_doan VARCHAR(50) NOT NULL,
    xac_suat_du_doan NUMERIC(5, 4) NOT NULL,
    mo_hinh_su_dung VARCHAR(50) NOT NULL,
    nguy_co_canh_bao VARCHAR(50) NOT NULL,
    thoi_gian_du_doan TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lo_trinh_hoc_tap (
    id SERIAL PRIMARY KEY,
    ma_sinh_vien VARCHAR(20) REFERENCES sinh_vien(ma_sinh_vien) ON DELETE CASCADE,
    hoc_ky_ap_dung VARCHAR(20) NOT NULL,
    mon_hoc_tien_quyet TEXT NOT NULL,
    mon_hoc_nang_cao TEXT NOT NULL,
    ky_nang_can_bo_tro TEXT NOT NULL,
    thoi_gian_hoc_khuyen_nghi VARCHAR(50) NOT NULL,
    loi_khuyen_hoc_tap TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS nhat_ky_co_van (
    id SERIAL PRIMARY KEY,
    ma_sinh_vien VARCHAR(20) REFERENCES sinh_vien(ma_sinh_vien) ON DELETE CASCADE,
    ten_co_van VARCHAR(100) NOT NULL,
    noi_dung_nhac_nho TEXT NOT NULL,
    hinh_thuc_ho_tro VARCHAR(100) NOT NULL,
    ngay_ghi_nhan TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO sinh_vien (ma_sinh_vien, ho_ten, gioi_tinh, ngay_sinh, chuyen_nganh, khoa_hoc, email, trang_thai) VALUES
('B24DTCN260', 'Trần Hữu Nhật', 'Nam', '2003-05-15', 'Công nghệ thông tin', 'D24TXCN08-B', 'nhat.th@ptit.edu.vn', 'Đang học'),
('B24DTCN244', 'Chu Đình Minh', 'Nam', '2003-08-22', 'Công nghệ thông tin', 'D24TXCN08-B', 'minh.cd@ptit.edu.vn', 'Đang học'),
('B21DCCN003', 'Lê Hoàng Cường', 'Nam', '2003-11-09', 'An toàn thông tin', 'D24TXCN08-B', 'cuong.lh@ptit.edu.vn', 'Đang học'),
('B21DCCN004', 'Phạm Minh Dũng', 'Nam', '2003-02-18', 'Khoa học máy tính', 'D24TXCN08-B', 'dung.pm@ptit.edu.vn', 'Đang học'),
('B21DCCN005', 'Vũ Thị Hoa', 'Nữ', '2003-07-30', 'Hệ thống thông tin', 'D24TXCN08-B', 'hoa.vt@ptit.edu.vn', 'Đang học'),
('B21DCCN006', 'Đỗ Quốc Hùng', 'Nam', '2003-01-25', 'Công nghệ thông tin', 'D24TXCN08-B', 'hung.dq@ptit.edu.vn', 'Cảnh báo học vụ'),
('B21DCCN007', 'Hoàng Thu Linh', 'Nữ', '2003-09-12', 'Khoa học máy tính', 'D24TXCN08-B', 'linh.ht@ptit.edu.vn', 'Đang học'),
('B21DCCN008', 'Ngô Quang Nam', 'Nam', '2003-04-05', 'An toàn thông tin', 'D24TXCN08-B', 'nam.nq@ptit.edu.vn', 'Đang học'),
('B21DCCN009', 'Đặng Thảo Nguyên', 'Nữ', '2003-12-19', 'Hệ thống thông tin', 'D24TXCN08-B', 'nguyen.dt@ptit.edu.vn', 'Đang học'),
('B21DCCN010', 'Bùi Anh Tuấn', 'Nam', '2003-06-08', 'Công nghệ thông tin', 'D24TXCN08-B', 'tuan.ba@ptit.edu.vn', 'Cảnh báo học vụ')
ON CONFLICT (ma_sinh_vien) DO NOTHING;

INSERT INTO chi_so_hoc_tap (ma_sinh_vien, hoc_ky, diem_gpa, diem_chuyen_can, diem_giua_ky, diem_do_an, so_gio_hoc_tuan, ty_le_diem_danh, so_lan_tuong_tac_lms, so_bai_tap_nop_dung_han, so_cau_hoi_dien_dan) VALUES
('B24DTCN260', 'Kỳ 1 Năm 4', 3.85, 9.8, 9.5, 9.6, 30.0, 98.5, 210, 12, 22),
('B24DTCN244', 'Kỳ 1 Năm 4', 3.72, 9.5, 9.2, 9.4, 28.0, 96.0, 195, 12, 18),
('B21DCCN003', 'Kỳ 1 Năm 4', 2.85, 7.5, 7.0, 7.2, 14.5, 85.0, 88, 8, 5),
('B21DCCN004', 'Kỳ 1 Năm 4', 3.88, 10.0, 9.5, 9.7, 32.0, 100.0, 210, 12, 25),
('B21DCCN005', 'Kỳ 1 Năm 4', 3.15, 8.0, 8.0, 7.8, 18.0, 90.0, 115, 10, 8),
('B21DCCN006', 'Kỳ 1 Năm 4', 1.82, 5.0, 4.5, 4.0, 6.0, 62.0, 32, 4, 1),
('B21DCCN007', 'Kỳ 1 Năm 4', 3.60, 9.2, 8.8, 8.9, 25.0, 96.0, 168, 12, 15),
('B21DCCN008', 'Kỳ 1 Năm 4', 2.65, 7.0, 6.5, 6.8, 12.0, 80.0, 75, 7, 3),
('B21DCCN009', 'Kỳ 1 Năm 4', 3.30, 8.5, 8.2, 8.0, 20.0, 92.0, 130, 10, 9),
('B21DCCN010', 'Kỳ 1 Năm 4', 1.65, 4.5, 3.8, 4.2, 5.0, 58.0, 28, 3, 0);

INSERT INTO phan_loai_trinh_do (ma_sinh_vien, trinh_do_du_doan, xac_suat_du_doan, mo_hinh_su_dung, nguy_co_canh_bao) VALUES
('B24DTCN260', 'Xuất sắc', 0.9850, 'XGBoost', 'Không có nguy cơ'),
('B24DTCN244', 'Xuất sắc', 0.9620, 'XGBoost', 'Không có nguy cơ'),
('B21DCCN003', 'Khá', 0.8870, 'XGBoost', 'Cần theo dõi'),
('B21DCCN004', 'Xuất sắc', 0.9780, 'XGBoost', 'Không có nguy cơ'),
('B21DCCN005', 'Khá', 0.8920, 'XGBoost', 'Không có nguy cơ'),
('B21DCCN006', 'Nguy cơ cảnh báo', 0.9630, 'XGBoost', 'Nguy cơ cao - Cần can thiệp gấp'),
('B21DCCN007', 'Giỏi', 0.9340, 'XGBoost', 'Không có nguy cơ'),
('B21DCCN008', 'Trung bình', 0.8750, 'XGBoost', 'Cần theo dõi'),
('B21DCCN009', 'Khá', 0.9010, 'XGBoost', 'Không có nguy cơ'),
('B21DCCN010', 'Nguy cơ cảnh báo', 0.9820, 'XGBoost', 'Nguy cơ rất cao - Báo cáo cố vấn');

INSERT INTO lo_trinh_hoc_tap (ma_sinh_vien, hoc_ky_ap_dung, mon_hoc_tien_quyet, mon_hoc_nang_cao, ky_nang_can_bo_tro, thoi_gian_hoc_khuyen_nghi, loi_khuyen_hoc_tap) VALUES
('B24DTCN260', 'Kỳ 2 Năm 4', 'Kiến trúc máy tính, Hệ điều hành', 'Học sâu ứng dụng, MLOps nâng cao, Điện toán đám mây', 'Nghiên cứu khoa học, Thiết kế hệ thống lớn', '28-32 giờ/tuần', 'Duy trì phong độ học tập xuất sắc, định hướng phát triển đồ án tốt nghiệp chuyên sâu MLOps và chuẩn bị hồ sơ du học/học bổng.'),
('B24DTCN244', 'Kỳ 2 Năm 4', 'Cơ sở dữ liệu, Lập trình Web', 'Kiến trúc vi dịch vụ, Tối ưu hóa cơ sở dữ liệu lớn, Docker Swarm', 'Kỹ năng quản trị hệ thống phân tán, DevOps', '25-30 giờ/tuần', 'Năng lực kỹ thuật rất vững vàng, khuyến khích triển khai các dự án quy mô lớn cho doanh nghiệp.'),
('B21DCCN003', 'Kỳ 2 Năm 4', 'Cấu trúc dữ liệu và giải thuật', 'An toàn mạng máy tính, Quản trị hệ thống Linux', 'Kỹ năng giải quyết vấn đề, Tự học công nghệ mới', '18-22 giờ/tuần', 'Tăng cường thời gian tự học trên hệ thống LMS, chủ động hoàn thành bài tập sớm hơn thời hạn để củng cố điểm số.'),
('B21DCCN004', 'Kỳ 2 Năm 4', 'Toán rời rạc, Trí tuệ nhân tạo', 'Mô hình ngôn ngữ lớn (LLM), Xử lý ngôn ngữ tự nhiên', 'Thuyết trình kỹ thuật, Quản lý dự án AI', '28-32 giờ/tuần', 'Sinh viên có năng lực vượt trội, khuyến khích tham gia nhóm nghiên cứu LAB AI của trường.'),
('B21DCCN005', 'Kỳ 2 Năm 4', 'Phân tích thiết kế hệ thống', 'Phân tích dữ liệu doanh nghiệp, ERP hiện đại', 'Trực quan hóa dữ liệu với PowerBI', '18-20 giờ/tuần', 'Phát huy thế mạnh phân tích nghiệp vụ, tham gia thực tập sớm tại các doanh nghiệp đối tác.'),
('B21DCCN006', 'Kỳ 2 Năm 4', 'Nhập môn lập trình, Toán cao cấp', 'Lập trình hướng đối tượng, Mạng máy tính cơ bản', 'Phương pháp quản lý thời gian, Kỹ năng tự học', '15-18 giờ/tuần', 'Cần gặp trực tiếp cố vấn học tập để xây dựng kế hoạch trả nợ môn, tham gia lớp phụ đạo tăng cường và tăng tỷ lệ chuyên cần.'),
('B21DCCN007', 'Kỳ 2 Năm 4', 'Học máy cơ bản, Đại số tuyến tính', 'Thị giác máy tính, Xử lý ảnh nâng cao', 'Lập trình Python nâng cao, PyTorch', '22-26 giờ/tuần', 'Rất có tiềm năng phát triển mảng AI/CV, nên đăng ký đồ án tốt nghiệp với giảng viên chuyên ngành.'),
('B21DCCN008', 'Kỳ 2 Năm 4', 'Mạng máy tính, Hệ quản trị CSDL', 'Kiểm thử bảo mật Web, Phân tích mã độc', 'Thực hành phòng thủ mạng trên máy ảo', '16-20 giờ/tuần', 'Cần chủ động đặt câu hỏi trên diễn đàn học tập, tăng thời lượng truy cập tài liệu bài giảng trực tuyến.'),
('B21DCCN009', 'Kỳ 2 Năm 4', 'Quản trị dự án CNTT', 'Phát triển ứng dụng Web tiến tiến', 'Kỹ năng giao tiếp, Tiếng Anh chuyên ngành', '18-22 giờ/tuần', 'Tích cực tham gia các buổi báo cáo chuyên đề và mở rộng kỹ năng lập trình full-stack.'),
('B21DCCN010', 'Kỳ 2 Năm 4', 'Cơ sở dữ liệu, Kiến trúc máy tính', 'Lập trình ứng dụng căn bản', 'Kỷ luật học tập, Kỹ năng làm bài kiểm tra', '15-20 giờ/tuần', 'Cố vấn học tập sẽ liên hệ với phụ huynh và bố trí sinh viên khá giỏi kèm cặp 1-1 để cải thiện kết quả học tập.');

INSERT INTO nhat_ky_co_van (ma_sinh_vien, ten_co_van, noi_dung_nhac_nho, hinh_thuc_ho_tro) VALUES
('B21DCCN006', 'TS. Nguyễn Văn Cố Vấn', 'Đã hẹn gặp sinh viên tư vấn học vụ. Sinh viên cam kết đi học chuyên cần và hoàn thành đủ bài tập thực hành tuần.', 'Gặp trực tiếp tại văn phòng khoa'),
('B21DCCN010', 'TS. Nguyễn Văn Cố Vấn', 'Cảnh báo tình trạng vắng quá số buổi quy định. Đã gửi email nhắc nhở và thông báo gia đình hỗ trợ đôn đốc.', 'Gửi email và gọi điện thoại');
