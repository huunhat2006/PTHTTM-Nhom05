document.addEventListener("DOMContentLoaded", function () {
    const formDuDoan = document.getElementById("form-du-doan-sinh-vien");
    if (formDuDoan) {
        formDuDoan.addEventListener("submit", async function (e) {
            e.preventDefault();
            const duLieu = {
                ma_sinh_vien: document.getElementById("input-ma-sv").value,
                ho_ten: document.getElementById("input-ho-ten").value,
                chuyen_nganh: document.getElementById("input-chuyen-nganh").value,
                diem_gpa: parseFloat(document.getElementById("input-gpa").value),
                diem_chuyen_can: parseFloat(document.getElementById("input-chuyen-can").value),
                diem_giua_ky: parseFloat(document.getElementById("input-giua-ky").value),
                diem_do_an: parseFloat(document.getElementById("input-do-an").value),
                so_gio_hoc_tuan: parseFloat(document.getElementById("input-so-gio").value),
                ty_le_diem_danh: parseFloat(document.getElementById("input-diem-danh").value),
                so_lan_tuong_tac_lms: parseInt(document.getElementById("input-lms").value),
                so_bai_tap_nop_dung_han: parseInt(document.getElementById("input-bai-tap").value),
                so_cau_hoi_dien_dan: parseInt(document.getElementById("input-cau-hoi").value)
            };

            const nutSubmit = document.getElementById("nut-du-doan");
            nutSubmit.disabled = true;
            nutSubmit.innerText = "Đang xử lý...";

            try {
                const res = await fetch("/api/du-doan", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(duLieu)
                });
                const data = await res.json();
                
                document.getElementById("ket-qua-khung").classList.remove("d-none");
                document.getElementById("ket-qua-trinh-do").innerText = data.trinh_do_du_doan;
                document.getElementById("ket-qua-xac-suat").innerText = (data.xac_suat_du_doan * 100).toFixed(1) + "%";
                document.getElementById("ket-qua-nguy-co").innerText = data.nguy_co_canh_bao;
                document.getElementById("ket-qua-tien-quyet").innerText = data.lo_trinh.mon_hoc_tien_quyet;
                document.getElementById("ket-qua-nang-cao").innerText = data.lo_trinh.mon_hoc_nang_cao;
                document.getElementById("ket-qua-ky-nang").innerText = data.lo_trinh.ky_nang_can_bo_tro;
                document.getElementById("ket-qua-thoi-gian").innerText = data.lo_trinh.thoi_gian_hoc_khuyen_nghi;
                document.getElementById("ket-qua-loi-khuyen").innerText = data.lo_trinh.loi_khuyen_hoc_tap;

                document.getElementById("ket-qua-khung").scrollIntoView({ behavior: "smooth" });
            } catch (err) {
                alert("Đã xảy ra lỗi khi dự đoán: " + err);
            } finally {
                nutSubmit.disabled = false;
                nutSubmit.innerText = "Phân tích và Gợi ý Lộ trình";
            }
        });
    }

    const formCoVan = document.getElementById("form-gui-co-van");
    if (formCoVan) {
        formCoVan.addEventListener("submit", async function (e) {
            e.preventDefault();
            const duLieu = {
                ma_sinh_vien: document.getElementById("co-van-ma-sv").value,
                ten_co_van: document.getElementById("co-van-ten").value,
                noi_dung_nhac_nho: document.getElementById("co-van-noi-dung").value,
                hinh_thuc_ho_tro: document.getElementById("co-van-hinh-thuc").value
            };
            try {
                const res = await fetch("/api/ghi-nhan-co-van", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(duLieu)
                });
                const data = await res.json();
                alert("Thành công: " + data.thong_bao);
                const modal = bootstrap.Modal.getInstance(document.getElementById("modalCoVan"));
                if (modal) modal.hide();
                formCoVan.reset();
            } catch (err) {
                alert("Lỗi khi ghi nhận: " + err);
            }
        });
    }
});

function moModalCoVan(maSv, hoTen) {
    document.getElementById("co-van-ma-sv").value = maSv;
    document.getElementById("co-van-ten-sv-hien-thi").innerText = hoTen + " (" + maSv + ")";
    const modal = new bootstrap.Modal(document.getElementById("modalCoVan"));
    modal.show();
}

