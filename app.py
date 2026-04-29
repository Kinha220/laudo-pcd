import streamlit as st
from pypdf import PdfReader

st.title("🔎 Descobrir valores dos Checkboxes")

reader = PdfReader("Anexo Unico.pdf")
fields = reader.get_fields()

for nome, campo in fields.items():
    if campo.get("/FT") == "/Btn":
        st.write("---------------")
        st.write("📌 Campo:", nome)
        st.write("Valor atual:", campo.get("/V"))
        st.write("Opções internas:", campo.get("/_States_"))
