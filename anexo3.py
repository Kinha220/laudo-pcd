import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO

st.title("🧪 Teste Anexo III - Clone completo")

nome = st.text_input("Nome", "TESTE NOME")
data = st.text_input("Data", "29/04/2026")
cpf = st.text_input("CPF", "123.456.789-00")

if st.button("Gerar teste"):

    reader = PdfReader("Anexo III - PCAT 18-2013.pdf")
    writer = PdfWriter()

    # 🔥 copia o PDF inteiro com estrutura interna
    writer.clone_reader_document_root(reader)

    # força aparência dos campos
    if "/AcroForm" in writer._root_object:
        writer._root_object["/AcroForm"].update({
            NameObject("/NeedAppearances"): BooleanObject(True)
        })

    campos = {
        "text_1aain": nome,
        "text_2vzkg": data,
        "text_3fmsf": cpf,
    }

    for page in writer.pages:
        writer.update_page_form_field_values(page, campos)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.download_button(
        "📥 Baixar PDF teste",
        output,
        "anexo3_teste_clone.pdf",
        "application/pdf"
    )
