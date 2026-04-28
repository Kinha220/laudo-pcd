import streamlit as st
from pypdf import PdfReader, PdfWriter
from io import BytesIO

st.title("Teste de campos do PDF")

nome = st.text_input("Nome")
cpf = st.text_input("CPF")

if st.button("Testar preenchimento"):

    reader = PdfReader("Anexo Unico.pdf")
    writer = PdfWriter()

    writer.append_pages_from_reader(reader)

    # TESTE EM ALGUNS CAMPOS
    writer.update_page_form_field_values(
        writer.pages[0],
        {
            "Text7": nome,
            "Text8": cpf,
            "Text9": "TESTE",
            "Text10": "TESTE 2"
        }
    )

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.download_button(
        "Baixar PDF teste",
        output,
        "teste_campos.pdf",
        "application/pdf"
    )
