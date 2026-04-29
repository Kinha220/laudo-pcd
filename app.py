import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO

st.title("Teste Provisória/Permanente")

opcao = st.radio(
    "Escolha o teste",
    ["/Escolha1", "/Escolha2"]
)

if st.button("Gerar teste"):

    reader = PdfReader("Anexo Unico.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    if "/AcroForm" in reader.trailer["/Root"]:
        writer._root_object.update({
            NameObject("/AcroForm"): reader.trailer["/Root"]["/AcroForm"]
        })
        writer._root_object["/AcroForm"].update({
            NameObject("/NeedAppearances"): BooleanObject(True)
        })

    campos = {
        "Group40": opcao
    }

    for page in writer.pages:
        writer.update_page_form_field_values(page, campos)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.download_button(
        "Baixar PDF teste",
        output,
        f"teste_{opcao.replace('/', '')}.pdf",
        "application/pdf"
    )
