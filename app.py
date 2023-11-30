import streamlit as st

st.title("Calculadora")
st.text("Insira dois números.")

num1 = st.number_input("Digite o primeiro número: ")
num2 = st.number_input("Digite o segundo número: ")

if st.button("Adição"):
    result = num1 + num2
    st.text("Resultado da adição:")
    st.title(result)
if st.button("Subtração"):
    result = num1 - num2
    st.text("Resultado da subtração:")
    st.title(result)
if st.button("Multiplicação"):
    result = num1 * num2
    st.text("Resultado da multiplicação:")
    st.title(result)
if st.button("Divisão"):
    result = num1 / num2
    st.text("Resultado da divisão:")
    st.title(result)
if st.button("Exponenciação"):
    result = num1 ** num2
    st.text("Resultado da exponenciação:")
    st.title(result)

