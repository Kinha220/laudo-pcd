import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO

st.title("🧪 Teste de preenchimento dos campos do PDF")

nome = st.text_input("Nome")
cpf = st.text_input("CPF")

if st.button("Gerar PDF teste"):

    reader = PdfReader("Anexo Unico.pdf")
    writer = PdfWriter()

    # Copia todas as páginas
    for page in reader.pages:
        writer.add_page(page)

    # Copia o formulário interno do PDF
    if "/AcroForm" in reader.trailer["/Root"]:
        writer._root_object.update({
            NameObject("/AcroForm"): reader.trailer["/Root"]["/AcroForm"]
        })
        writer._root_object["/AcroForm"].update({
            NameObject("/NeedAppearances"): BooleanObject(True)
        })

    campos = {
        "Text7": nome,
        "Text8": cpf,
        "Text9": "TESTE CAMPO 9",
        "Text10": "TESTE CAMPO 10",
        "Text11": "TESTE CAMPO 11"
    }

    for i in range(len(writer.pages)):
        writer.update_page_form_field_values(writer.pages[i], campos)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("PDF gerado!")

    st.download_button(
        "📥 Baixar PDF teste",
        data=output,
        file_name="teste_campos.pdf",
        mime="application/pdf"
    )
