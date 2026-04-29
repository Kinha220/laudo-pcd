import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO

st.title("🧪 Mapeador de campos do PDF")

if st.button("Gerar PDF com nomes dos campos"):

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

    campos = {}

    # Preenche todos os campos de texto com o próprio nome
    for i in range(7, 34):
        campos[f"Text{i}"] = f"Text{i}"

    campos["Text64"] = "Text64"
    campos["Text65"] = "Text65"
    campos["Text66"] = "Text66"

    # Teste do caráter da deficiência
    campos["Group40"] = "/Permanente"

    for i in range(len(writer.pages)):
        writer.update_page_form_field_values(writer.pages[i], campos)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.download_button(
        "📥 Baixar PDF mapeado",
        data=output,
        file_name="mapa_campos.pdf",
        mime="application/pdf"
    )
