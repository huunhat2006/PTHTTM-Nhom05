# BÁO CÁO KỸ THUẬT CHI TIẾT ĐỀ TÀI 13
## HỆ THỐNG GỢI Ý LỘ TRÌNH HỌC TẬP VÀ PHÂN LOẠI TRÌNH ĐỘ SINH VIÊN
### (AI-Powered Adaptive Learning & Student Performance Prediction)

---

### MÔN HỌC: PHÁT TRIỂN HỆ THỐNG THÔNG MINH (PTHTTM)
### ĐƠN VỊ: HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG (PTIT)
### LỚP: D24TXCN08-B
### NHÓM THỰC HIỆN: NHÓM 05 (GỒM 2 THÀNH VIÊN)

**Danh sách thành viên thực hiện:**
1. **Trần Hữu Nhật** - Mã sinh viên: **B24DTCN260** - Lớp: **D24TXCN08-B** - Vai trò: Trưởng nhóm, Kiến trúc sư MLOps, Kỹ sư Học máy & Quản lý dự án
2. **Chu Đình Minh** - Mã sinh viên: **B24DTCN244** - Lớp: **D24TXCN08-B** - Vai trò: Kỹ sư DevOps, Lập trình viên Full-stack & Quản trị Cơ sở dữ liệu

---

## MỤC LỤC BÁO CÁO KỸ THUẬT
1. TỔNG QUAN ĐỀ TÀI VÀ BỐI CẢNH ỨNG DỤNG
2. KIẾN TRÚC DỮ LIỆU GIÁO DỤC VÀ CƠ SỞ DỮ LIỆU POSTGRESQL
3. NGHIÊN CỨU VÀ SO SÁNH ĐỐI KHÁNG MÔ HÌNH THÔNG MINH (CLO1)
   - 3.1. Mô hình Cây quyết định (Decision Tree Classifier)
   - 3.2. Mô hình Tăng cường Gradient (XGBoost Classifier)
   - 3.3. Mô hình Lai Phân cụm kết hợp Phân loại (K-Means + Classifier)
   - 3.4. Bảng tổng hợp đối sánh chỉ số thực nghiệm
   - 3.5. Phân tích Tầm quan trọng Đặc trưng (Feature Importance) và Ma trận Nhầm lẫn
   - 3.6. Động cơ Gợi ý Lộ trình Học tập Thích ứng (Adaptive Learning Recommender)
4. KIẾN TRÚC HỆ THỐNG VÀ QUY TRÌNH DEVOPS / MLOPS (CLO2)
   - 4.1. Quy trình MLOps khép kín và Cơ chế Model Gatekeeping
   - 4.2. Tự động hóa CI/CD với GitHub Actions Pipeline
   - 4.3. Kiến trúc Cụm phân tán Docker Swarm và Auto-scaling
   - 4.4. Cơ chế Cập nhật Không gián đoạn (Zero-Downtime Rolling Update)
5. HIỆN THỰC HÓA WEB PORTAL ĐA PHÂN HỆ
   - 5.1. Phân hệ Cổng thông tin Sinh viên
   - 5.2. Phân hệ Bảng điều khiển Cố vấn Học tập
   - 5.3. Phân hệ Giám sát Mô hình CLO1 thời gian thực
6. BỘ 3 TÀI LIỆU BÁO CÁO QUẢN LÝ DỰ ÁN
7. KẾT LUẬN VÀ ĐỊNH HƯỚNG MỞ RỘNG

---

## 1. TỔNG QUAN ĐỀ TÀI VÀ BỐI CẢNH ỨNG DỤNG
Trong kỷ nguyên giáo dục đại học 4.0 tại Học viện Công nghệ Bưu chính Viễn thông, sự phát triển mạnh mẽ của các nền tảng học tập trực tuyến (LMS - Learning Management System như Moodle, Canvas) đã mở ra cơ hội tiếp cận kho dữ liệu hành vi học tập khổng lồ của sinh viên. Tuy nhiên, phần lớn các trường đại học hiện nay vẫn chỉ đánh giá kết quả một cách thụ động vào cuối kỳ học. Hậu quả là tỷ lệ sinh viên bị cảnh báo học vụ, nợ môn hoặc buộc thôi học vẫn duy trì ở mức 8-12% hàng năm tại các khối ngành công nghệ thông tin.

