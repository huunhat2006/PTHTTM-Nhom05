import os
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from ml_engine.data_loader import tai_du_lieu, chuan_bi_dac_trung_va_nhan, DANH_SACH_DAC_TRUNG, ANH_XA_NHAN, ANH_XA_NHAN_NGUOC

def danh_gia_chuyen_sau():
    df_test = tai_du_lieu("data/du_lieu_kiem_thu.csv")
    X_test, y_test = chuan_bi_dac_trung_va_nhan(df_test)
    
    if not os.path.exists("ml_engine/models/mo_hinh_xgboost.joblib"):
        from ml_engine.train_models import huan_luyen_tat_ca_mo_hinh
        huan_luyen_tat_ca_mo_hinh()
        
    mo_hinh_xgb = joblib.load("ml_engine/models/mo_hinh_xgboost.joblib")
    mo_hinh_dt = joblib.load("ml_engine/models/mo_hinh_decision_tree.joblib")
    
    y_pred_xgb = mo_hinh_xgb.predict(X_test)
    y_pred_dt = mo_hinh_dt.predict(X_test)
    
    nhan_labels = [ANH_XA_NHAN_NGUOC[i] for i in range(5)]
    
    cm_xgb = confusion_matrix(y_test, y_pred_xgb, labels=[0, 1, 2, 3, 4]).tolist()
    cm_dt = confusion_matrix(y_test, y_pred_dt, labels=[0, 1, 2, 3, 4]).tolist()
    
    tam_quan_trong_xgb = [float(x) for x in mo_hinh_xgb.feature_importances_]
    tam_quan_trong_dt = [float(x) for x in mo_hinh_dt.feature_importances_]
    
    dac_trung_tieng_viet = [
        "Điểm GPA tích lũy",
        "Điểm chuyên cần",
        "Điểm kiểm tra giữa kỳ",
        "Điểm bài tập lớn/đồ án",
        "Số giờ học mỗi tuần",
        "Tỷ lệ điểm danh (%)",
        "Số lần tương tác LMS",
        "Số bài tập nộp đúng hạn",
        "Số câu hỏi trên diễn đàn"
    ]
    
    bao_cao_chuyen_sau = {
        "nhan_lop": nhan_labels,
        "dac_trung": dac_trung_tieng_viet,
        "ma_tran_nham_lan_xgboost": cm_xgb,
        "ma_tran_nham_lan_decision_tree": cm_dt,
        "tam_quan_trong_xgboost": tam_quan_trong_xgb,
        "tam_quan_trong_decision_tree": tam_quan_trong_dt,
        "bao_cao_chi_tiet_xgboost": classification_report(y_test, y_pred_xgb, target_names=nhan_labels, output_dict=True)
    }
    
    with open("ml_engine/models/danh_gia_chuyen_sau.json", "w", encoding="utf-8") as f:
        json.dump(bao_cao_chuyen_sau, f, ensure_ascii=False, indent=2)
        
    return bao_cao_chuyen_sau

if __name__ == "__main__":
    danh_gia_chuyen_sau()

