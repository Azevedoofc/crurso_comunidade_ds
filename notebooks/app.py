import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pandas as pd
import streamlit as st
from src import answers as asw
from src.extraction import load_data

st.set_page_config(layout="wide")

def create_dataframe_section(df):
    st.title("Sections - Database Description")

    col_1, col_2 = st.columns(2)

    col_1.header("Database")
    col_1.dataframe(df, height=530)

    col_2.header("Data Description")
    data_description = """
        | Coluna | Descrição |
        | :----- | --------: |
        | ID | Identificador da linha/registro |
        | name | Fabricante e Modelo da Moto |
        | selling_price | Preço de Venda |
        | year | Ano de Fabricação da Moto |
        | seller_type | Tipo de Vendedor - Se é vendedor pessoal ou revendedor |
        | owner | Se é primeiro, segundo, terceiro ou quarto dono da moto |
        | km_driven | Quantidade de Quilômetros percorridos pela moto |
        | ex_showroom_price | Preço da motocicleta sem as taxas de seguro e registro |
        | age | Quantidade de anos em que a moto está em uso |
        | km_class | Classificação das motos conforme a quilometragem percorrida |
        | km_per_year | Quantidade de Quilômetros percorridos a cada ano |
        | km_per_month | Quantidade de Quilômetros percorridos por mês |
        | company | Fabricante da Motocicleta |
    """
    col_2.markdown(data_description)

def create_answers_section(df):
    st.title("Main Questions Answers")

    st.header("First Round")
    st.subheader("How many bikes are being sold by their owners and how many bikes are being sold by distributors?")
    asw.rd1_question_9(df)

    st.subheader("How many bikes are being sold are bikes from a unique owner?")
    asw.rd1_question_13(df)

    st.subheader("Are high kilometer bikes more expensive than bikes with lower kilometer?")
    asw.rd1_question_14(df)

    st.subheader("Are the bikes with a unique owner more expensive on average than the other bikes?")
    asw.rd2_question_1(df)

    st.subheader("Are the bikes that have more owners also the bikes with more kilometers traveled on average?")
    asw.rd2_question_2(df)

    st.subheader("Which company has the most bikes registered?")
    asw.rd2_question_7(df)

    st.subheader("Which company has the most expensive bikes on average?")
    asw.rd3_question_2(df)

    st.subheader("Are the companies that have the most expensive bikes registered also the companies with the most bikes registered?")
    asw.rd3_question_5(df)

    st.subheader("Which bikes are good for buying?")
    asw.rd3_question_7(df)

def create_main_layout():
    df = load_data()
    create_dataframe_section(df)
    create_answers_section(df)

if __name__ == "__main__":
    create_main_layout()