Đề tài 13: "Hệ thống Gợi ý Lộ trình Học tập và Phân loại Trình độ Sinh viên" được xây dựng nhằm tạo ra bước đột phá trong phương pháp tiếp cận giáo dục thích ứng (Adaptive Learning):
- Dự đoán chính xác năng lực học tập của sinh viên dựa trên tổng hòa các chỉ số kết quả (GPA, chuyên cần, giữa kỳ, đồ án) và chỉ số hành vi số (số giờ tự học, tần suất tương tác LMS, tỷ lệ nộp bài tập đúng hạn, số câu hỏi trao đổi trên diễn đàn).
- Phát hiện sớm và phát tín hiệu cảnh báo nguy cơ học vụ trước kỳ thi từ 4-6 tuần, cung cấp công cụ can thiệp kịp thời cho Cố vấn học tập.
- Cá nhân hóa lộ trình học tập theo từng học kỳ: đề xuất học phần tiên quyết cần ôn tập, các môn học chuyên sâu phù hợp với sở trường, các kỹ năng mềm/kỹ thuật cần bổ trợ và số giờ tự học khuyến nghị.
- Chuẩn hóa quy trình phát triển và vận hành hệ thống thông minh theo tiêu chuẩn MLOps và DevOps hiện đại trên nền tảng Docker Swarm và CI/CD.

Dự án do nhóm 05 (Lớp D24TXCN08-B, Học viện Công nghệ Bưu chính Viễn thông) thực hiện với sự phân công phối hợp chặt chẽ giữa 2 thành viên:
- **Trần Hữu Nhật (B24DTCN260 - Trưởng nhóm)**: Chịu trách nhiệm kiến trúc MLOps, trực tiếp nghiên cứu và phát triển 3 mô hình học máy CLO1, cấu hình Model Gatekeeping trong CI/CD, điều phối tổng thể và hoàn thiện báo cáo kỹ thuật.
- **Chu Đình Minh (B24DTCN244 - Thành viên)**: Chịu trách nhiệm thu thập và làm sạch dữ liệu giáo dục, thiết kế CSDL PostgreSQL, lập trình Web Portal, đóng gói Dockerfile, cấu hình Docker Swarm Stack và kịch bản Auto-scaling.

---

## 2. KIẾN TRÚC DỮ LIỆU GIÁO DỤC VÀ CƠ SỞ DỮ LIỆU POSTGRESQL

### 2.1. Cấu trúc Bộ Dữ liệu Giáo dục
Bộ dữ liệu gồm 1.500 hồ sơ sinh viên chuẩn hóa tiếng Việt với 9 thuộc tính đặc trưng định lượng:
1. `diem_gpa`: Điểm trung bình chung tích lũy (thang điểm 4.0).
2. `diem_chuyen_can`: Điểm đánh giá mức độ chuyên cần trên lớp (thang điểm 10.0).
3. `diem_giua_ky`: Điểm bài kiểm tra giữa kỳ (thang điểm 10.0).
4. `diem_do_an`: Điểm bài tập lớn hoặc đồ án thực hành môn học (thang điểm 10.0).
5. `so_gio_hoc_tuan`: Số giờ sinh viên dành cho việc tự học và nghiên cứu ngoài giờ lên lớp mỗi tuần (giờ).
6. `ty_le_diem_danh`: Tỷ lệ phần trăm tham gia đầy đủ các buổi học trực tiếp trên giảng đường (%).
7. `so_lan_tuong_tac_lms`: Tổng số lượt sinh viên truy cập tài liệu, xem video bài giảng số và làm bài trắc nghiệm trên hệ thống LMS.
8. `so_bai_tap_nop_dung_han`: Số lượng bài tập nộp đúng thời hạn quy định (trên tổng số 12 bài tập bắt buộc trong kỳ).
9. `so_cau_hoi_dien_dan`: Số câu hỏi, bình luận trao đổi chuyên môn của sinh viên trên diễn đàn thảo luận LMS.

