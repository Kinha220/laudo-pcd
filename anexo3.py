import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO

st.title("📄 Anexo III - PCD")

# ===== INPUTS =====
nome = st.text_input("Nome")
data_nasc = st.text_input("Data de nascimento")
rg = st.text_input("RG")
orgao = st.text_input("Órgão emissor")
uf = st.text_input("UF")
mae = st.text_input("Mãe")
pai = st.text_input("Pai")
responsavel = st.text_input("Responsável")

sexo = st.radio("Sexo", ["Masculino", "Feminino"])

patologias = st.text_input("Patologias")
sequelas = st.text_input("Sequelas")
movimentos = st.text_input("Limitação dos movimentos")
decorrente = st.text_area("Decorrente de")

nome_medico = st.text_input("Nome do Médico")
especialidade = st.text_input("Especialidade")
nome_medico2 = st.text_input("Nome do Médico 2")
especialidade2 = st.text_input("Especialidade 2")

unidade = st.text_input("Unidade")
cnpj = st.text_input("CNPJ")
resp_unidade = st.text_input("Responsável unidade")
cpf_resp = st.text_input("CPF responsável")

# ======================
# FUNÇÃO RADIO (SEXO)
# ======================

def sexo_valor(sexo):
    if sexo == "Masculino":
        return {
            "radio_group_7zabh": "/Value_jipa",
            "radio_group_8lhuk": "/Off"
        }
    else:
        return {
            "radio_group_7zabh": "/Off",
            "radio_group_8lhuk": "/Value_zjcr"
        }

# ======================
# GERAR PDF
# ======================

if st.button("Gerar PDF"):

    reader = PdfReader("Anexo III - PCAT 18-2013.pdf")
    writer = PdfWriter()

    writer.clone_reader_document_root(reader)

    if "/AcroForm" in writer._root_object:
        writer._root_object["/AcroForm"].update({
            NameObject("/NeedAppearances"): BooleanObject(True)
        })

    campos = {
        # IDENTIFICAÇÃO
        "text_2omgi": nome,
        "text_3qmhu": data_nasc,
        "text_4iybw": rg,
        "text_5ihyi": orgao,
        "text_6bofk": uf,
        "text_9tdmv": mae,
        "text_10hwgs": pai,
        "text_11ojru": responsavel,

        # LAUDO
        "text_12ektp": patologias,
        "text_13pwjh": sequelas,
        "text_16nlvk": movimentos,
        "textarea_18znhl": decorrente,

        # MÉDICOS
        "text_19btld": nome_medico,
        "text_20cvcp": especialidade,
        "text_21neei": nome_medico2,
        "text_22phwu": especialidade2,

        # UNIDADE
        "text_23qetd": unidade,
        "text_25khyd": cnpj,
        "text_24ttbs": resp_unidade,
        "text_26rhjh": cpf_resp,

        # REQUERENTE (página 2)
        "text_31gqik": nome,
        "text_32s": cpf_resp,
    }

    # adiciona sexo (radio)
    campos.update(sexo_valor(sexo))

    for page in writer.pages:
        writer.update_page_form_field_values(page, campos)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("PDF gerado com sucesso!")

    st.download_button(
        "📥 Baixar PDF",
        output,
        "anexo3_final.pdf",
        "application/pdf"
    )
