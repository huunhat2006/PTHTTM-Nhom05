import openpyxl
from datetime import datetime

wb = openpyxl.load_workbook('Project_Work Breakdown Structure.xlsx')
ws = wb.active

ws.cell(8, 5, 'Nhóm 05 - Lớp D24TXCN08-B - Học viện Công nghệ Bưu chính Viễn thông')
ws.cell(9, 5, 'Hệ thống Gợi ý Lộ trình Học tập và Phân loại Trình độ Sinh viên (AI-Powered Adaptive Learning & Student Performance Prediction)')

danh_sach_cong_viec = [
    (14, '1. Khởi tạo dự án & Quản lý', None, None, None, datetime(2026, 9, 5), datetime(2026, 9, 18), 'Trần Hữu Nhật (B24DTCN260)', 'Tài liệu Kế hoạch & Kiến trúc', 'Done'),
    (15, None, '1.1. Lập Kế hoạch hành động (Action Plan) & WBS', None, None, datetime(2026, 9, 5), datetime(2026, 9, 10), 'Trần Hữu Nhật (B24DTCN260)', 'Project_Action Plan.docx', 'Done'),
    (16, None, '1.2. Khảo sát nghiệp vụ & Phân tích yêu cầu (SRS)', None, None, datetime(2026, 9, 11), datetime(2026, 9, 15), 'Chu Đình Minh (B24DTCN244)', 'Tài liệu Đặc tả Yêu cầu', 'Done'),
    (17, None, '1.3. Thiết kế kiến trúc tổng thể DevOps & MLOps', None, None, datetime(2026, 9, 15), datetime(2026, 9, 18), 'Trần Hữu Nhật (B24DTCN260)', 'Sơ đồ Kiến trúc Hệ thống', 'Done'),
    (18, '2. Dữ liệu giáo dục & Cơ sở dữ liệu', None, None, None, datetime(2026, 9, 19), datetime(2026, 10, 2), 'Chu Đình Minh (B24DTCN244)', 'Bộ CSDL & Dataset chuẩn hóa', 'Done'),
    (19, None, '2.1. Thiết kế lược đồ CSDL PostgreSQL', None, None, datetime(2026, 9, 19), datetime(2026, 9, 23), 'Chu Đình Minh (B24DTCN244)', 'init.sql, db_connection.py', 'Done'),
    (20, None, '2.2. Thu thập & Sinh 1500 mẫu dữ liệu giáo dục', None, None, datetime(2026, 9, 24), datetime(2026, 9, 28), 'Chu Đình Minh (B24DTCN244)', 'generate_data.py, CSV files', 'Done'),
    (21, None, '2.3. Tiền xử lý, chuẩn hóa & Phân tích khám phá EDA', None, None, datetime(2026, 9, 29), datetime(2026, 10, 2), 'Trần Hữu Nhật (B24DTCN260)', 'data_loader.py & Báo cáo EDA', 'Done'),
    (22, '3. Nghiên cứu Mô hình Thông minh CLO1', None, None, None, datetime(2026, 10, 3), datetime(2026, 10, 23), 'Trần Hữu Nhật (B24DTCN260)', 'Mô hình ML & Động cơ Gợi ý', 'Done'),
    (23, None, '3.1. Xây dựng mô hình Decision Tree Classifier', None, None, datetime(2026, 10, 3), datetime(2026, 10, 7), 'Trần Hữu Nhật (B24DTCN260)', 'mo_hinh_decision_tree.joblib', 'Done'),
    (24, None, '3.2. Xây dựng mô hình XGBoost Classifier', None, None, datetime(2026, 10, 8), datetime(2026, 10, 13), 'Trần Hữu Nhật (B24DTCN260)', 'mo_hinh_xgboost.joblib', 'Done'),
    (25, None, '3.3. Xây dựng mô hình K-Means + Phân loại', None, None, datetime(2026, 10, 14), datetime(2026, 10, 18), 'Trần Hữu Nhật (B24DTCN260)', 'mo_hinh_kmeans_classifier.joblib', 'Done'),
    (26, None, '3.4. Đánh giá đối sánh chỉ số, Ma trận nhầm lẫn', None, None, datetime(2026, 10, 19), datetime(2026, 10, 21), 'Trần Hữu Nhật (B24DTCN260)', 'ket_qua_so_sanh.json', 'Done'),
    (27, None, '3.5. Xây dựng Động cơ Gợi ý Lộ trình thích ứng', None, None, datetime(2026, 10, 21), datetime(2026, 10, 23), 'Trần Hữu Nhật (B24DTCN260)', 'recommender.py', 'Done'),
    (28, '4. Web Portal & Hạ tầng Docker Swarm CLO2', None, None, None, datetime(2026, 10, 24), datetime(2026, 11, 10), 'Chu Đình Minh (B24DTCN244)', 'Web Portal & Swarm Cluster', 'Done'),
    (29, None, '4.1. Xây dựng Backend FastAPI & RESTful API', None, None, datetime(2026, 10, 24), datetime(2026, 10, 28), 'Chu Đình Minh (B24DTCN244)', 'main.py, schemas.py', 'Done'),
    (30, None, '4.2. Phát triển Cổng sinh viên & Dashboard cố vấn', None, None, datetime(2026, 10, 29), datetime(2026, 11, 4), 'Chu Đình Minh (B24DTCN244)', 'templates/*.html, app.js', 'Done'),
    (31, None, '4.3. Đóng gói Dockerfile Web & ML Pipeline', None, None, datetime(2026, 11, 5), datetime(2026, 11, 7), 'Chu Đình Minh (B24DTCN244)', 'Dockerfile.web, Dockerfile.ml', 'Done'),
    (32, None, '4.4. Cấu hình Docker Swarm Stack & Auto-scaling', None, None, datetime(2026, 11, 8), datetime(2026, 11, 10), 'Chu Đình Minh (B24DTCN244)', 'docker-stack.yml, autoscaling_swarm.sh', 'Done'),
    (33, '5. Quy trình CI/CD & Nghiệm thu Tổng kết', None, None, None, datetime(2026, 11, 11), datetime(2026, 11, 25), 'Trần Hữu Nhật (B24DTCN260)', 'CI/CD Pipeline & Bộ Báo cáo', 'Done'),
    (34, None, '5.1. Thiết lập GitHub Actions CI/CD Pipeline', None, None, datetime(2026, 11, 11), datetime(2026, 11, 14), 'Chu Đình Minh (B24DTCN244)', 'ci-cd.yml', 'Done'),
    (35, None, '5.2. Cấu hình Model Gatekeeper (F1 >= 0.85)', None, None, datetime(2026, 11, 15), datetime(2026, 11, 17), 'Trần Hữu Nhật (B24DTCN260)', 'Kiểm tra Ngưỡng Gatekeeper', 'Done'),
    (36, None, '5.3. Kiểm thử tải & Kiểm thử tích hợp toàn diện', None, None, datetime(2026, 11, 18), datetime(2026, 11, 20), 'Trần Hữu Nhật, Chu Đình Minh', 'Kịch bản kiểm thử & Log Swarm', 'Done'),
    (37, None, '5.4. Hoàn thiện Bộ 3 Báo cáo Kỹ thuật môn học', None, None, datetime(2026, 11, 21), datetime(2026, 11, 25), 'Trần Hữu Nhật, Chu Đình Minh', 'Bộ 3 Báo cáo Kỹ thuật', 'Done')
]

for row_idx, t1, t2, t3, t4, s_date, e_date, resp, deliv, status in danh_sach_cong_viec:
    ws.cell(row_idx, 2, t1)
    ws.cell(row_idx, 3, t2)
    ws.cell(row_idx, 4, t3)
    ws.cell(row_idx, 5, t4)
    ws.cell(row_idx, 6, s_date)
    ws.cell(row_idx, 7, e_date)
    ws.cell(row_idx, 8, resp)
    ws.cell(row_idx, 9, deliv)
    ws.cell(row_idx, 10, status)

for r in range(38, 46):
    for c in range(2, 11):
        if c == 10:
            ws.cell(r, c, None)

wb.save('Project_Work Breakdown Structure.xlsx')
print('WBS updated successfully with B24DTCN260 & B24DTCN244 and D24TXCN08-B!')