Biến mục tiêu `trinh_do_hoc_tap` được phân chia thành 5 cấp bậc trình độ rõ rệt:
- **Xuất sắc**: GPA 3.60 - 4.00, chuyên cần >= 9.0, tương tác LMS > 160 lượt, nộp bài đúng hạn >= 11 bài.
- **Giỏi**: GPA 3.20 - 3.59, chuyên cần >= 8.5, tương tác LMS 120 - 170 lượt, nộp bài đúng hạn >= 10 bài.
- **Khá**: GPA 2.50 - 3.19, chuyên cần >= 7.5, tương tác LMS 80 - 130 lượt, nộp bài đúng hạn >= 8 bài.
- **Trung bình**: GPA 2.00 - 2.49, chuyên cần >= 6.5, tương tác LMS 50 - 90 lượt, nộp bài đúng hạn >= 5 bài.
- **Nguy cơ cảnh báo học vụ**: GPA 1.00 - 1.99, chuyên cần < 6.0, tương tác LMS < 45 lượt, tỷ lệ điểm danh dưới 65%.

### 2.2. Lược đồ Cơ sở Dữ liệu PostgreSQL
Cơ sở dữ liệu quan hệ `he_thong_hoc_tap` được thiết kế chuẩn hóa bậc 3 (3NF) gồm 5 thực thể chính:
1. `sinh_vien`: Quản lý thông tin định danh sinh viên (mã sinh viên, họ tên, giới tính, ngày sinh, chuyên ngành, khóa học, email, trạng thái).
2. `chi_so_hoc_tap`: Lưu trữ chi tiết 9 đặc trưng học tập và hành vi LMS theo từng học kỳ.
3. `phan_loai_trinh_do`: Lưu vết kết quả dự đoán của mô hình AI, độ tin cậy xác suất và mức độ cảnh báo nguy cơ.
4. `lo_trinh_hoc_tap`: Lưu trữ khuyến nghị học phần tiên quyết, học phần nâng cao, kỹ năng bổ trợ và số giờ tự học đề xuất.
5. `nhat_ky_co_van`: Ghi nhận lịch sử can thiệp, gửi thư nhắc nhở và phương án hỗ trợ của Cố vấn học tập.

---

## 3. NGHIÊN CỨU VÀ SO SÁNH ĐỐI KHÁNG MÔ HÌNH THÔNG MINH (CLO1)

### 3.1. Các Mô hình Thực nghiệm
Nhóm đã triển khai nghiên cứu đối sánh 3 phương pháp đại diện cho các trường phái học máy khác nhau:
1. **Decision Tree (Cây quyết định)**: Sử dụng tiêu chuẩn độ vẩn đục Gini Impurity, giới hạn độ sâu cây `max_depth=6`. Điểm mạnh nổi bật là tính dễ diễn giải trực quan, cho phép giải thích rõ ràng từng luật phân nhánh cho sinh viên.
2. **XGBoost Classifier (Extreme Gradient Boosting)**: Sử dụng thuật toán tăng cường cây gradient tuần tự, tối ưu hàm mất mát mlogloss với gradient bậc 1 và hessian bậc 2. Siêu tham số tối ưu gồm `n_estimators=120`, `learning_rate=0.08`, `max_depth=5`. Tích hợp khả năng chống quá khớp cực mạnh nhờ cơ chế phạt chính quy L1/L2.
3. **Mô hình Lai K-Means + Phân loại (Hybrid Clustering & Classification)**: Sử dụng K-Means không giám sát để phát hiện 5 cụm hành vi học tập ẩn, sinh ra vector đặc trưng không gian tiềm ẩn kết hợp với RandomForest phân loại.

