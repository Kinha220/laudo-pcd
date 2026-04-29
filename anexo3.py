import streamlit as st
from pypdf import PdfReader

st.title("🔎 Mapeamento do Anexo III")

reader = PdfReader("Anexo III - PCAT 18-2013.pdf")

for i, page in enumerate(reader.pages):
    st.subheader(f"Página {i + 1}")

    if "/Annots" in page:
        for annot in page["/Annots"]:
            obj = annot.get_object()

            nome = obj.get("/T")
            tipo = obj.get("/FT")
            valor = obj.get("/V")
            opcoes = obj.get("/_States_")

            if nome:
                st.write("---------------")
                st.write("Campo:", nome)
                st.write("Tipo:", tipo)
                st.write("Valor atual:", valor)
                st.write("Opções:", opcoes)
    else:
        st.write("Sem campos editáveis nesta página.")
