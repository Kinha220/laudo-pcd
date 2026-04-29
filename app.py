import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

st.set_page_config(page_title="Gerador de Laudo PCD", layout="centered")

st.title("📄 Gerador de Laudo PCD - Anexo Único")

# ========================
# DADOS PRINCIPAIS
# ========================

st.subheader("1. Serviço Médico")
servico_medico = st.text_input("Serviço Médico / Unidade de Saúde")
cnpj = st.text_input("CNPJ")
data = st.text_input("Data")

tipo_servico = st.selectbox(
    "Serviço médico prestado por:",
    [
        "",
        "Detran",
        "Privado credenciado pelo Detran",
        "Serviço público de saúde",
        "Privado que integra o SUS",
        "Serviço social autônomo"
    ]
)

st.subheader("2. Identificação do Requerente")
nome = st.text_input("Nome")
cpf = st.text_input("CPF")

st.subheader("3. Laudo de Avaliação")
cid_fisica = st.text_input("CID - Deficiência Física")
cid_visual = st.text_input("CID - Deficiência Visual/Auditiva")

carater = st.radio(
    "Caráter da deficiência",
    ["Provisória", "Permanente"],
    horizontal=True
)

descricao = st.text_area("Descrição detalhada da deficiência")

st.subheader("4. Assinaturas")
nome_medico = st.text_input("Nome do médico")
responsavel_servico = st.text_input("Nome do responsável pelo serviço médico")

st.subheader("5. Informações Complementares")

tem_def_fisica = st.checkbox("Pessoa com Deficiência Física")
tem_def_visual = st.checkbox("Pessoa com Deficiência Visual/Auditiva")

segmentos = st.multiselect(
    "Segmentos afetados",
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
        "Deformidade congênita/adquirida"
    ]
)

condicoes = st.multiselect(
    "Condições visual/auditiva",
    [
        "Acuidade visual / campo visual",
        "Perda auditiva bilateral"
    ]
)

st.subheader("6. Assinatura Final")
cpf_medico = st.text_input("CPF do médico")
especialidade = st.text_input("Especialidade")
unidade = st.text_input("Unidade Emissora do Laudo", value=servico_medico)
cnpj_unidade = st.text_input("CNPJ da Unidade", value=cnpj)
responsavel = st.text_input("Responsável pela Unidade")
cpf_responsavel = st.text_input("CPF do Responsável")


def check(valor):
    return "/Sim" if valor else "/Off"


def marcar_carater_visual(writer, carater):
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)

    c.setFont("Helvetica-Bold", 12)

    # Ajuste fino do X:
    # Primeiro número = esquerda/direita
    # Segundo número = sobe/desce
    if carater == "Provisória":
        c.drawString(302, 213, "X")
    else:
        c.drawString(418, 213, "X")

    c.save()
    packet.seek(0)

    overlay = PdfReader(packet)
    writer.pages[0].merge_page(overlay.pages[0])


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
        "Text19": nome,
        "Text20": cpf,

        # Página 3
        "Text21": nome_medico,
        "Text22": cpf_medico,
        "Text23": especialidade,
        "Text25": unidade,
        "Text26": cnpj_unidade,
        "Text29": "",
        "Text30": "",
        "Text31": responsavel,
        "Text32": cpf_responsavel,
        "Text64": nome,
        "Text65": cpf,
        "Text66": "verdadeiras",

        # Checkboxes página 1
        "Check Box34": check(tipo_servico == "Detran"),
        "Check Box35": check(tipo_servico == "Privado credenciado pelo Detran"),
        "Check Box36": check(tipo_servico == "Serviço público de saúde"),
        "Check Box37": check(tipo_servico == "Privado que integra o SUS"),
        "Check Box38": check(tipo_servico == "Serviço social autônomo"),

        # Checkboxes página 2
        "Check Box42": check(tem_def_fisica),

        "Check Box43": check("Cabeça" in segmentos),
        "Check Box44": check("Pescoço" in segmentos),
        "Check Box45": check("Tronco" in segmentos),
        "Check Box46": check("Membros Inferiores" in segmentos),
        "Check Box47": check("Membros Superiores" in segmentos),

        "Check Box48": check("Paraplegia" in formas),
        "Check Box49": check("Monoparesia" in formas),
        "Check Box50": check("Triplegia" in formas),
        "Check Box51": check("Hemiparesia" in formas),
        "Check Box52": check("Paralisia Cerebral" in formas),
        "Check Box53": check("Paraparesia" in formas),
        "Check Box54": check("Tetraplegia" in formas),
        "Check Box55": check("Triparesia" in formas),
        "Check Box56": check("Ostomia" in formas),
        "Check Box57": check("Nanismo" in formas),
        "Check Box58": check("Monoplegia" in formas),
        "Check Box59": check("Tetraparesia" in formas),
        "Check Box60": check("Hemiplegia" in formas),
        "Check Box61": check("Amputação ou Ausência de Membro" in formas),
        "Check Box67": check("Deformidade congênita/adquirida" in formas),

        "Check Box62": check("Acuidade visual / campo visual" in condicoes),
        "Check Box63": check("Perda auditiva bilateral" in condicoes),
    }

    for page in writer.pages:
        writer.update_page_form_field_values(page, campos)

    # Marca Provisória/Permanente com X visual
    marcar_carater_visual(writer, carater)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("PDF gerado com sucesso!")

    st.download_button(
        "📥 Baixar PDF",
        output,
        "laudo_pcd_preenchido.pdf",
        "application/pdf"
    )
