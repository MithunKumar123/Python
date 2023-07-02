import streamlit as sl
import pandas as p

sl.set_page_config(layout="wide")

col_1, col_2 = sl.columns(2)


def show_column(data_list):
    for index_arg, row_arg in data_list.iterrows():
        sl.header(row_arg['title'])
        sl.write(row_arg["description"])
        sl.image("images/" + row_arg['image'])
        sl.write(f"[Source Code]({row_arg['url']})")


with col_1:
    sl.image("images/photo.png")

with col_2:
    sl.title("Mithunkumar Selvaraj")
    content = """This is a sample content and needs to be modified from the data source on the fly"""
    sl.info(content)

sl.write("Below you can find some apps which I built in python, Feel free to contact me")

col_3, empty_col, col_4 = sl.columns([1.5,0.5,1.5])
data = p.read_csv("data.csv", sep=";")
with col_3:
    show_column(data[:10])

with col_4:
    show_column(data[10:])
