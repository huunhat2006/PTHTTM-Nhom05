import docx

doc = docx.Document('Project_Action Plan.docx')

noi_dung = {
    'team_name': 'Nhóm 05 - Lớp D24TXCN08-B - Học viện Công nghệ Bưu chính Viễn thông',
    'members': 'Trần Hữu Nhật - MSV: B24DTCN260 - Lớp: D24TXCN08-B (Trưởng nhóm - Quản lý dự án, Kiến trúc MLOps & Kỹ sư Học máy)\nChu Đình Minh - MSV: B24DTCN244 - Lớp: D24TXCN08-B (Thành viên - Kỹ sư DevOps, Lập trình viên Web Portal & Cơ sở dữ liệu)',
    'title': 'Hệ thống Gợi ý Lộ trình Học tập và Phân loại Trình độ Sinh viên (AI-Powered Adaptive Learning & Student Performance Prediction)',
    'objective': '- Xây dựng giải pháp thông minh toàn diện ứng dụng Machine Learning (Decision Tree, XGBoost, K-Means + Phân loại) để phân tích dữ liệu giáo dục đa chiều (điểm số học tập, tương tác hệ thống LMS, mức độ chuyên cần, thời gian tự học).\n- Tự động phân loại chính xác 5 cấp độ trình độ sinh viên (Xuất sắc, Giỏi, Khá, Trung bình, Nguy cơ cảnh báo học vụ) với độ chính xác F1-score đạt trên 98%.\n- Phát hiện sớm và cảnh báo kịp thời các sinh viên có nguy cơ trượt môn hoặc bị buộc thôi học trước kỳ thi từ 4-6 tuần, cung cấp công cụ can thiệp cho Cố vấn học tập.\n- Tự động hóa đề xuất Lộ trình học tập thích ứng cá nhân hóa (Adaptive Learning Roadmap) bao gồm học phần tiên quyết cần ôn tập, học phần nâng cao khuyến nghị, kỹ năng bổ trợ và số giờ tự học phù hợp theo từng kỳ.\n- Hiện thực hóa quy trình DevOps / MLOps hoàn chỉnh từ khâu chuẩn hóa dữ liệu, kiểm thử tự động (CI/CD), Model Gatekeeping, đóng gói Docker đến triển khai cụm phân tán Docker Swarm có khả năng tự động co giãn (Auto-scaling) và cập nhật không gián đoạn (Zero-downtime Rolling Update).',
    'abstract': 'Dự án Hệ thống Gợi ý Lộ trình Học tập và Phân loại Trình độ Sinh viên giải quyết bài toán cốt lõi trong giáo dục đại học thời kỳ số hóa: tình trạng sinh viên bị mất định hướng, cảnh báo học vụ muộn và thiếu lộ trình phát triển năng lực cá nhân hóa. Bằng việc ứng dụng thuật toán học máy XGBoost kết hợp cơ sở dữ liệu quan hệ PostgreSQL và hạ tầng Docker Swarm hiện đại, hệ thống phân tích đồng thời dữ liệu kết quả học tập và hành vi tương tác trên LMS để đưa ra dự đoán chuẩn xác và khuyến nghị lộ trình thích ứng. Sản phẩm bàn giao gồm một Cổng thông tin Web Portal hiện đại phục vụ đồng thời sinh viên và cố vấn học tập, một Pipeline MLOps tự động hóa kiểm định mô hình qua CI/CD GitHub Actions, và hệ thống báo cáo kỹ thuật chi tiết theo chuẩn môn học Phát triển hệ thống thông minh.',
    'methodology': '- Phương pháp Học máy (CLO1): Thu thập và làm sạch dữ liệu giáo dục có cấu trúc. Huấn luyện thực nghiệm và so sánh đối sánh giữa 3 hướng tiếp cận: Cây quyết định (Decision Tree - độ diễn giải cao), XGBoost (thuật toán tăng cường Gradient với khả năng xử lý phi tuyến và chống overfitting vượt trội), và K-Means kết hợp Phân loại (phát hiện cụm tiềm năng ẩn kết hợp phân lớp). Sử dụng các độ đo Accuracy, Precision, Recall, F1-Score, ma trận nhầm lẫn và Feature Importance để chọn mô hình tối ưu đưa vào sản xuất.\n- Phương pháp DevOps & MLOps (CLO2): Thiết lập quy trình phát triển và vận hành tự động: Tích hợp liên tục (CI) kiểm tra cú pháp, chất lượng mã nguồn, kiểm thử dữ liệu và kiểm định ngưỡng chất lượng mô hình (Model Gatekeeper: F1 >= 0.85); Đóng gói container hóa qua Dockerfile cho Web Portal và ML Engine; Triển khai liên tục (CD) lên cụm Docker Swarm phân tán với Nginx Reverse Proxy, cấu hình Replicas, Healthcheck, Rolling Update và kịch bản Auto-scaling tự động co giãn tài nguyên theo tải CPU thực tế.',
    'data': '- Dữ liệu sử dụng: Dữ liệu giáo dục có cấu trúc chuẩn hóa tiếng Việt gồm 1.500 hồ sơ sinh viên với 9 nhóm đặc trưng định lượng: Điểm trung bình tích lũy (GPA thang 4), Điểm chuyên cần (thang 10), Điểm kiểm tra giữa kỳ (thang 10), Điểm bài tập lớn/đồ án (thang 10), Số giờ tự học mỗi tuần, Tỷ lệ tham gia điểm danh (%), Số lần truy cập tương tác LMS, Số bài tập nộp đúng hạn (trên 12 bài), và Số câu hỏi trao đổi trên diễn đàn học tập.\n- Nguồn gốc và Quy trình thu thập: Tích lũy từ hệ thống quản lý đào tạo và log truy cập máy chủ LMS Moodle của nhà trường, lưu trữ tập trung tại cơ sở dữ liệu PostgreSQL.\n- Tiền xử lý và sử dụng: Dữ liệu được làm sạch, xử lý giá trị ngoại lai, chuẩn hóa bằng StandardScaler và phân chia ngặt nghèo thành tập Huấn luyện (80% - 1.200 mẫu) và tập Kiểm thử độc lập (20% - 300 mẫu) để đánh giá khách quan.',
    'outcome': '- Hệ thống Web Portal hoàn chỉnh: Giao diện Cổng sinh viên tra cứu chỉ số, nhận phân loại trình độ và xem lộ trình học tập thích ứng cá nhân hóa; Giao diện Cố vấn học tập trực quan hóa bảng phân bổ năng lực sinh viên, bảng cảnh báo sinh viên nguy cơ học vụ và chức năng gửi phiếu can thiệp/nhắc nhở.\n- Pipeline MLOps & DevOps khép kín: Tự động hóa kiểm tra dữ liệu, huấn luyện mô hình, kiểm tra ngưỡng chất lượng Gatekeeper (F1 >= 0.85), đóng gói Docker và triển khai lên cụm Docker Swarm.\n- Bộ mô hình ML tối ưu: Tệp mô hình XGBoost đã qua huấn luyện đạt F1-score trên 98%, lưu trữ tại Model Registry kèm siêu dữ liệu đánh giá.\n- Lợi ích mang lại: Giảm tỷ lệ sinh viên bị cảnh báo học vụ và buộc thôi học xuống dưới 5%, nâng cao năng lực tự học của sinh viên, tiết kiệm thời gian quản lý cho cố vấn học tập và khoa chuyên môn.',
    'roles': '1. Trần Hữu Nhật - MSV: B24DTCN260 - Lớp: D24TXCN08-B (Trưởng nhóm / MLOps Architect & ML Engineer): Định hướng kiến trúc tổng thể, nghiên cứu và huấn luyện 3 mô hình học máy CLO1 (Decision Tree, XGBoost, K-Means + Phân loại), thiết lập quy trình MLOps, cấu hình Model Gatekeeping, quản lý tiến độ và biên tập báo cáo dự án.\n2. Chu Đình Minh - MSV: B24DTCN244 - Lớp: D24TXCN08-B (Thành viên / DevOps Engineer & Full-stack Developer): Thu thập và xử lý dữ liệu giáo dục (EDA), thiết kế cơ sở dữ liệu PostgreSQL, xây dựng Web Portal (FastAPI, Cổng sinh viên, Dashboard cố vấn), đóng gói Dockerfile, cấu hình Docker Swarm Stack (docker-stack.yml), kịch bản Auto-scaling và pipeline CI/CD GitHub Actions.',
    'schedule': 'Dự án được triển khai qua 5 Sprint chính (tương ứng với WBS chi tiết):\n- Sprint 1 (Tuần 1 - Tuần 2): Khởi tạo dự án, phân tích yêu cầu nghiệp vụ, thiết kế kiến trúc hệ thống và lập kế hoạch hành động (Action Plan & WBS).\n- Sprint 2 (Tuần 3 - Tuần 4): Thu thập, làm sạch dữ liệu giáo dục; thiết kế cơ sở dữ liệu PostgreSQL (init.sql); thực hiện phân tích khám phá dữ liệu (EDA).\n- Sprint 3 (Tuần 5 - Tuần 7): Nghiên cứu và huấn luyện thực nghiệm 3 mô hình học máy CLO1 (Decision Tree, XGBoost, K-Means + Phân loại); đánh giá chỉ số và xây dựng động cơ gợi ý lộ trình thích ứng.\n- Sprint 4 (Tuần 8 - Tuần 10): Phát triển Web Portal (FastAPI, Cổng sinh viên, Dashboard cố vấn); đóng gói Docker container; thiết lập cụm Docker Swarm và Auto-scaling (CLO2).\n- Sprint 5 (Tuần 11 - Tuần 12): Tích hợp pipeline CI/CD GitHub Actions; kiểm thử tích hợp toàn diện; nghiệm thu sản phẩm và hoàn thiện bộ 3 tài liệu báo cáo kỹ thuật.',
    'instructor': 'Giảng viên hướng dẫn ghi nhận đánh giá, nhận xét tiến độ và kết quả nghiệm thu đề tài.'
}

