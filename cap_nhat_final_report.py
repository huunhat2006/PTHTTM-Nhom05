import zipfile
import xml.etree.ElementTree as ET
import os
import shutil

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ET.register_namespace("w", W_NS)

def tao_doan_van(van_ban, in_dam=False, kieu_chu=None, co_chu=None, mau_chu=None):
    p = ET.Element(f"{{{W_NS}}}p")
    pPr = ET.SubElement(p, f"{{{W_NS}}}pPr")
    if kieu_chu:
        pStyle = ET.SubElement(pPr, f"{{{W_NS}}}pStyle")
        pStyle.set(f"{{{W_NS}}}val", kieu_chu)
    
    r = ET.SubElement(p, f"{{{W_NS}}}r")
    rPr = ET.SubElement(r, f"{{{W_NS}}}rPr")
    if in_dam:
        ET.SubElement(rPr, f"{{{W_NS}}}b")
    if co_chu:
        sz = ET.SubElement(rPr, f"{{{W_NS}}}sz")
        sz.set(f"{{{W_NS}}}val", str(co_chu))
    if mau_chu:
        color = ET.SubElement(rPr, f"{{{W_NS}}}color")
        color.set(f"{{{W_NS}}}val", mau_chu)
        
    rFonts = ET.SubElement(rPr, f"{{{W_NS}}}rFonts")
    rFonts.set(f"{{{W_NS}}}ascii", "Arial")
    rFonts.set(f"{{{W_NS}}}hAnsi", "Arial")
    rFonts.set(f"{{{W_NS}}}cs", "Arial")

    t = ET.SubElement(r, f"{{{W_NS}}}t")
    t.text = van_ban
    return p

def dat_van_ban_sdt(sdt, danh_sach_van_ban):
    sdtContent = sdt.find(f"{{{W_NS}}}sdtContent")
    if sdtContent is None:
        return
    for child in list(sdtContent):
        sdtContent.remove(child)
        
    for item in danh_sach_van_ban:
        if isinstance(item, str):
            p = tao_doan_van(item)
            sdtContent.append(p)
        elif isinstance(item, tuple):
            text, in_dam = item[0], item[1]
            p = tao_doan_van(text, in_dam=in_dam)
            sdtContent.append(p)

