import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO

st.title("📄 Gerador de Laudo PCD")

# FORMULÁRIO
servico_medico = st.text_input("Serviço Médico / Unidade de Saúde")
cnpj = st.text_input("CNPJ")
data = st.text_input("Data")

nome = st.text_input("Nome")
cpf = st.text_input("CPF")

if st.button("Gerar PDF"):

    reader = PdfReader("Anexo Unico.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # Mantém os campos do PDF
    if "/AcroForm" in reader.trailer["/Root"]:
        writer._root_object.update({
            NameObject("/AcroForm"): reader.trailer["/Root"]["/AcroForm"]
        })
        writer._root_object["/AcroForm"].update({
            NameObject("/NeedAppearances"): BooleanObject(True)
        })

    campos = {
        "Text7": servico_medico,
        "Text8": cnpj,
        "Text9": data,
        "Text10": nome,
        "Text11": cpf
    }

    for i in range(len(writer.pages)):
        writer.update_page_form_field_values(writer.pages[i], campos)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("PDF gerado com sucesso!")

    st.download_button(
        "📥 Baixar PDF",
        output,
        "laudo_pcd.pdf",
        "application/pdf"
    )
