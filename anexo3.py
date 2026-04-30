import streamlit as st
from pypdf import PdfReader

st.title("🔎 Leitor de campos preenchidos - Anexo III")

arquivo = st.file_uploader(
    "Envie aqui o PDF já preenchido manualmente",
    type=["pdf"]
)

if arquivo is not None:
    reader = PdfReader(arquivo)
    campos = reader.get_fields()

    if not campos:
        st.error("Nenhum campo editável encontrado.")
    else:
        st.success(f"Foram encontrados {len(campos)} campos.")

        for nome_campo, info in campos.items():
            tipo = info.get("/FT", "")
            valor = info.get("/V", "")

            if valor:
                st.write("---------------")
                st.write(f"📌 Campo interno: `{nome_campo}`")
                st.write(f"🔠 Tipo: `{tipo}`")
                st.write(f"📝 Valor preenchido: `{valor}`")
