import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO

st.title("📄 Anexo III - PCD")

nome = st.text_input("Nome")
data_nasc = st.text_input("Data de nascimento")
rg = st.text_input("RG")
orgao = st.text_input("Órgão emissor")
uf = st.text_input("UF")
mae = st.text_input("Mãe")
pai = st.text_input("Pai")
sexo = st.radio("Sexo", ["Masculino", "Feminino"])

def check(valor):
    return "/Sim" if valor else "/Off"

if st.button("Gerar PDF"):

    reader = PdfReader("Anexo III - PCAT 18-2013.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # ESSENCIAL: copia o formulário interno
    if "/AcroForm" in reader.trailer["/Root"]:
        writer._root_object.update({
            NameObject("/AcroForm"): reader.trailer["/Root"]["/AcroForm"]
        })
        writer._root_object["/AcroForm"].update({
            NameObject("/NeedAppearances"): BooleanObject(True)
        })

    dados = {
        "text_1aain": nome,
        "text_2vzkg": data_nasc,
        "text_3fmsf": rg,
        "text_4uvdc": orgao,
        "text_5xlcb": uf,
        "text_8ylvx": mae,
        "text_10mrxo": pai,
        "checkbox_16fqts": check(sexo == "Masculino"),
        "checkbox_17tlov": check(sexo == "Feminino"),
    }

    for page in writer.pages:
        writer.update_page_form_field_values(page, dados)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("PDF gerado com sucesso!")

    st.download_button(
        "📥 Baixar PDF",
        output,
        "anexo3_preenchido.pdf",
        "application/pdf"
    )
