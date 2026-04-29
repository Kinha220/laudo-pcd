import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO

st.set_page_config(page_title="Gerador de Laudo PCD", layout="centered")

st.title("📄 Gerador de Laudo PCD - Anexo Único")

# =========================
# DADOS PRINCIPAIS
# =========================

st.subheader("1. Serviço Médico")

servico_medico = st.text_input("Serviço Médico / Unidade de Saúde")
cnpj = st.text_input("CNPJ")
data = st.text_input("Data")

tipo_servico = st.selectbox(
    "Este serviço médico é prestado por:",
    [
        "",
        "Departamento de Trânsito (Detran)",
        "Setor privado credenciado pelo Detran",
        "Serviço público de saúde",
        "Setor privado que integra o SUS",
        "Serviço social autônomo",
    ]
)

st.subheader("2. Identificação do Requerente")

nome = st.text_input("Nome")
cpf = st.text_input("CPF")

st.subheader("3. Laudo de Avaliação")

cid_fisica = st.text_input("CID - Deficiência Física")
cid_visual_auditiva = st.text_input("CID - Deficiência Visual/Auditiva")

carater = st.radio(
    "Caráter da deficiência",
    ["", "Provisória", "Permanente"],
    horizontal=True
)

descricao = st.text_area("Descrição detalhada da deficiência")

st.subheader("4. Assinaturas")

nome_medico = st.text_input("Nome do médico")
responsavel_servico = st.text_input("Nome do responsável pelo serviço médico/unidade de saúde")

st.subheader("5. Informações Complementares")

nome_comp = st.text_input("Nome - Informações complementares", value=nome)
cpf_comp = st.text_input("CPF - Informações complementares", value=cpf)

tem_def_fisica = st.checkbox("Pessoa com Deficiência Física")
tem_def_visual_auditiva = st.checkbox("Pessoa com Deficiência Visual/Auditiva")

segmentos = st.multiselect(
    "Segmentos do corpo humano",
    ["Cabeça", "Pescoço", "Tronco", "Membros Inferiores", "Membros Superiores"]
)

formas = st.multiselect(
    "Forma da deficiência física",
    [
        "Paraplegia",
        "Monoparesia",
        "Triplegia",
        "Hemiparesia",
        "Paralisia Cerebral",
        "Paraparesia",
        "Tetraplegia",
        "Triparesia",
        "Ostomia",
        "Nanismo",
        "Monoplegia",
        "Tetraparesia",
        "Hemiplegia",
        "Amputação ou Ausência de Membro",
        "Deformidade congênita/adquirida",
    ]
)

condicoes_visual_auditiva = st.multiselect(
    "Condições visual/auditiva",
    [
        "Acuidade visual / campo visual",
        "Perda auditiva bilateral",
    ]
)

st.subheader("6. Declaração e Assinatura Final")

nome_paciente_decl = st.text_input("Nome do paciente na declaração", value=nome)
cpf_paciente_decl = st.text_input("CPF do paciente na declaração", value=cpf)
texto_declaracao = st.text_input("Complemento da declaração", value="verdadeiras")

nome_medico_final = st.text_input("Nome do médico - assinatura final", value=nome_medico)
cpf_medico = st.text_input("CPF do médico")
especialidade = st.text_input("Especialidade")
unidade_emissora = st.text_input("Unidade Emissora do Laudo", value=servico_medico)
cnpj_unidade = st.text_input("CNPJ da Unidade Emissora", value=cnpj)
responsavel_unidade = st.text_input("Responsável pela Unidade")
cpf_responsavel = st.text_input("CPF do Responsável")


def marcar_checkbox(valor):
    return "/Sim" if valor else "/Off"


if st.button("Gerar PDF preenchido"):

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

    campos_texto = {
        # Página 1
        "Text7": servico_medico,
        "Text8": cnpj,
        "Text9": data,
        "Text10": nome,
        "Text11": cpf,
        "Text12": cid_fisica,
        "Text13": cid_visual_auditiva,
        "Text14": descricao,

        # Página 2
        "Text15": nome_medico,
        "Text16": responsavel_servico,
        "Text17": nome_comp,
        "Text18": cpf_comp,

        # Página 3
        "Text21": nome_medico_final,
        "Text22": cpf_medico,
        "Text23": especialidade,
        "Text25": unidade_emissora,
        "Text26": cnpj_unidade,
        "Text29": responsavel_unidade,
        "Text30": cpf_responsavel,
        "Text64": nome_paciente_decl,
        "Text65": cpf_paciente_decl,
        "Text66": texto_declaracao,
    }

    campos_checkbox = {
        # Tipo de serviço - Página 1
        "Check Box34": marcar_checkbox(tipo_servico == "Departamento de Trânsito (Detran)"),
        "Check Box35": marcar_checkbox(tipo_servico == "Setor privado credenciado pelo Detran"),
        "Check Box36": marcar_checkbox(tipo_servico == "Serviço público de saúde"),
        "Check Box37": marcar_checkbox(tipo_servico == "Setor privado que integra o SUS"),
        "Check Box38": marcar_checkbox(tipo_servico == "Serviço social autônomo"),

        # Página 2
        "Check Box42": marcar_checkbox(tem_def_fisica),

        "Check Box43": marcar_checkbox("Cabeça" in segmentos),
        "Check Box44": marcar_checkbox("Pescoço" in segmentos),
        "Check Box45": marcar_checkbox("Tronco" in segmentos),
        "Check Box46": marcar_checkbox("Membros Inferiores" in segmentos),
        "Check Box47": marcar_checkbox("Membros Superiores" in segmentos),

        "Check Box48": marcar_checkbox("Paraplegia" in formas),
        "Check Box49": marcar_checkbox("Monoparesia" in formas),
        "Check Box50": marcar_checkbox("Triplegia" in formas),
        "Check Box51": marcar_checkbox("Hemiparesia" in formas),
        "Check Box52": marcar_checkbox("Paralisia Cerebral" in formas),

        "Check Box53": marcar_checkbox("Paraparesia" in formas),
        "Check Box54": marcar_checkbox("Tetraplegia" in formas),
        "Check Box55": marcar_checkbox("Triparesia" in formas),
        "Check Box56": marcar_checkbox("Ostomia" in formas),
        "Check Box57": marcar_checkbox("Nanismo" in formas),

        "Check Box58": marcar_checkbox("Monoplegia" in formas),
        "Check Box59": marcar_checkbox("Tetraparesia" in formas),
        "Check Box60": marcar_checkbox("Hemiplegia" in formas),
        "Check Box61": marcar_checkbox("Amputação ou Ausência de Membro" in formas),

        "Check Box67": marcar_checkbox("Deformidade congênita/adquirida" in formas),

        "Check Box62": marcar_checkbox("Acuidade visual / campo visual" in condicoes_visual_auditiva),
        "Check Box63": marcar_checkbox("Perda auditiva bilateral" in condicoes_visual_auditiva),
    }

    todos_campos = {}
    todos_campos.update(campos_texto)
    todos_campos.update(campos_checkbox)

    for i in range(len(writer.pages)):
        writer.update_page_form_field_values(writer.pages[i], todos_campos)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("PDF gerado com sucesso!")

    st.download_button(
        "📥 Baixar PDF preenchido",
        data=output,
        file_name=f"Laudo_PCD_{nome}.pdf",
        mime="application/pdf"
    )
