import streamlit as sl

sl.set_page_config(layout="wide")

col_1,col_2 = sl.columns(2)

with col_1:
    sl.image("images/photo.png")

with col_2:
    sl.title("Mithunkumar Selvaraj")
    content = """This is a sample content and needs to be modified from the data source on the fly"""
    sl.info(content)