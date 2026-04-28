import streamlit as st
from pypdf import PdfReader

st.title("🔎 Leitor de campos do PDF")

arquivo = st.selectbox(
    "Escolha o PDF",
    ["Anexo Unico.pdf", "Anexo III - PCAT 18-2013.pdf"]
)

reader = PdfReader(arquivo)
fields = reader.get_fields()

if fields:
    st.success(f"Foram encontrados {len(fields)} campos editáveis.")

    for nome_campo, info in fields.items():
        st.write("📌", nome_campo)
else:
    st.error("Esse PDF não possui campos editáveis detectáveis pelo Python.")
