import streamlit as st

def main():
    st.title("我的第一個Streamlit App")
    st.header("Jared vs Nydia")
    st.subheader("這是一個簡單的Streamlit應用程式")
    st.text("這是一些普通的文字。")
    st.markdown("這是一些 **Markdown** 格式的文字。")
    st.latex(r"E = mc^2")  # 顯示LaTeX公式
    st.json({"key": "value", "number": 42})  # 顯示JSON格式的資料
    st.dataframe({"Column1": [1, 2, 3], "Column2": ["A", "B", "C"]})  # 顯示DataFrame
    st.table({"Column1": [1, 2, 3], "Column2": ["A", "B", "C"]})  # 顯示表格
    st.write("歡迎來到我的應用程式！")
    st.button("點擊我！", key="my_button")
    st.text_input("請輸入一些文字", key="my_text_input")
    st.checkbox("勾選我！", key="my_checkbox")
    st.radio("選擇一個選項", options=["選項1", "選項2", "選項3"], key="my_radio")
    st.selectbox("選擇一個選項", options=["選項A", "選項B", "選項C"], key="my_selectbox")
    st.multiselect("多選選項", options=["選項X", "選項Y", "選項Z"], key="my_multiselect")
    st.slider("滑動條", min_value=0, max_value=100, key="my_slider")
    st.number_input("數字輸入", min_value=0, max_value=100, key="my_number_input")
    st.text_area("多行文字輸入", key="my_text_area")
    st.file_uploader("上傳檔案", type=["txt", "csv"], key="my_file_uploader")
    st.date_input("選擇日期", key="my_date_input")
    st.time_input("選擇時間", key="my_time_input")
    st.color_picker("選擇顏色", key="my_color_picker")
    st.progress(50, text="進度條示例", key="my_progress")
    st.spinner("正在處理...")  # 顯示一個處理中的提示
    st.success("操作成功！", icon="✅")  # 顯示成功提示
    st.error("發生錯誤！", icon="❌")  # 顯示錯誤提示
    st.warning("這是一個警告！", icon="⚠️")  # 顯示警告提示
    st.info("這是一個資訊提示！", icon="ℹ️")  # 顯示資訊提示
    st.markdown("這是一些 **Markdown** 格式的文字。")  # 使用Markdown格式顯示文字
    st.latex(r"E = mc^2")  # 顯示LaTeX公式
    st.json({"key": "value", "number": 42})  # 顯示JSON格式的資料
    st.dataframe({"Column1": [1, 2, 3], "Column2": ["A", "B", "C"]})  # 顯示DataFrame
    st.table({"Column1": [1, 2, 3], "Column2": ["A", "B", "C"]})  # 顯示表格
    st.balloons()  # 顯示氣球動畫
    st.sidebar.title("側邊欄")
    st.sidebar.write("這是側邊欄的內容。")
    st.sidebar.button("側邊欄按鈕", key="sidebar_button")
    st.sidebar.text_input("側邊欄文字輸入", key="sidebar_text_input")
    st.sidebar.checkbox("側邊欄勾選框", key="sidebar_checkbox")
    st.sidebar.radio("側邊欄選項", options=["選項A", "選項B"], key="sidebar_radio")
    st.sidebar.selectbox("側邊欄選擇框", options=["選項1", "選項2"], key="sidebar_selectbox")
    st.sidebar.multiselect("側邊欄多選框", options=["選項X", "選項Y"], key="sidebar_multiselect")
    st.sidebar.slider("側邊欄滑動條", min_value=0, max_value=50, key="sidebar_slider")
    st.sidebar.number_input("側邊欄數字輸入", min_value=0, max_value=50, key="sidebar_number_input")
    st.sidebar.text_area("側邊欄多行文字輸入", key="sidebar_text_area")
    st.sidebar.file_uploader("側邊欄上傳檔案", type=["txt", "csv"], key="sidebar_file_uploader")
    st.sidebar.date_input("側邊欄日期選擇", key="sidebar_date_input")
    st.sidebar.time_input("側邊欄時間選擇", key="sidebar_time_input")
    st.sidebar.color_picker("側邊欄顏色選擇", key="sidebar_color_picker")
    st.sidebar.progress(30, text="側邊欄進度條示例", key="sidebar_progress")
    st.sidebar.spinner("側邊欄正在處理...")  # 側邊欄處理中的提示
    st.sidebar.success("側邊欄操作成功！", icon="✅")  # 側邊欄成功提示
    st.sidebar.error("側邊欄發生錯誤！", icon="❌")  # 側邊欄錯誤提示
    st.sidebar.warning("側邊欄這是一個警告！", icon="⚠️")  # 側邊欄警告提示
    st.sidebar.info("側邊欄這是一個資訊提示！", icon="ℹ️")  # 側邊欄資訊提示
    st.sidebar.markdown("側邊欄這是一些 **Markdown** 格式的文字。")  # 側邊欄使用Markdown格式顯示文字
    st.sidebar.latex(r"E = mc^2")  # 側邊欄顯示LaTeX公式
    st.sidebar.json({"key": "value", "number": 42})  # 側邊欄顯示JSON格式的資料
    st.sidebar.dataframe({"Column1": [1, 2, 3], "Column2": ["A", "B", "C"]})  # 側邊欄顯示DataFrame 


if __name__ == "__main__":
    main()