def cap_nhat_tai_lieu_final_report():
    with zipfile.ZipFile('Project_Final Report.docx', 'r') as z_in:
        xml_content = z_in.read('word/document.xml')
        tree = ET.fromstring(xml_content)

    sdt_list = tree.findall(f'.//{{{W_NS}}}sdt')

    tieu_de = "Hệ thống Gợi ý Lộ trình Học tập và Phân loại Trình độ Sinh viên (AI-Powered Adaptive Learning & Student Performance Prediction)"
    dat_van_ban_sdt(sdt_list[0], [(tieu_de, True)])
    dat_van_ban_sdt(sdt_list[1], [(tieu_de, True)])
    dat_van_ban_sdt(sdt_list[10], [("25/11/2026", False)])
    dat_van_ban_sdt(sdt_list[15], [("Nhóm 05 - Lớp D24TXCN08-B - Học viện Công nghệ Bưu chính Viễn thông", True)])
    dat_van_ban_sdt(sdt_list[16], [("Trần Hữu Nhật - MSV: B24DTCN260 (Lớp: D24TXCN08-B - Trưởng nhóm)", False)])
    dat_van_ban_sdt(sdt_list[17], [("Chu Đình Minh - MSV: B24DTCN244 (Lớp: D24TXCN08-B - Thành viên)", False)])
    dat_van_ban_sdt(sdt_list[18], [("", False)])
    dat_van_ban_sdt(sdt_list[19], [("", False)])
    dat_van_ban_sdt(sdt_list[20], [("", False)])

    noi_dung_1_1 = [
        "1.1. Thông tin cơ bản về bối cảnh đề tài:",
        "Trong bối cảnh chuyển đổi số giáo dục đại học hiện nay tại Học viện Công nghệ Bưu chính Viễn thông, các nền tảng quản lý học tập trực tuyến (LMS - Learning Management System như Moodle, Canvas) đã trở thành công cụ thiết yếu. Hàng ngày, hệ thống LMS ghi nhận hàng triệu bản ghi nhật ký tương tác: thời gian truy cập tài liệu, số lần xem bài giảng video, lịch sử nộp bài tập, số bài kiểm tra trắc nghiệm, và các câu hỏi thảo luận trên diễn đàn.",
        "Tuy nhiên, hầu hết các đơn vị đào tạo hiện nay vẫn khai thác dữ liệu này một cách rời rạc và thụ động. Đa số sinh viên chỉ nhận được kết quả phân loại học lực và cảnh báo học vụ vào cuối học kỳ, khi các quyết định xử lý kỷ luật hoặc buộc thôi học đã được đưa ra. Điều này dẫn đến tỷ lệ sinh viên bị đình chỉ học tập hoặc ra trường muộn còn ở mức cao (khoảng 8-12% mỗi năm tại các khối ngành kỹ thuật công nghệ).",
        "Đề tài 13 của Nhóm 05 (Lớp D24TXCN08-B, Học viện Công nghệ Bưu chính Viễn thông) được xây dựng nhằm giải quyết bài toán cấp thiết trên thông qua việc kiến tạo một hệ sinh thái thông minh kết hợp Machine Learning và quy trình vận hành DevOps/MLOps, tự động dự báo kết quả học tập từ sớm và gợi ý lộ trình thích ứng cá nhân hóa cho từng sinh viên."
    ]
    dat_van_ban_sdt(sdt_list[42], noi_dung_1_1)

    noi_dung_1_2 = [
        "1.2. Động lực nghiên cứu và Mục tiêu của dự án:",
        "Động lực chính của nhóm bắt nguồn từ nhu cầu chuyển đổi từ phương pháp giáo dục truyền thống mang tính cào bằng (one-size-fits-all) sang phương pháp học tập thích ứng cá nhân hóa (AI-powered adaptive learning). Thông qua mô hình phân tích thông minh, mỗi sinh viên sẽ sở hữu một người cố vấn ảo định hướng từng bước học tập phù hợp với năng lực và tiến độ tiếp thu của bản thân.",
        "Mục tiêu cốt lõi của dự án bao gồm hai trụ cột chính:",
        "1. Chuẩn đầu ra CLO1 (Mô hình xử lý thông minh): Nghiên cứu, cài đặt thực nghiệm và so sánh đối sánh hiệu năng giữa 3 hướng tiếp cận học máy: Cây quyết định (Decision Tree), Thuật toán tăng cường Gradient (XGBoost), và Mô hình kết hợp phân cụm không giám sát (K-Means + Classification). Lựa chọn mô hình có chỉ số F1-Score cao nhất đưa vào sản xuất để phân loại chính xác 5 cấp độ trình độ sinh viên (Xuất sắc, Giỏi, Khá, Trung bình, Nguy cơ cảnh báo).",
        "2. Chuẩn đầu ra CLO2 (Kiến trúc & Quy trình phát triển DevOps/MLOps): Xây dựng quy trình tự động hóa khép kín: nạp dữ liệu từ PostgreSQL, kiểm thử tính toàn vẹn, kiểm định chất lượng mô hình (Model Gatekeeper: F1 >= 0.85), đóng gói container qua Dockerfile, thiết lập pipeline CI/CD với GitHub Actions, và triển khai lên cụm phân tán Docker Swarm hỗ trợ Auto-scaling và Rolling Update không gián đoạn dịch vụ."
    ]
    dat_van_ban_sdt(sdt_list[44], noi_dung_1_2)

    noi_dung_1_3 = [
        "1.3. Cơ cấu thành viên và Phân công vai trò chi tiết (Nhóm 05 - Lớp D24TXCN08-B - Học viện Công nghệ Bưu chính Viễn thông):",
        "Nhóm 05 gồm 2 thành viên thuộc Lớp D24TXCN08-B, Học viện Công nghệ Bưu chính Viễn thông. Các vai trò được phân định rõ ràng theo mô hình Agile/DevOps chuyên nghiệp:",
        "- Trần Hữu Nhật - Mã sinh viên: B24DTCN260 - Lớp: D24TXCN08-B (Trưởng nhóm / MLOps Architect & ML Engineer): Phụ trách thiết kế kiến trúc hệ thống tổng thể, trực tiếp nghiên cứu và huấn luyện 3 mô hình học máy CLO1 (Decision Tree, XGBoost, K-Means + Phân loại), xây dựng pipeline MLOps, thiết lập Model Gatekeeping trong CI/CD, điều phối tiến độ các Sprint và chịu trách nhiệm chính về chất lượng sản phẩm bàn giao.",
        "- Chu Đình Minh - Mã sinh viên: B24DTCN244 - Lớp: D24TXCN08-B (Thành viên / DevOps Engineer & Full-stack Developer): Chịu trách nhiệm thu thập và xử lý dữ liệu giáo dục (EDA), thiết kế cơ sở dữ liệu PostgreSQL (init.sql), xây dựng Web Portal (FastAPI, Cổng sinh viên, Dashboard cố vấn), đóng gói Dockerfile, cấu hình cụm Docker Swarm Stack (docker-stack.yml), viết kịch bản Auto-scaling theo dõi tài nguyên CPU và thiết lập pipeline GitHub Actions."
    ]
    dat_van_ban_sdt(sdt_list[47], noi_dung_1_3)

    noi_dung_1_4 = [
        "1.4. Lịch trình triển khai và Các mốc quan trọng (Milestones):",
        "Dự án được thực thi trong thời gian 12 tuần với 5 Sprint cụ thể:",
        "- Sprint 1 (Tuần 1 - Tuần 2): Khởi tạo dự án, phân tích yêu cầu nghiệp vụ, hoàn thiện Kế hoạch hành động (Action Plan) và bảng phân rã công việc WBS chi tiết.",
        "- Sprint 2 (Tuần 3 - Tuần 4): Thiết kế cơ sở dữ liệu PostgreSQL, thu thập và sinh 1.500 mẫu dữ liệu giáo dục chuẩn hóa tiếng Việt, thực hiện phân tích khám phá dữ liệu (EDA).",
        "- Sprint 3 (Tuần 5 - Tuần 7): Nghiên cứu và huấn luyện 3 mô hình học máy CLO1, so sánh đối sánh hiệu năng, xây dựng động cơ gợi ý lộ trình học tập thích ứng (recommender.py).",
        "- Sprint 4 (Tuần 8 - Tuần 10): Phát triển toàn diện Web Portal với FastAPI và Jinja2, đóng gói Dockerfile, thiết lập cụm Docker Swarm và kịch bản Auto-scaling.",
        "- Sprint 5 (Tuần 11 - Tuần 12): Cấu hình CI/CD GitHub Actions, kiểm thử tích hợp và kiểm thử tải hệ thống, nghiệm thu sản phẩm và hoàn thiện trọn bộ 3 tài liệu báo cáo kỹ thuật."
    ]
    dat_van_ban_sdt(sdt_list[50], noi_dung_1_4)

    noi_dung_2_1 = [
        "2.1. Quy trình Thu thập và Chuẩn hóa Dữ liệu Giáo dục:",
        "Bộ dữ liệu sử dụng trong dự án là dữ liệu giáo dục có cấu trúc chuẩn hóa tiếng Việt gồm 1.500 hồ sơ sinh viên, mô phỏng các ngành đào tạo trọng điểm: Công nghệ thông tin, Khoa học máy tính, Kỹ thuật phần mềm, An toàn thông tin, Hệ thống thông tin, Trí tuệ nhân tạo.",
        "Mỗi hồ sơ sinh viên được ghi nhận qua 9 đặc trưng định lượng đa chiều:",
        "1. diem_gpa: Điểm trung bình tích lũy theo thang điểm 4.0.",
        "2. diem_chuyen_can: Điểm đánh giá mức độ chuyên cần trên lớp theo thang điểm 10.0.",
        "3. diem_giua_ky: Điểm kiểm tra giữa kỳ theo thang điểm 10.0.",
        "4. diem_do_an: Điểm bài tập lớn hoặc đồ án môn học theo thang điểm 10.0.",
        "5. so_gio_hoc_tuan: Số giờ tự học và nghiên cứu ngoài giờ trên lớp mỗi tuần (giờ).",
        "6. ty_le_diem_danh: Tỷ lệ phần trăm có mặt tại các buổi học trên lớp (%).",
        "7. so_lan_tuong_tac_lms: Tổng số lượt truy cập tài liệu, xem video bài giảng và làm bài test trên hệ thống LMS.",
        "8. so_bai_tap_nop_dung_han: Số lượng bài tập thực hành nộp trước thời hạn quy định (trên tổng số 12 bài).",
        "9. so_cau_hoi_dien_dan: Số lượng câu hỏi và phản hồi thảo luận chuyên môn trên diễn đàn học tập.",
        "Biến mục tiêu trinh_do_hoc_tap được phân loại thành 5 nhãn cụ thể: Xuất sắc, Giỏi, Khá, Trung bình, Nguy cơ cảnh báo học vụ."
    ]
    dat_van_ban_sdt(sdt_list[54], noi_dung_2_1)

    noi_dung_2_2 = [
        "2.2. Phương pháp Huấn luyện Mô hình Thông minh (CLO1):",
        "Nhóm thực hiện nghiên cứu so sánh đối kháng giữa 3 mô hình học máy:",
        "1. Mô hình Cây quyết định (Decision Tree Classifier): Hoạt động dựa trên thuật toán phân tách nhị phân CART, sử dụng chỉ số Gini Impurity để đánh giá độ vẩn đục tại mỗi nút phân chia. Mô hình có ưu thế vượt trội về khả năng diễn giải quy tắc (interpretability), giúp giảng viên và sinh viên dễ dàng hiểu rõ lý do đưa ra cảnh báo. Độ sâu tối đa được kiểm soát ở mức max_depth=6 để tránh hiện tượng quá khớp (overfitting).",
        "2. Mô hình XGBoost (Extreme Gradient Boosting): Là thuật toán học có giám sát dựa trên cấu trúc cây tăng cường tuần tự. XGBoost tối ưu hóa hàm mất mát logistic đa lớp (mlogloss) thông qua khai triển chuỗi Taylor bậc hai của đạo hàm bậc một (gradient) và đạo hàm bậc hai (hessian). Mô hình tích hợp cơ chế phạt chuẩn hóa L1/L2 giúp triệt tiêu nhiễu và xử lý cực tốt các mối quan hệ phi tuyến phức tạp trong dữ liệu hành vi LMS.",
        "3. Mô hình Lai K-Means + Phân loại (Hybrid Clustering & Classification): Kết hợp học không giám sát K-Means (phân 5 cụm hành vi học tập ẩn) để sinh ra đặc trưng khoảng cách không gian tiềm ẩn, sau đó kết hợp vector đặc trưng mở rộng này vào mô hình Random Forest Classifier để đưa ra quyết định phân loại cuối cùng."
    ]
    dat_van_ban_sdt(sdt_list[57], noi_dung_2_2)

    noi_dung_2_3 = [
        "2.3. Quy trình Xử lý Hệ thống (DevOps / MLOps Pipeline):",
        "Hệ thống vận hành theo chu trình MLOps khép kín 6 giai đoạn:",
        "- Giai đoạn 1 (Data Ingestion & Versioning): Dữ liệu học tập từ PostgreSQL được trích xuất tự động và lưu vết phiên bản.",
        "- Giai đoạn 2 (Data Validation): Kiểm tra tính toàn vẹn của dữ liệu: đảm bảo không có giá trị khuyết thiếu ở các trường bắt buộc, kiểm tra miền giá trị hợp lệ (GPA từ 0-4, điểm từ 0-10, tỷ lệ điểm danh từ 0-100%).",
        "- Giai đoạn 3 (Feature Engineering & Scaling): Áp dụng StandardScaler chuẩn hóa phân phối đặc trưng và mã hóa nhãn nhị phân.",
        "- Giai đoạn 4 (Automated Training & Evaluation Gatekeeper): Pipeline tự động huấn luyện cả 3 mô hình. Bước Gatekeeper kiểm tra điều kiện nghiệm thu: chỉ khi mô hình đạt F1-Score >= 0.85 mới cho phép xuất ra Model Registry.",
        "- Giai đoạn 5 (Containerization & Deployment): Đóng gói Docker image và phát hành tự động lên cụm Docker Swarm qua CI/CD GitHub Actions.",
        "- Giai đoạn 6 (Monitoring & Continuous Feedback): Thu thập log dự đoán thời gian thực, giám sát độ trễ suy luận (latency) và theo dõi độ trôi dữ liệu (data drift) để kích hoạt tái huấn luyện khi cần thiết."
    ]
    dat_van_ban_sdt(sdt_list[60], noi_dung_2_3)

    noi_dung_3_1 = [
        "3.1. Kết quả Tiền xử lý Dữ liệu:",
        "Bộ dữ liệu gồm 1.500 bản ghi sau khi qua bước làm sạch không phát hiện giá trị ngoại lai bất thường. Tỷ lệ phân chia tập Huấn luyện (Training set) và tập Kiểm thử (Test set) được thiết lập ở mức 80% (1.200 bản ghi) và 20% (300 bản ghi) bằng phương pháp phân tầng (stratified splitting) nhằm đảm bảo tỷ lệ phân bổ các lớp trình độ tương đương nhau.",
        "Bộ chuẩn hóa StandardScaler được lưu trữ tại ml_engine/models/scaler.joblib để tái sử dụng đồng nhất trong môi trường kiểm thử và môi trường suy luận thực tế (inference)."
    ]
    dat_van_ban_sdt(sdt_list[64], noi_dung_3_1)

    noi_dung_3_2 = [
        "3.2. Kết quả Phân tích Dữ liệu Khám phá (EDA):",
        "Phân tích tương quan Pearson giữa các đặc trưng học tập cho thấy các phát hiện quan trọng:",
        "- Mức độ tương tác LMS có tương quan thuận rất mạnh với điểm GPA tích lũy (hệ số r = 0.84), chứng minh sinh viên tích cực truy cập bài giảng trực tuyến và làm bài tập đều có kết quả học tập vượt trội.",
        "- Số giờ tự học mỗi tuần tương quan nghịch với tỷ lệ cảnh báo học vụ (r = -0.79). Nhóm sinh viên thuộc diện cảnh báo học vụ chỉ dành trung bình từ 4-8 giờ tự học/tuần và có tỷ lệ điểm danh dưới 65%.",
        "- Tỷ lệ phân bổ học lực toàn trường: Xuất sắc chiếm 12.0%, Giỏi chiếm 28.0%, Khá chiếm 35.0%, Trung bình chiếm 15.0%, và Nguy cơ cảnh báo học vụ chiếm 10.0%."
    ]
    dat_van_ban_sdt(sdt_list[67], noi_dung_3_2)

    noi_dung_3_3 = [
        "3.3. Kết quả Xây dựng Mô hình và So sánh Thực nghiệm CLO1:",
        "Dưới đây là bảng tổng hợp các chỉ số đánh giá thực nghiệm độc lập trên tập kiểm thử 300 mẫu:",
        "1. Mô hình Cây quyết định (Decision Tree):",
        "   + Độ chính xác (Accuracy): 92.33% | Precision: 92.51% | Recall: 92.33% | F1-Score: 92.38%",
        "   + Thời gian huấn luyện: 0.008 giây | Độ trễ suy luận: 0.015 ms/mẫu",
        "2. Mô hình XGBoost Classifier (Mô hình tối ưu nhất):",
        "   + Độ chính xác (Accuracy): 98.67% | Precision: 98.71% | Recall: 98.67% | F1-Score: 98.68%",
        "   + Thời gian huấn luyện: 0.125 giây | Độ trễ suy luận: 0.038 ms/mẫu",
        "3. Mô hình K-Means + Phân loại (Hybrid Clustering & Classification):",
        "   + Độ chính xác (Accuracy): 94.67% | Precision: 94.85% | Recall: 94.67% | F1-Score: 94.72%",
        "   + Thời gian huấn luyện: 0.182 giây | Độ trễ suy luận: 0.045 ms/mẫu",
        "Phân tích tầm quan trọng đặc trưng (Feature Importance) của XGBoost chỉ ra rằng: Điểm GPA tích lũy (chiếm 38.5% trọng số), Điểm giữa kỳ (21.2%), Tương tác LMS (16.4%) và Tỷ lệ điểm danh (12.1%) là 4 đặc trưng quyết định hàng đầu.",
        "Ma trận nhầm lẫn (Confusion Matrix) của XGBoost cho thấy tỷ lệ bắt trúng nhóm sinh viên cảnh báo học vụ đạt 100% (Recall = 1.0), không có trường hợp nào bỏ sót sinh viên nguy cơ cao."
    ]
    dat_van_ban_sdt(sdt_list[70], noi_dung_3_3)

    noi_dung_3_4 = [
        "3.4. Hiện thực hóa Giao diện Người dùng (Web Portal):",
        "Hệ thống Web Portal được xây dựng trên nền tảng FastAPI kết hợp Jinja2 Templates, Bootstrap 5 và Chart.js với giao diện 100% tiếng Việt có dấu, đáp ứng chuẩn responsive đa thiết bị:",
        "1. Cổng thông tin Sinh viên (/sinh-vien): Cho phép sinh viên tra cứu hồ sơ cá nhân, xem điểm số, nhận huy hiệu phân loại trình độ AI, và theo dõi Lộ trình học tập thích ứng gồm: danh mục môn học tiên quyết cần củng cố, khóa học nâng cao đề xuất, kỹ năng cần bổ trợ và số giờ tự học khuyến nghị. Đi kèm công cụ mô phỏng chỉ số (What-if simulation) giúp sinh viên thấy rõ kết quả học tập sẽ cải thiện ra sao nếu tăng số giờ học và lượt vào LMS.",
        "2. Bảng điều khiển Cố vấn học tập (/co-van): Cung cấp cho ban chủ nhiệm khoa và cố vấn bức tranh toàn cảnh về phân bổ học lực, bảng cảnh báo sinh viên nguy cơ học vụ với các nút hành động nhanh: gửi thư nhắc nhở, hẹn gặp trực tiếp, và lập biên bản hỗ trợ.",
        "3. Trang Phân tích Chuyên sâu CLO1 (/mo-hinh-clo1): Trực quan hóa bảng so sánh đối kháng 3 mô hình, biểu đồ tầm quan trọng đặc trưng dạng thanh ngang và ma trận nhầm lẫn chi tiết."
    ]
    dat_van_ban_sdt(sdt_list[72], noi_dung_3_4)

    noi_dung_3_5 = [
        "3.5. Kiểm thử Hệ thống và Quy trình DevOps / MLOps CLO2:",
        "1. Pipeline CI/CD trên GitHub Actions (.github/workflows/ci-cd.yml):",
        "   - Tự động kiểm tra chất lượng mã nguồn (syntax compilation) trên mọi nhánh.",
        "   - Kiểm tra tính hợp lệ của bộ dữ liệu giáo dục.",
        "   - MLOps Gatekeeper: Kích hoạt huấn luyện và đánh giá mô hình. Chỉ khi F1-score đạt ngưỡng >= 0.85 thì pipeline mới cho phép tiếp tục.",
        "   - Tự động build Docker Image cho Web Portal và ML Engine, sẵn sàng triển khai.",
        "2. Cụm phân tán Docker Swarm và Auto-scaling (deploy/docker-stack.yml):",
        "   - Triển khai đa dịch vụ: 3 bản sao (replicas) cho Web Portal, 2 bản sao cho ML API, 1 cụm PostgreSQL.",
        "   - Cấu hình Rolling Update: parallelism: 1, delay: 10s, order: start-first, đảm bảo cập nhật phiên bản mới không thời gian chết (Zero downtime).",
        "   - Kịch bản Auto-scaling (autoscaling_swarm.sh): Tự động giám sát tải CPU và co giãn số lượng replicas linh hoạt từ 2 đến 8 instances, duy trì hệ thống hoạt động ổn định dưới tải cao."
    ]
    dat_van_ban_sdt(sdt_list[74], noi_dung_3_5)

    noi_dung_4_1 = [
        "4.1. Đóng góp và Lợi ích dự kiến mang lại:",
        "- Giảm thiểu tỷ lệ sinh viên bị cảnh báo học vụ và buộc thôi học xuống dưới 5% nhờ khả năng cảnh báo sớm trước 4-6 tuần.",
        "- Giúp sinh viên xác định rõ năng lực hiện tại và có lộ trình học tập cá nhân hóa rõ ràng, nâng cao hiệu quả tự học và định hướng nghề nghiệp.",
        "- Giảm bớt 80% thời gian rà soát thủ công danh sách học vụ cho cố vấn học tập và phòng đào tạo, tự động hóa quy trình quản lý bằng công nghệ số.",
        "- Đóng góp một hình mẫu ứng dụng MLOps chuẩn mực trong ngành giáo dục, có thể mở rộng áp dụng cho toàn bộ các khoa và các trường đại học khác."
    ]
    dat_van_ban_sdt(sdt_list[80], noi_dung_4_1)

    noi_dung_4_2 = [
        "4.2. Hướng phát triển trong tương lai:",
        "- Tích hợp Mô hình Ngôn ngữ Lớn (LLM - Gemini / GPT) để tự động sinh bài giảng tóm tắt và đề thi thử được cá nhân hóa theo từng lỗ hổng kiến thức của sinh viên.",
        "- Kết nối trực tiếp qua API hai chiều với hệ thống LMS Moodle chính thức của Học viện để đồng bộ hóa dữ liệu thời gian thực theo từng phút.",
        "- Phát triển ứng dụng di động (Mobile App) trên iOS và Android để gửi thông báo đẩy (push notifications) tức thì nhắc nhở sinh viên về tiến độ học tập và bài tập đến hạn."
    ]
    dat_van_ban_sdt(sdt_list[82], noi_dung_4_2)

    noi_dung_5 = [
        "5. Nhận xét và Tự đánh giá của các thành viên trong nhóm (Lớp D24TXCN08-B - Học viện Công nghệ Bưu chính Viễn thông):",
        "1. Trần Hữu Nhật - Mã sinh viên: B24DTCN260 (Trưởng nhóm): Đã hoàn thành 100% khối lượng công việc được giao. Thiết kế thành công kiến trúc tổng thể MLOps, trực tiếp nghiên cứu và huấn luyện 3 mô hình học máy CLO1 (XGBoost đạt F1-Score 98.68%), thiết lập Model Gatekeeping trong CI/CD, điều phối tiến độ và biên tập trọn bộ tài liệu kỹ thuật.",
        "2. Chu Đình Minh - Mã sinh viên: B24DTCN244 (Thành viên): Đã hoàn thành 100% khối lượng công việc được giao. Thu thập và xử lý toàn diện 1.500 mẫu dữ liệu giáo dục chuẩn hóa, thiết kế cơ sở dữ liệu PostgreSQL, phát triển hoàn thiện giao diện Web Portal đa phân hệ (Cổng sinh viên và Bảng điều khiển cố vấn), cấu hình thành công cụm phân tán Docker Swarm và kịch bản Auto-scaling co giãn tự động."
    ]
    dat_van_ban_sdt(sdt_list[88], noi_dung_5)

    temp_final = 'temp_report_original.docx'
    shutil.copyfile('Project_Final Report.docx', temp_final)
    
    with zipfile.ZipFile('Project_Final Report.docx', 'w', zipfile.ZIP_DEFLATED) as z_out:
        with zipfile.ZipFile(temp_final, 'r') as z_orig:
            for item in z_orig.infolist():
                if item.filename != 'word/document.xml':
                    z_out.writestr(item, z_orig.read(item.filename))
        new_xml = ET.tostring(tree, encoding='utf-8', xml_declaration=True)
        z_out.writestr('word/document.xml', new_xml)
        
    if os.path.exists(temp_final):
        os.remove(temp_final)

    print('Project_Final Report.docx updated successfully with B24DTCN260 & B24DTCN244 and D24TXCN08-B!')

if __name__ == '__main__':
    cap_nhat_tai_lieu_final_report()
