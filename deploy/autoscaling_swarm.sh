TEN_DICH_VU="pthttm_stack_web_portal"
NGUONG_CPU_TREN=75
NGUONG_CPU_DUOI=25
SO_LUONG_TOI_THIEU=2
SO_LUONG_TOI_DA=8

SO_LUONG_HIEN_TAI=$(docker service inspect --format='{{.Spec.Mode.Replicated.Replicas}}' $TEN_DICH_VU 2>/dev/null || echo 2)
MUC_SU_DUNG_CPU=$(docker stats --no-stream --format "{{.CPUPerc}}" | sed 's/%//' | awk '{s+=$1} END {print s/NR}')
MUC_CPU_TRUNG_BINH=${MUC_SU_DUNG_CPU%.*}

if [ -z "$MUC_CPU_TRUNG_BINH" ]; then
    MUC_CPU_TRUNG_BINH=30
fi

if [ "$MUC_CPU_TRUNG_BINH" -gt "$NGUONG_CPU_TREN" ] && [ "$SO_LUONG_HIEN_TAI" -lt "$SO_LUONG_TOI_DA" ]; then
    SO_LUONG_MOI=$((SO_LUONG_HIEN_TAI + 1))
    docker service scale $TEN_DICH_VU=$SO_LUONG_MOI
elif [ "$MUC_CPU_TRUNG_BINH" -lt "$NGUONG_CPU_DUOI" ] && [ "$SO_LUONG_HIEN_TAI" -gt "$SO_LUONG_TOI_THIEU" ]; then
    SO_LUONG_MOI=$((SO_LUONG_HIEN_TAI - 1))
    docker service scale $TEN_DICH_VU=$SO_LUONG_MOI
fi

