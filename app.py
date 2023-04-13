import streamlit as st

st.set_page_config(
    page_title="Giải phương trình bậc 2",
    page_icon=":pencil2:",
    layout="wide",
    )

st.title("Giải phương trình bậc 2")
st.write("Nhập các hệ số a, b, c của phương trình bậc 2 và nhấn nút \"Giải phương trình\" để tính toán.")

col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input("a", value=0.0, step=0.1)
with col2:
    b = st.number_input("b", value=0.0, step=0.1)
with col3:
    c = st.number_input("c", value=0.0, step=0.1)

st.write("")

col4, col5 = st.columns(2)
with col4:
    if st.button("Giải phương trình"):
        delta = b**2 - 4*a*c
        if delta < 0:
            st.warning("Phương trình vô nghiệm.")
        elif delta == 0:
            x = -b / (2*a)
            st.success(f"Phương trình có nghiệm kép x = {x}.")
        else:
            x1 = (-b + delta**0.5) / (2*a)
            x2 = (-b - delta**0.5) / (2*a)
            st.success(f"Phương trình có hai nghiệm phân biệt x1 = {x1} và x2 = {x2}.")
with col5:
    st.write("")


