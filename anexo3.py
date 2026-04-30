import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO

st.set_page_config(page_title="Anexo III - PCAT 18/2013", layout="centered")

st.title("📄 Anexo III - PCAT 18/2013")

# =====================
# FORMULÁRIO
# =====================

st.subheader("1. Identificação do Requerente")

data_emissao = st.text_input("Data de emissão")
nome = st.text_input("Nome")
data_nascimento = st.text_input("Data de nascimento")
sexo = st.radio("Sexo", ["Masculino", "Feminino"], horizontal=True)

identidade = st.text_input("Identidade nº")
orgao_emissor = st.text_input("Órgão emissor")
uf = st.text_input("UF")
mae = st.text_input("Mãe")
pai = st.text_input("Pai")
responsavel_legal = st.text_input("Responsável / Representante legal")

st.subheader("2. Laudo Pericial")

patologia_fisica = st.text_input("Deficiência física - Patologias")
sequela_fisica = st.text_input("Deficiência física - Sequelas")

patologia_visual = st.text_input("Deficiência visual - Patologias")
sequela_visual = st.text_input("Deficiência visual - Sequelas")

movimentos = st.text_input("Limitação dos movimentos de")
decorrente = st.text_input("Decorrente de")

membro_superior_esquerdo = st.checkbox("Membro superior esquerdo")
membro_superior_direito = st.checkbox("Membro superior direito")
membro_inferior_esquerdo = st.checkbox("Membro inferior esquerdo")
membro_inferior_direito = st.checkbox("Membro inferior direito")

st.subheader("3. Médicos e Unidade Emissora")

nome_medico_1 = st.text_input("Nome do médico 1")
especialidade_1 = st.text_input("Especialidade médico 1")

nome_medico_2 = st.text_input("Nome do médico 2")
especialidade_2 = st.text_input("Especialidade médico 2")

unidade = st.text_input("Unidade Emissora do Laudo")
cnpj = st.text_input("CNPJ")
responsavel = st.text_input("Responsável")
cpf_responsavel = st.text_input("CPF responsável")

# =====================
# FUNÇÕES
# =====================

def valor_checkbox(nome_campo, marcado):
    valores = {
        "checkbox_16fqts": "/Yes_wqrt",
        "checkbox_17tlov": "/Yes_hyik",
        "checkbox_18zbja": "/Yes_vmc",
        "checkbox_19wnum": "/Yes_uvoj",
        "checkbox_111xjey": "/Yes_kcbz",
        "checkbox_112eml": "/Yes_yzh",
    }

    if not marcado:
        return "/Off"

    return valores.get(nome_campo, "/Yes")


# =====================
# GERAR PDF
# =====================

if st.button("Gerar Anexo III"):

    reader = PdfReader("Anexo III - PCAT 18-2013.pdf")
    writer = PdfWriter()

    writer.clone_reader_document_root(reader)

    if "/AcroForm" in writer._root_object:
        writer._root_object["/AcroForm"].update({
            NameObject("/NeedAppearances"): BooleanObject(True)
        })

    campos = {
        # Página 1 - Identificação
        "text_113jmbp": data_emissao,
        "text_1aain": nome,
        "text_2vzkg": data_nascimento,
        "text_3fmsf": identidade,
        "text_4uvdc": orgao_emissor,
        "text_5xlcb": uf,
        "text_8ylvx": mae,
        "text_10mrxo": pai,
        "text_11yhb": responsavel_legal,

        # Sexo
        "checkbox_111xjey": valor_checkbox("checkbox_111xjey", sexo == "Masculino"),
        "checkbox_112eml": valor_checkbox("checkbox_112eml", sexo == "Feminino"),

        # Página 1 - Laudo Pericial
        "text_12xfw": patologia_fisica,
        "text_14amyd": sequela_fisica,
        "text_13wate": patologia_visual,
        "text_15vxpx": sequela_visual,

        # Membros
        "checkbox_16fqts": valor_checkbox("checkbox_16fqts", membro_superior_esquerdo),
        "checkbox_17tlov": valor_checkbox("checkbox_17tlov", membro_superior_direito),
        "checkbox_18zbja": valor_checkbox("checkbox_18zbja", membro_inferior_esquerdo),
        "checkbox_19wnum": valor_checkbox("checkbox_19wnum", membro_inferior_direito),

        "text_21lsif": movimentos,
        "text_23zdpk": decorrente,

        # Página 1 - Médicos e unidade
        "text_24ezmf": nome_medico_1,
        "text_25lnty": especialidade_1,
        "text_26fdqd": nome_medico_2,
        "text_27ey": especialidade_2,
        "text_28bslb": unidade,
        "text_30jooj": cnpj,
        "text_29lviz": responsavel,
        "text_31tqp": cpf_responsavel,

        # Página 2 - Identificação repetida
        "text_32ktxf": nome,
        "text_33ybmg": cpf_responsavel,
    }

    for page in writer.pages:
        writer.update_page_form_field_values(page, campos)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("Anexo III gerado com sucesso!")

    st.download_button(
        "📥 Baixar Anexo III preenchido",
        output,
        "anexo3_preenchido.pdf",
        "application/pdf"
    )