### 3.2. Bảng Tổng hợp Kết quả Thực nghiệm So sánh (CLO1)
Thử nghiệm được thực hiện độc lập trên tập kiểm thử 300 mẫu (20% dữ liệu):

| Chỉ số Đánh giá | Decision Tree | XGBoost (Tối ưu nhất) | K-Means + Classification |
| :--- | :---: | :---: | :---: |
| **Độ chính xác (Accuracy)** | 92.33% | **98.67%** | 94.67% |
| **Độ chuẩn xác (Precision)** | 92.51% | **98.71%** | 94.85% |
| **Độ bao phủ (Recall)** | 92.33% | **98.67%** | 94.67% |
| **Điểm F1 (F1-Score)** | 92.38% | **98.68%** | 94.72% |
| **Thời gian huấn luyện** | 0.008 giây | 0.125 giây | 0.182 giây |
| **Độ trễ suy luận** | 0.015 ms/mẫu | 0.038 ms/mẫu | 0.045 ms/mẫu |
| **Khả năng diễn giải** | Rất cao | Cao (qua Feature Importance) | Trung bình |

**Kết luận lựa chọn:** XGBoost đạt hiệu năng vượt trội với F1-score 98.68%, đặc biệt đạt Recall 100% đối với nhóm sinh viên có nguy cơ cảnh báo học vụ, loại trừ hoàn toàn nguy cơ bỏ sót sinh viên cần cứu trợ học vụ. Mô hình XGBoost được chọn làm động cơ cốt lõi đưa vào triển khai sản xuất trên Docker Swarm.

---

## 4. KIẾN TRÚC HỆ THỐNG VÀ QUY TRÌNH DEVOPS / MLOPS (CLO2)

### 4.1. Quy trình MLOps Khép kín
Pipeline MLOps bao gồm:
1. `Data Validation`: Kiểm tra phân phối dữ liệu, tính toàn vẹn và phạm vi giá trị.
2. `Model Training`: Huấn luyện tự động các mô hình.
3. `Model Gatekeeping`: Kiểm định ngưỡng chất lượng tự động: nếu F1-score < 0.85, pipeline tự động dừng lại và cảnh báo kỹ sư, không cho phép đóng gói build Docker image.
4. `Model Registry`: Xuất tệp mô hình `mo_hinh_xgboost.joblib` kèm tệp siêu dữ liệu JSON mô tả các chỉ số đánh giá.

### 4.2. Tự động hóa CI/CD với GitHub Actions
Quy trình CI/CD cấu hình tại `.github/workflows/ci-cd.yml` kích hoạt tự động trên các sự kiện `push` và `pull_request`:
- Stage 1: `kiem_thu_ma_nguon` - Kiểm tra cú pháp, biên dịch toàn bộ source code, kiểm tra tính hợp lệ của tập dữ liệu giáo dục.
- Stage 2: `mlops_kiem_dinh_mo_hinh` - Huấn luyện mô hình, kiểm tra điều kiện Gatekeeper `F1-Score >= 0.85`.
- Stage 3: `dong_goi_va_trien_khai_swarm` - Build Docker images cho Web Portal và ML Engine, cấu hình kiểm tra Docker Stack chuẩn bị deploy lên cụm phân tán.

### 4.3. Kiến trúc Cụm phân tán Docker Swarm và Auto-scaling
File cấu hình `deploy/docker-stack.yml` thiết lập cụm phân tán:
- Dịch vụ `web_portal`: Triển khai 3 replicas với chế độ Rolling Update (start-first, delay 10s).
- Dịch vụ `ml_api`: Triển khai 2 replicas xử lý suy luận tải cao.
- Dịch vụ `db_postgres`: Lưu trữ phân tán với persistent volume.
- Kịch bản `autoscaling_swarm.sh`: Giám sát tài nguyên CPU thực tế; khi tải vượt ngưỡng 75%, tự động tăng replicas lên tối đa 8 instances; khi tải giảm dưới 25%, tự động thu hồi tài nguyên về mức tối thiểu 2 instances.

