# HỆ THỐNG GỢI Ý LỘ TRÌNH HỌC TẬP VÀ PHÂN LOẠI TRÌNH ĐỘ SINH VIÊN
## (AI-Powered Adaptive Learning & Student Performance Prediction)

### Học viện Công nghệ Bưu chính Viễn thông (PTIT)
- **Lớp**: D24TXCN08-B
- **Môn học**: Phát triển hệ thống thông minh (PTHTTM)
- **Nhóm thực hiện**: Nhóm 05
  - **Trần Hữu Nhật** - MSV: **B24DTCN260** (Trưởng nhóm)
  - **Chu Đình Minh** - MSV: **B24DTCN244** (Thành viên)
- **Đề tài số 13**: Hệ thống Gợi ý Lộ trình Học tập và Phân loại Trình độ Sinh viên

---

## 1. Giới thiệu Tổng quan
Hệ thống kết hợp giữa Học máy (Machine Learning), Cơ sở dữ liệu quan hệ (PostgreSQL) và Quy trình Vận hành Tự động hóa hiện đại (DevOps / MLOps trên nền tảng Docker Swarm & CI/CD) nhằm:
1. Dự đoán chính xác kết quả học tập của sinh viên dựa trên dữ liệu giáo dục đa chiều (điểm GPA, chuyên cần, giữa kỳ, đồ án, thời gian tự học, tỷ lệ điểm danh, hành vi tương tác trên hệ thống quản lý học tập LMS).
2. Phát hiện sớm các sinh viên thuộc nhóm nguy cơ cảnh báo học vụ để cố vấn học tập kịp thời can thiệp, gửi nhắc nhở và lên phương án kèm cặp.
3. Tự động đề xuất lộ trình học tập thích ứng cá nhân hóa (Adaptive Learning Roadmap) bao gồm: môn học tiên quyết cần củng cố, học phần nâng cao khuyến nghị, kỹ năng cần bổ trợ và số giờ tự học phù hợp theo từng học kỳ.

---

## 2. Công nghệ Cốt lõi
- **Học máy & Xử lý thông minh (CLO1)**: So sánh thực nghiệm Decision Tree, XGBoost và K-Means kết hợp Phân loại. Mô hình XGBoost đạt hiệu năng vượt trội với F1-score trên 0.98.
- **Cơ sở dữ liệu**: PostgreSQL lưu trữ hồ sơ sinh viên, chỉ số học tập, lộ trình học tập và nhật ký hỗ trợ của cố vấn.
- **Giao diện Web Portal**: FastAPI, Jinja2 Templates, Bootstrap 5, Chart.js hỗ trợ cả hai phân hệ: Cổng thông tin Sinh viên và Bảng điều khiển Cố vấn học tập.
- **Quy trình DevOps & MLOps (CLO2)**:
  - Khép kín từ khâu nạp dữ liệu, kiểm tra tính toàn vẹn (Data Validation), huấn luyện, thẩm định ngưỡng chất lượng mô hình (Model Gatekeeper: F1 >= 0.85).
  - Triển khai cụm Docker Swarm phân tán đa dịch vụ với tính năng Auto-scaling và Rolling Update (cập nhật không gián đoạn dịch vụ).
  - CI/CD tự động hóa toàn diện qua GitHub Actions.

---

## 3. Cấu trúc Thư mục Dự án
```
PTHTTM-Nhom05/
├── Project_Action Plan.docx              Kế hoạch dự án chi tiết Nhóm 05
├── Project_Final Report.docx             Báo cáo tổng kết dự án cuối khóa
├── Project_Work Breakdown Structure.xlsx Bảng phân rã công việc WBS
├── Bao_Cao_Ky_Thuat_Chi_Tiet.md          Báo cáo kỹ thuật chi tiết
├── requirements.txt                      Danh mục thư viện phụ thuộc
├── data/
│   ├── generate_data.py                  Kịch bản sinh 1500 mẫu dữ liệu giáo dục
│   ├── du_lieu_sinh_vien.csv             Bộ dữ liệu tổng thể
│   ├── du_lieu_huan_luyen.csv            Tập dữ liệu huấn luyện (80%)
│   └── du_lieu_kiem_thu.csv              Tập dữ liệu kiểm thử độc lập (20%)
├── database/
│   ├── init.sql                          Cấu trúc bảng PostgreSQL & dữ liệu khởi tạo
│   └── db_connection.py                  Kết nối cơ sở dữ liệu SQLAlchemy
├── ml_engine/
│   ├── data_loader.py                    Nạp và chuẩn bị đặc trưng
│   ├── train_models.py                   Huấn luyện và so sánh CLO1 (Decision Tree, XGBoost, K-Means)
│   ├── evaluate_models.py                Đánh giá ma trận nhầm lẫn & tầm quan trọng đặc trưng
│   ├── recommender.py                    Động cơ gợi ý lộ trình thích ứng
│   └── models/                           Tệp mô hình và báo cáo chỉ số JSON
├── web_app/
│   ├── main.py                           Ứng dụng FastAPI backend & routing
│   ├── schemas.py                        Định nghĩa lược đồ Pydantic
│   ├── static/                           Tệp CSS và JavaScript
│   └── templates/                        Giao diện Web Portal HTML (Jinja2)
├── deploy/
│   ├── docker-compose.yml                Triển khai môi trường cục bộ
│   ├── docker-stack.yml                  Triển khai cụm Docker Swarm có Auto-scaling
│   ├── Dockerfile.web                    Đóng gói Web Portal
│   ├── Dockerfile.ml                     Đóng gói Pipeline MLOps
│   ├── nginx.conf                        Cấu hình tải cân bằng Nginx
│   └── autoscaling_swarm.sh              Kịch bản tự động scale dịch vụ Swarm
└── .github/
    └── workflows/
        └── ci-cd.yml                     Quy trình CI/CD tự động hóa kiểm thử và triển khai
```

---

## 4. Hướng dẫn Vận hành Hệ thống

### 4.1. Cài đặt Môi trường Cục bộ
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 4.2. Khởi tạo Dữ liệu và Huấn luyện Mô hình CLO1
```bash
python data/generate_data.py
python -m ml_engine.train_models
python -m ml_engine.evaluate_models
```

### 4.3. Chạy Ứng dụng Web Portal
```bash
uvicorn web_app.main:app --reload --host 0.0.0.0 --port 8000
```
Truy cập trình duyệt tại địa chỉ: `http://localhost:8000`
- Cổng Sinh viên: `http://localhost:8000/sinh-vien`
- Bảng điều khiển Cố vấn: `http://localhost:8000/co-van`
- Báo cáo So sánh Mô hình CLO1: `http://localhost:8000/mo-hinh-clo1`

### 4.4. Triển khai bằng Docker Compose
```bash
docker compose -f deploy/docker-compose.yml up -d --build
```

### 4.5. Triển khai trên Cụm Docker Swarm (CLO2)
```bash
docker swarm init
docker stack deploy -c deploy/docker-stack.yml pthttm_stack
docker service ls
```
Tự động co giãn (Auto-scaling):
```bash
bash deploy/autoscaling_swarm.sh
```