t0 = doc.tables[0]
t0.rows[1].cells[1].text = noi_dung['team_name']
t0.rows[2].cells[1].text = noi_dung['members']
t0.rows[3].cells[1].text = noi_dung['title']
t0.rows[5].cells[0].text = noi_dung['objective']
t0.rows[5].cells[1].text = noi_dung['objective']
t0.rows[7].cells[0].text = noi_dung['abstract']
t0.rows[7].cells[1].text = noi_dung['abstract']
t0.rows[9].cells[0].text = noi_dung['methodology']
t0.rows[9].cells[1].text = noi_dung['methodology']

t1 = doc.tables[1]
t1.rows[1].cells[0].text = noi_dung['data']
t1.rows[1].cells[1].text = noi_dung['data']
t1.rows[3].cells[0].text = noi_dung['outcome']
t1.rows[3].cells[1].text = noi_dung['outcome']
t1.rows[5].cells[0].text = noi_dung['roles']
t1.rows[5].cells[1].text = noi_dung['roles']

t2 = doc.tables[2]
t2.rows[1].cells[0].text = noi_dung['schedule']
t2.rows[1].cells[1].text = noi_dung['schedule']
t2.rows[3].cells[0].text = noi_dung['instructor']
t2.rows[3].cells[1].text = noi_dung['instructor']

doc.save('Project_Action Plan.docx')
print('Action Plan updated successfully with student codes B24DTCN260 & B24DTCN244 and class D24TXCN08-B!')
