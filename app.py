import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import re
from datetime import datetime

st.set_page_config(page_title="Gerador de Laudo PCD", layout="centered")

st.title("📄 Gerador de Laudo PCD - Anexo Único")


# ========================
# FUNÇÕES
# ========================

def somente_numeros(valor):
    return re.sub(r"\D", "", valor or "")


def formatar_cpf(valor):
    v = somente_numeros(valor)[:11]

    if len(v) <= 3:
        return v
    elif len(v) <= 6:
        return f"{v[:3]}.{v[3:]}"
    elif len(v) <= 9:
        return f"{v[:3]}.{v[3:6]}.{v[6:]}"
    else:
        return f"{v[:3]}.{v[3:6]}.{v[6:9]}-{v[9:]}"


def formatar_cnpj(valor):
    v = somente_numeros(valor)[:14]

    if len(v) <= 2:
        return v
    elif len(v) <= 5:
        return f"{v[:2]}.{v[2:]}"
    elif len(v) <= 8:
        return f"{v[:2]}.{v[2:5]}.{v[5:]}"
    elif len(v) <= 12:
        return f"{v[:2]}.{v[2:5]}.{v[5:8]}/{v[8:]}"
    else:
        return f"{v[:2]}.{v[2:5]}.{v[5:8]}/{v[8:12]}-{v[12:]}"


def formatar_data(valor):
    v = somente_numeros(valor)[:8]

    if len(v) <= 2:
        return v
    elif len(v) <= 4:
        return f"{v[:2]}/{v[2:]}"
    else:
        return f"{v[:2]}/{v[2:4]}/{v[4:]}"


def validar_cpf(cpf):
    cpf = somente_numeros(cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = 11 - (soma % 11)
    dig1 = 0 if dig1 >= 10 else dig1

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = 11 - (soma % 11)
    dig2 = 0 if dig2 >= 10 else dig2

    return cpf[-2:] == f"{dig1}{dig2}"


def validar_cnpj(cnpj):
    cnpj = somente_numeros(cnpj)

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    dig1 = 11 - (soma % 11)
    dig1 = 0 if dig1 >= 10 else dig1

    soma = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    dig2 = 11 - (soma % 11)
    dig2 = 0 if dig2 >= 10 else dig2

    return cnpj[-2:] == f"{dig1}{dig2}"


def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def atualizar_cpf(campo):
    st.session_state[campo] = formatar_cpf(st.session_state[campo])


def atualizar_cnpj(campo):
    st.session_state[campo] = formatar_cnpj(st.session_state[campo])


def atualizar_data(campo):
    st.session_state[campo] = formatar_data(st.session_state[campo])


def check(valor):
    return "/Sim" if valor else "/Off"


def marcar_carater_visual(writer, carater):
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    c.setFont("Helvetica-Bold", 12)

    if carater == "Provisória":
        c.circle(280, 280, 5, fill=1)
    else:
        c.circle(420, 280, 5, fill=1)

    c.save()
    packet.seek(0)

    overlay = PdfReader(packet)
    writer.pages[0].merge_page(overlay.pages[0])


# ========================
# FORMULÁRIO
# ========================

st.subheader("1. Serviço Médico")

servico_medico = st.text_input("Serviço Médico / Unidade de Saúde")

cnpj = st.text_input(
    "CNPJ",
    key="cnpj",
    on_change=atualizar_cnpj,
    args=("cnpj",)
)

data = st.text_input(
    "Data",
    key="data",
    on_change=atualizar_data,
    args=("data",)
)

tipo_servico = st.selectbox(
    "Serviço médico prestado por:",
    [
        "",
        "pelo Departamento de Trânsito (Detran)",
        "por setor privado credenciado pelo Detran",
        "pelo serviço público de saúde",
        "por setor privado que integra o Sistema Único de Saúde (SUS)",
        "pelo serviço social autônomo",
    ],
)

st.subheader("2. Identificação do Requerente")

nome_requerente = st.text_input("Nome")

cpf_requerente = st.text_input(
    "CPF",
    key="cpf_requerente",
    on_change=atualizar_cpf,
    args=("cpf_requerente",)
)

st.subheader("3. Laudo de Avaliação")

cid_fisica = st.text_input("CID - Deficiência Física (*)")
cid_visual = st.text_input("CID - Deficiência Visual/Auditiva (*)")

carater = st.radio(
    "Caráter da deficiência",
    ["Provisória", "Permanente"],
    horizontal=True,
)

descricao = st.text_area("Descrição detalhada da deficiência")

st.subheader("4. Assinaturas")

nome_medico = st.text_input("Nome do médico")
assinatura_medico = st.text_input("Assinatura do médico")
responsavel_servico = st.text_input("Nome do responsável pelo serviço médico")
assinatura_responsavel_servico = st.text_input(
    "Assinatura do responsável pelo serviço médico"
)

st.subheader("5. Informações Complementares")

tem_def_fisica = st.checkbox("Pessoa com Deficiência Física")
tem_def_visual = st.checkbox("Pessoa com Deficiência Visual/Auditiva")

segmentos = st.multiselect(
    "Segmentos afetados",
    ["Cabeça", "Pescoço", "Tronco", "Membros Inferiores", "Membros Superiores"],
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
    ],
)

