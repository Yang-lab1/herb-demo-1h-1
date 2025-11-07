import streamlit as st
import sqlite3

# 连接数据库（成员A传的herbs.db放在同一文件夹）
def get_db():
    return sqlite3.connect("herbs.db")

st.title("1小时测试版")

# 1. 查询功能（按名称搜）
st.subheader("查药材")
name = st.text_input("输入名称（如当归）")
if st.button("查询"):
    db = get_db()
    res = db.execute("SELECT * FROM herbs WHERE 名称 LIKE ?", (f'%{name}%',)).fetchall()
    st.write(res)  # 直接显示结果，不美化
    db.close()

# 2. 提交功能
st.subheader("提建议")
with st.form("f"):
    n = st.text_input("药材名")
    c = st.text_input("建议内容")
    if st.form_submit_button("提交"):
        db = get_db()
        db.execute("INSERT INTO pending (名称, 内容) VALUES (?,?)", (n, c))
        db.commit()
        db.close()
        st.success("提交成功！")
