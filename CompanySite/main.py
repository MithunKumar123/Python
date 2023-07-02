import streamlit as sl
import pandas as p

sl.set_page_config(layout="wide")

sl.header('The Best company website')
sl.write('Hi! This is a demo which can be given as part of the best company website development')

df = p.read_csv("data.csv", sep=",")

sl.subheader("Our Team Members")

col_1, col_2, col_3 = sl.columns(3)


def show_column(data_list):
    for index_arg, row_arg in data_list.iterrows():
        sl.subheader(f"{row_arg['first name'].title()} {row_arg['last name'].title()}")
        sl.write(row_arg['role'])
        sl.image("images/" + row_arg['image'])


with col_1:
    show_column(df[:4])

with col_2:
    show_column(df[4:8])

with col_3:
    show_column(df[8:])