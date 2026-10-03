import streamlit as st

# ==============================
# CẤU HÌNH ỨNG DỤNG
# ==============================
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 TÍNH LÃI GỬI TIẾT KIỆM NGÂN HÀNG")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi.")

st.divider()

# ==============================
# NHẬP THÔNG TIN
# ==============================

so_tien_gui = st.number_input(
    "💰 Số tiền gửi (VNĐ)",
    min_value=0,
    value=500_000_000,
    step=1_000_000,
    format="%d"
)

ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    value=3,
    step=1
)

lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    value=6.0,
    step=0.1
)

hinh_thuc_nhan_lai = st.selectbox(
    "💵 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# ==============================
# NÚT TÍNH TOÁN
# ==============================

if st.button("🧮 TÍNH TIỀN LÃI", use_container_width=True):

    # Chuyển lãi suất từ % sang số thập phân
    lai_suat_nam = lai_suat / 100

    # =================================
    # 1. NHẬN LÃI CUỐI KỲ
    # =================================
    if hinh_thuc_nhan_lai == "Cuối kỳ":

        tien_lai_dinh_ky = (
            so_tien_gui
            * lai_suat_nam
            * ky_han
            / 12
        )

        tong_tien_lai = tien_lai_dinh_ky

        tong_goc_va_lai = (
            so_tien_gui + tong_tien_lai
        )

        ten_lai_dinh_ky = "Tiền lãi cuối kỳ"

    # =================================
    # 2. NHẬN LÃI HÀNG THÁNG
    # =================================
    elif hinh_thuc_nhan_lai == "Hàng tháng":

        tien_lai_dinh_ky = (
            so_tien_gui
            * lai_suat_nam
            / 12
        )

        tong_tien_lai = (
            tien_lai_dinh_ky * ky_han
        )

        tong_goc_va_lai = (
            so_tien_gui + tong_tien_lai
        )

        ten_lai_dinh_ky = "Tiền lãi mỗi tháng"

    # =================================
    # 3. NHẬN LÃI HÀNG QUÝ
    # =================================
    else:

        # Số quý trong kỳ hạn
        so_quy = ky_han / 3

        # Tiền lãi mỗi quý
        tien_lai_dinh_ky = (
            so_tien_gui
            * lai_suat_nam
            * 3
            / 12
        )

        tong_tien_lai = (
            tien_lai_dinh_ky * so_quy
        )

        tong_goc_va_lai = (
            so_tien_gui + tong_tien_lai
        )

        ten_lai_dinh_ky = "Tiền lãi mỗi quý"

    # ==============================
    # HIỂN THỊ KẾT QUẢ
    # ==============================

    st.success("✅ Tính toán thành công!")

    st.subheader("📊 KẾT QUẢ")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label=ten_lai_dinh_ky,
            value=f"{tien_lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            label="Tổng tiền lãi",
            value=f"{tong_tien_lai:,.0f} VNĐ"
        )

    st.metric(
        label="💰 Tổng số tiền gốc và tiền lãi",
        value=f"{tong_goc_va_lai:,.0f} VNĐ"
    )

    # ==============================
    # THÔNG TIN KHOẢN GỬI
    # ==============================

    st.divider()

    st.write("### 📋 Thông tin khoản gửi")

    st.write(f"**Số tiền gửi:** {so_tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc_nhan_lai}")

# ==============================
# GHI CHÚ
# ==============================

st.divider()

st.caption(
    "Lưu ý: Kết quả được tính theo phương pháp lãi đơn, "
    "giả định lãi suất không thay đổi trong suốt kỳ hạn "
    "và tiền lãi không được nhập vào tiền gốc."
)