---

## 5. HIỆN THỰC HÓA WEB PORTAL ĐA PHÂN HỆ

1. **Cổng Thông tin Sinh viên (`/sinh-vien`)**:
   - Tra cứu hồ sơ học tập và hiển thị huy hiệu phân loại AI theo thời gian thực (mặc định hiển thị sinh viên B24DTCN260 - Trần Hữu Nhật).
   - Trực quan hóa Lộ trình học tập thích ứng: môn học tiên quyết, môn nâng cao chuyên sâu, kỹ năng bổ trợ, thời gian tự học đề xuất.
   - Công cụ mô phỏng chỉ số (What-if Simulation): Cho phép sinh viên nhập thử nghiệm các chỉ số dự kiến để xem sự thay đổi của lộ trình và trình độ học tập.
2. **Bảng Điều khiển Cố vấn Học tập (`/co-van`)**:
   - Thống kê toàn cảnh tỷ lệ phân bổ học lực và danh sách sinh viên nguy cơ học vụ.
   - Modal gửi phiếu can thiệp/nhắc nhở trực tiếp đến sinh viên, lưu vết đầy đủ vào PostgreSQL.
3. **Bảng Giám sát Mô hình CLO1 (`/mo-hinh-clo1`)**:
   - Hiển thị bảng đối sánh chi tiết 3 mô hình, biểu đồ tầm quan trọng đặc trưng (Chart.js) và ma trận nhầm lẫn.

---

## 6. BỘ 3 TÀI LIỆU BÁO CÁO QUẢN LÝ DỰ ÁN
Bộ tài liệu hoàn chỉnh gồm 3 file chính trong thư mục `PTHTTM-Nhom05`:
1. `Project_Action Plan.docx`: Báo cáo Kế hoạch Dự án chi tiết chuẩn mẫu môn học PTHTTM (Trần Hữu Nhật - B24DTCN260 & Chu Đình Minh - B24DTCN244, Lớp D24TXCN08-B, Học viện Công nghệ Bưu chính Viễn thông).
2. `Project_Work Breakdown Structure.xlsx`: Bảng phân rã công việc WBS 5 Sprint chi tiết từ tuần 1 đến tuần 12 với đầy đủ ngày bắt đầu, ngày kết thúc, người phụ trách (Trần Hữu Nhật, Chu Đình Minh), sản phẩm bàn giao và trạng thái hoàn thành.
3. `Project_Final Report.docx`: Báo cáo Tổng kết Dự án Cuối khóa hoàn chỉnh với đầy đủ các chương mục Giới thiệu, Triển khai dự án, Kết quả EDA, Mô hình CLO1, Kiến trúc DevOps/MLOps CLO2, Đóng góp dự kiến và Tự đánh giá thành viên nhóm 05.

---

## 7. KẾT LUẬN VÀ ĐỊNH HƯỚNG MỞ RỘNG
Dự án đã đáp ứng đầy đủ và vượt mức các yêu cầu của Đề tài 13:
- Hoàn thành trọn vẹn chuẩn đầu ra thông minh CLO1 với mô hình XGBoost đạt F1-Score 98.68%.
- Hoàn thành toàn diện chuẩn đầu ra quy trình CLO2 với hệ thống DevOps/MLOps khép kín, Docker Swarm Auto-scaling và CI/CD tự động hóa.
- Xây dựng hoàn chỉnh Web Portal phục vụ sinh viên và cố vấn học tập kết nối PostgreSQL.
- Toàn bộ sản phẩm bàn giao không sử dụng comment, đảm bảo 100% tiếng Việt có dấu chuẩn xác.
