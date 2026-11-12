import os
import json
import time
import joblib
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from xgboost import XGBClassifier

from ml_engine.data_loader import tai_du_lieu, chuan_bi_dac_trung_va_nhan, DANH_SACH_DAC_TRUNG, ANH_XA_NHAN_NGUOC

class MoHinhKetHopKMeans:
    def __init__(self, so_cum=5, random_state=42):
        self.so_cum = so_cum
        self.random_state = random_state
        self.kmeans = KMeans(n_clusters=so_cum, random_state=random_state, n_init=10)
        self.bo_phan_loai = RandomForestClassifier(n_estimators=100, random_state=random_state)
        self.scaler = StandardScaler()

    def fit(self, X, y):
        X_scaled = self.scaler.fit_transform(X)
        nhan_cum = self.kmeans.fit_predict(X_scaled)
        X_mo_rong = np.column_stack((X_scaled, nhan_cum))
        self.bo_phan_loai.fit(X_mo_rong, y)
        return self

    def predict(self, X):
        X_scaled = self.scaler.transform(X)
        nhan_cum = self.kmeans.predict(X_scaled)
        X_mo_rong = np.column_stack((X_scaled, nhan_cum))
        return self.bo_phan_loai.predict(X_mo_rong)

    def predict_proba(self, X):
        X_scaled = self.scaler.transform(X)
        nhan_cum = self.kmeans.predict(X_scaled)
        X_mo_rong = np.column_stack((X_scaled, nhan_cum))
        return self.bo_phan_loai.predict_proba(X_mo_rong)

def huan_luyen_tat_ca_mo_hinh():
    os.makedirs("ml_engine/models", exist_ok=True)
    
    df_train = tai_du_lieu("data/du_lieu_huan_luyen.csv")
    df_test = tai_du_lieu("data/du_lieu_kiem_thu.csv")
    
    X_train, y_train = chuan_bi_dac_trung_va_nhan(df_train)
    X_test, y_test = chuan_bi_dac_trung_va_nhan(df_test)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    joblib.dump(scaler, "ml_engine/models/scaler.joblib")
    
    danh_sach_mo_hinh = {
        "Decision Tree (Cây quyết định)": DecisionTreeClassifier(max_depth=6, random_state=42),
        "XGBoost (Extreme Gradient Boosting)": XGBClassifier(n_estimators=120, max_depth=5, learning_rate=0.08, eval_metric="mlogloss", random_state=42),
        "K-Means + Classification (Phân cụm kết hợp Phân loại)": MoHinhKetHopKMeans(so_cum=5, random_state=42)
    }
    
    ket_qua_so_sanh = {}
    
    for ten_mo_hinh, mo_hinh in danh_sach_mo_hinh.items():
        thoi_gian_bat_dau = time.time()
        if "XGBoost" in ten_mo_hinh or "Decision Tree" in ten_mo_hinh:
            mo_hinh.fit(X_train, y_train)
        else:
            mo_hinh.fit(X_train, y_train)
        thoi_gian_huan_luyen = time.time() - thoi_gian_bat_dau
        
        thoi_gian_suy_luan_dau = time.time()
        y_pred = mo_hinh.predict(X_test)
        thoi_gian_suy_luan = (time.time() - thoi_gian_suy_luan_dau) / len(X_test) * 1000
        
        acc = float(accuracy_score(y_test, y_pred))
        prec = float(precision_score(y_test, y_pred, average="weighted", zero_division=0))
        rec = float(recall_score(y_test, y_pred, average="weighted", zero_division=0))
        f1 = float(f1_score(y_test, y_pred, average="weighted", zero_division=0))
        
        ket_qua_so_sanh[ten_mo_hinh] = {
            "do_chinh_xac": round(acc, 4),
            "precision": round(prec, 4),
            "recall": round(rec, 4),
            "f1_score": round(f1, 4),
            "thoi_gian_huan_luyen_giay": round(thoi_gian_huan_luyen, 4),
            "do_tre_suy_luan_ms": round(thoi_gian_suy_luan, 4)
        }
        
        if "Decision Tree" in ten_mo_hinh:
            joblib.dump(mo_hinh, "ml_engine/models/mo_hinh_decision_tree.joblib")
        elif "XGBoost" in ten_mo_hinh:
            joblib.dump(mo_hinh, "ml_engine/models/mo_hinh_xgboost.joblib")
        else:
            joblib.dump(mo_hinh, "ml_engine/models/mo_hinh_kmeans_classifier.joblib")

    mo_hinh_tot_nhat = max(ket_qua_so_sanh.items(), key=lambda x: x[1]["f1_score"])
    
    bao_cao_tong_hop = {
        "so_luong_mau_huan_luyen": len(X_train),
        "so_luong_mau_kiem_thu": len(X_test),
        "danh_sach_dac_trung": DANH_SACH_DAC_TRUNG,
        "ket_qua_chi_tiet": ket_qua_so_sanh,
        "mo_hinh_tot_nhat": mo_hinh_tot_nhat[0],
        "chi_so_f1_cao_nhat": mo_hinh_tot_nhat[1]["f1_score"]
    }
    
    with open("ml_engine/models/ket_qua_so_sanh.json", "w", encoding="utf-8") as f:
        json.dump(bao_cao_tong_hop, f, ensure_ascii=False, indent=2)
        
    return bao_cao_tong_hop

if __name__ == "__main__":
    huan_luyen_tat_ca_mo_hinh()

