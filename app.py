import streamlit as st
from streamlit import session_state as ss
from pdftext.extraction import plain_text_output
from io import BytesIO

if 'pdf_ref' not in ss:
    ss.pdf_ref = None

def main():
    st.title("Lấy text từ slides/pdf")

    # Hướng dẫn sử dụng
    st.header("Hướng dẫn sử dụng")
    st.write("""
    1. Nhấn nút 'Tải lên' để chọn file PDF mình muốn lấy văn bản.
    2. Nhập khoảng trang trong file mình muốn chuyển sang text.
    3. Nhấn nút 'Chuyển đổi sang văn bản' để bắt đầu.
    4. Sau đó, nhấn nút 'Tải xuống' để lấy file txt. M có thể copy từ đó sang word,.... .
    """)

    st.file_uploader("Tải lên file PDF", type=('pdf'), key='pdf')
    
    if ss.pdf:
        ss.pdf_ref = ss.pdf

    if ss.pdf_ref:
        binary_data = ss.pdf_ref.getvalue()

        st.subheader("Nhập số trang để trích xuất:")
        start_page = st.number_input("Trang bắt đầu", min_value=1, value=1)
        end_page = st.number_input("Trang kết thúc", min_value=1, value=10)

        if st.button("Chuyển đổi sang văn bản"):
            try:
                pdf_path = "temp.pdf"
                with open(pdf_path, "wb") as f:
                    f.write(binary_data)
                
                text = plain_text_output(pdf_path, sort=True, hyphens=False, page_range=list(range(start_page, end_page + 1)))
                
                text_file = "output.txt"
                with open(text_file, "w", encoding="utf-8") as f:
                    f.write(text)
                
                st.success("Trích xuất văn bản thành công!")
                with open(text_file, "r", encoding="utf-8") as f:
                    st.download_button("Tải xuống", data=f.read(), file_name="output.txt", mime="text/plain")
            
            except Exception as e:
                st.error(f"Lỗi: {e}")

if __name__ == "__main__":
    main()
