import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO

st.title("📄 Gerador de Laudo PCD")

# ========================
# FORMULÁRIO
# ========================

servico_medico = st.text_input("Serviço Médico")
cnpj = st.text_input("CNPJ")
data = st.text_input("Data")

nome = st.text_input("Nome")
cpf = st.text_input("CPF")

cid_fisica = st.text_input("CID Física")
cid_visual = st.text_input("CID Visual/Auditiva")
descricao = st.text_area("Descrição")

nome_medico = st.text_input("Nome do médico")
responsavel_servico = st.text_input("Responsável do serviço")

especialidade = st.text_input("Especialidade")
cpf_medico = st.text_input("CPF do médico")

unidade = st.text_input("Unidade emissora")
cnpj_unidade = st.text_input("CNPJ unidade")

responsavel = st.text_input("Responsável")
cpf_responsavel = st.text_input("CPF responsável")

if st.button("Gerar PDF"):

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
        # Página 1
        "Text7": servico_medico,
        "Text8": cnpj,
        "Text9": data,
        "Text10": nome,
        "Text11": cpf,
        "Text12": cid_fisica,
        "Text13": cid_visual,
        "Text14": descricao,

        # Página 2
        "Text15": nome_medico,
        "Text16": responsavel_servico,
        "Text17": nome,
        "Text18": cpf,

        # Página 3
        "Text21": nome_medico,
        "Text22": cpf_medico,
        "Text23": especialidade,
        "Text25": unidade,
        "Text26": cnpj_unidade,
        "Text29": responsavel,
        "Text30": cpf_responsavel,
        "Text64": nome,
        "Text65": cpf,
        "Text66": "verdadeiras"
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
        "laudo_final.pdf",
        "application/pdf"
    )
