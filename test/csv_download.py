import streamlit as st
import pandas as pd
import base64

# Streamlit 앱 제목 설정
st.title("DataFrame을 CSV로 다운로드하기")

# 사용자로부터 데이터 입력 받기
st.write("데이터를 입력하세요:")
data = st.text_area("데이터 입력", "1,2,3\n4,5,6\n7,8,9")

# 입력받은 데이터를 DataFrame으로 변환
data_list = [row.split(",") for row in data.split("\n")]
df = pd.DataFrame(data_list, columns=["열1", "열2", "열3"])

# DataFrame을 출력
st.write("생성된 DataFrame:")
st.write(df)

# CSV 파일 다운로드 링크 생성
def download_link(df, filename, text):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

# "CSV 파일로 다운로드" 버튼 생성
if st.button("CSV 파일로 다운로드"):
    st.markdown(download_link(df, "data.csv", "여기를 클릭하여 다운로드하세요!"), unsafe_allow_html=True)
