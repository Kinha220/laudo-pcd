import streamlit as st
from pypdf import PdfReader

st.title("🔎 Diagnóstico do PDF")

reader = PdfReader("Anexo III - PCAT 18-2013.pdf")

st.write("Tem AcroForm?", "/AcroForm" in reader.trailer["/Root"])

fields = reader.get_fields()
st.write("Campos detectados:", fields)

for i, page in enumerate(reader.pages):
    st.subheader(f"Página {i+1}")
    st.write("Tem Annots?", "/Annots" in page)
    if "/Annots" in page:
        st.write(page["/Annots"])