condicoes = st.multiselect(
    "Condições visual/auditiva",
    [
        "Acuidade visual / campo visual",
        "Perda auditiva bilateral",
    ],
)

st.subheader("6. Assinatura Final")

cpf_medico = st.text_input(
    "CPF do médico",
    key="cpf_medico",
    on_change=atualizar_cpf,
    args=("cpf_medico",)
)

especialidade = st.text_input("Especialidade")

unidade = st.text_input("Unidade Emissora do Laudo", value=servico_medico)

cnpj_unidade = st.text_input(
    "CNPJ da Unidade",
    key="cnpj_unidade",
    value=cnpj,
    on_change=atualizar_cnpj,
    args=("cnpj_unidade",)
)

responsavel_unidade = st.text_input("Responsável pela Unidade")

cpf_responsavel_unidade = st.text_input(
    "CPF do Responsável pela Unidade",
    key="cpf_responsavel_unidade",
    on_change=atualizar_cpf,
    args=("cpf_responsavel_unidade",)
)


# ========================
# GERAR PDF
# ========================

if st.button("Gerar PDF"):

    erros = []

    if not validar_cnpj(cnpj):
        erros.append("CNPJ principal inválido.")

    if not validar_data(data):
        erros.append("Data inválida. Use uma data real no formato dd/mm/aaaa.")

    if not validar_cpf(cpf_requerente):
        erros.append("CPF do requerente inválido.")

    if cpf_medico and not validar_cpf(cpf_medico):
        erros.append("CPF do médico inválido.")

    if not validar_cnpj(cnpj_unidade):
        erros.append("CNPJ da unidade inválido.")

    if cpf_responsavel_unidade and not validar_cpf(cpf_responsavel_unidade):
        erros.append("CPF do responsável pela unidade inválido.")

    if erros:
        for erro in erros:
            st.error(erro)
        st.stop()

    reader = PdfReader("Anexo Unico.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    if "/AcroForm" in reader.trailer["/Root"]:
        writer._root_object.update(
            {NameObject("/AcroForm"): reader.trailer["/Root"]["/AcroForm"]}
        )
        writer._root_object["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)}
        )

    campos = {
        # Página 1
        "Text7": servico_medico,
        "Text8": cnpj,
        "Text9": data,
        "Text10": nome_requerente,
        "Text11": cpf_requerente,
        "Text12": cid_fisica,
        "Text13": cid_visual,
        "Text14": descricao,

        # Página 2 - 3. Assinaturas
        "Text15": nome_medico,
        "Text16": assinatura_medico,
        "Text17": responsavel_servico,
        "Text18": assinatura_responsavel_servico,

        # Página 2 - 4.1 Identificação do requerente
        "Text19": nome_requerente,
        "Text20": cpf_requerente,

        # Página 3 - 4.4 Assinaturas
        "Text21": nome_medico,
        "Text22": assinatura_medico,
        "Text23": responsavel_servico,
        "Text24": assinatura_responsavel_servico,

        # Página 3 - 4.5 Declaração
        "Text64": nome_requerente,
        "Text65": cpf_requerente,
        "Text66": "verdadeiras",

        # Página 3 - 4.6 Assinatura final
        "Text25": nome_medico,
        "Text26": cpf_medico,
        "Text27": especialidade,
        "Text28": assinatura_medico,
        "Text29": unidade,
        "Text30": cnpj_unidade,
        "Text31": responsavel_unidade,
        "Text32": cpf_responsavel_unidade,

        # Checkboxes página 1
        "Check Box34": check(tipo_servico == "pelo Departamento de Trânsito (Detran)"),
        "Check Box35": check(tipo_servico == "por setor privado credenciado pelo Detran"),
        "Check Box36": check(tipo_servico == "pelo serviço público de saúde"),
        "Check Box37": check(tipo_servico == "por setor privado que integra o Sistema Único de Saúde (SUS)"),
        "Check Box38": check(tipo_servico == "pelo serviço social autônomo"),

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

    marcar_carater_visual(writer, carater)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("PDF gerado com sucesso!")

    st.download_button(
        "📥 Baixar PDF",
        output,
        "laudo_pcd_preenchido.pdf",
        "application/pdf",
    )
