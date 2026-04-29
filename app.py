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
        tipo = info.get("/FT", "")
        valor = info.get("/V", "")
        opcoes = info.get("/Opt", "")

        st.write("---------------")
        st.write("📌 Campo:", nome_campo)
        st.write("Tipo:", tipo)
        st.write("Valor atual:", valor)
        st.write("Opções:", opcoes)
else:
    st.error("Esse PDF não possui campos editáveis detectáveis.")
