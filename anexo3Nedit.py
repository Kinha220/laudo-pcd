import streamlit as st
from io import BytesIO
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

st.set_page_config(page_title="Anexo III - PDF Fixo", layout="centered")
st.title("📄 Gerador Anexo III - PDF não editável")

# =========================
# FORMULÁRIO
# =========================

with st.expander("1. Identificação", expanded=True):
    data_emissao = st.text_input("Data de emissão", placeholder="20/02/26")
    nome = st.text_input("Nome")
    cpf = st.text_input("CPF")
    data_nascimento = st.text_input("Data de nascimento")
    identidade = st.text_input("Identidade nº")
    orgao_emissor = st.text_input("Órgão emissor")
    uf = st.text_input("UF")
    mae = st.text_input("Mãe")
    pai = st.text_input("Pai")
    responsavel_legal = st.text_input("Responsável legal")
    sexo = st.radio("Sexo", [ "Masculino", "Feminino"], horizontal=True)

with st.expander("2. Laudo pericial", expanded=True):
    cid_fisica = st.text_input("CID - Deficiência Física")
    sequelas_fisica = st.text_input("Sequelas - Deficiência Física")
    cid_visual = st.text_input("CID - Deficiência Visual")
    sequelas_visual = st.text_input("Sequelas - Deficiência Visual")
    lado_superior_esquerdo = st.checkbox("Superior esquerdo")
    lado_superior_direito = st.checkbox("Superior direito")
    lado_inferior_esquerdo = st.checkbox("Inferior esquerdo")
    lado_inferior_direito = st.checkbox("Inferior direito")
    limitacao_movimentos = st.text_input("Limitação dos movimentos")
    decorrente_de = st.text_area("Decorrente de")

with st.expander("3. Médicos e unidade emissora"):
    medico_1 = st.text_input("Nome do Médico 1")
    especialidade_1 = st.text_input("Especialidade 1")
    medico_2 = st.text_input("Nome do Médico 2")
    especialidade_2 = st.text_input("Especialidade 2")
    unidade_emissora = st.text_input("Unidade Emissora do Laudo")
    cnpj_unidade = st.text_input("CNPJ da Unidade")
    responsavel_unidade = st.text_input("Responsável da Unidade")
    cpf_responsavel = st.text_input("CPF do Responsável")

with st.expander("4. Deficiência física"):
    outra_especificacao = st.text_input("Outra especificação")

    st.subheader("Segmentos acometidos")
    segmento_cabeca = st.checkbox("Cabeça")
    segmento_pescoco = st.checkbox("Pescoço")
    segmento_tronco = st.checkbox("Tronco")
    segmento_membros_inferiores = st.checkbox("Membros Inferiores")
    segmento_membros_superiores = st.checkbox("Membros Superiores")

    st.subheader("Letras do enquadramento")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        chk_c = st.checkbox("C")
        chk_d = st.checkbox("D")
        chk_e = st.checkbox("E")
        chk_f = st.checkbox("F")

    with col2:
        chk_g = st.checkbox("G")
        chk_h = st.checkbox("H")
        chk_i = st.checkbox("I")
        chk_j = st.checkbox("J")

    with col3:
        chk_k = st.checkbox("K")
        chk_l = st.checkbox("L")
        chk_m = st.checkbox("M")
        chk_n = st.checkbox("N")

    with col4:
        chk_o = st.checkbox("O")
        chk_p = st.checkbox("P")
        chk_q = st.checkbox("Q")
        chk_r = st.checkbox("R")
        chk_s = st.checkbox("S")

    st.subheader("Formas apresentadas")
    paraplegia = st.checkbox("Paraplegia")
    monoparesia = st.checkbox("Monoparesia")
    triplegia = st.checkbox("Triplegia")
    hemiparesia = st.checkbox("Hemiparesia")
    paralisia_cerebral = st.checkbox("Paralisia Cerebral")
    paraparesia = st.checkbox("Paraparesia")
    tetraplegia = st.checkbox("Tetraplegia")
    triparesia = st.checkbox("Triparesia")
    hemiplegia = st.checkbox("Hemiplegia")
    nanismo = st.checkbox("Nanismo")
    monoplegia = st.checkbox("Monoplegia")
    tetraparesia = st.checkbox("Tetraparesia")
    amputacao = st.checkbox("Amputação ou Ausência de Membro")

with st.expander("5. Exames"):
    exame_ressonancia = st.checkbox("Ressonância nuclear magnética")
    crm_ressonancia = st.text_input("CRM - Ressonância")
    data_ressonancia = st.text_input("Data - Ressonância")

    exame_eletroneuromiografia = st.checkbox("Eletroneuromiografia")
    crm_eletroneuromiografia = st.text_input("CRM - Eletroneuromiografia")
    data_eletroneuromiografia = st.text_input("Data - Eletroneuromiografia")

    exame_cinefuncional = st.checkbox("Cinefuncional")
    crm_cinefuncional = st.text_input("CRM - Cinefuncional")
    data_cinefuncional = st.text_input("Data - Cinefuncional")

    exame_radiografia = st.checkbox("Radiografia digital escanometria")
    crm_radiografia = st.text_input("CRM - Radiografia digital escanometria")
    data_radiografia = st.text_input("Data - Radiografia digital escanometria")

    exame_cobb = st.checkbox("Radiografia ângulo de Cobb")
    crm_cobb = st.text_input("CRM - Radiografia ângulo de Cobb")
    data_cobb = st.text_input("Data - Radiografia ângulo de Cobb")

    exame_tomografia = st.checkbox("Tomografia")
    crm_tomografia = st.text_input("CRM - Tomografia")
    data_tomografia = st.text_input("Data - Tomografia")

    exame_anatomopatologico = st.checkbox("Anatomopatológico")
    crm_anatomopatologico = st.text_input("CRM - Anatomopatológico")
    data_anatomopatologico = st.text_input("Data - Anatomopatológico")

    exame_medico_assistente = st.checkbox("Laudo do médico assistente")
    crm_medico_assistente = st.text_input("CRM - Laudo médico assistente")
    data_medico_assistente = st.text_input("Data - Laudo médico assistente")

    exame_extra_1_check = st.checkbox("Exame extra 1")
    exame_extra_1 = st.text_input("Nome do exame extra 1")
    crm_extra_1 = st.text_input("CRM - Exame extra 1")
    data_extra_1 = st.text_input("Data - Exame extra 1")

    exame_extra_2_check = st.checkbox("Exame extra 2")
    exame_extra_2 = st.text_input("Nome do exame extra 2")
    crm_extra_2 = st.text_input("CRM - Exame extra 2")
    data_extra_2 = st.text_input("Data - Exame extra 2")

with st.expander("6. Assinatura"):
    medico_assinatura_1 = st.text_input("Médico assinatura 1")
    especialidade_assinatura_1 = st.text_input("Especialidade assinatura 1")
    medico_assinatura_2 = st.text_input("Médico assinatura 2")
    especialidade_assinatura_2 = st.text_input("Especialidade assinatura 2")
    unidade_credenciada = st.text_input("Unidade Credenciada Emissora")
    cnpj_credenciada = st.text_input("CNPJ Credenciada")
    responsavel_credenciada = st.text_input("Responsável Credenciada")
    cpf_credenciada = st.text_input("CPF Credenciada")


def marcar(c, condicao, x, y):
    if condicao:
        c.setFont("Helvetica-Bold", 8)
        c.drawString(x, y, "X")


def texto(c, valor, x, y, tamanho=8):
    if valor:
        c.setFont("Helvetica", tamanho)
        c.drawString(x, y, str(valor))


if st.button("Gerar PDF fixo"):

    modelo_pdf = "Anexo III - PCAT 18-2013 (1).pdf"  # coloque aqui o nome do PDF NÃO editável

    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)

    # =========================
    # PÁGINA 1
    # =========================

    texto(c, data_emissao, 476, 715,16)
    texto(c, nome, 90, 682,14)
    texto(c, data_nascimento, 60, 646,14)
    texto(c, identidade, 120, 626,14)
    texto(c, orgao_emissor, 275, 627,14)
    texto(c, uf, 405, 627,14)
    texto(c, mae, 86, 603,14)
    texto(c, pai, 78, 578,14)
    texto(c, responsavel_legal, 212, 555,14)

    marcar(c, sexo == "Masculino", 260, 659)
    marcar(c, sexo == "Feminino", 377, 659)

    texto(c, cid_fisica, 199, 457)
    texto(c, sequelas_fisica, 372, 457)
    texto(c, cid_visual, 201, 432)
    texto(c, sequelas_visual, 372, 432)

    marcar(c, segmento_cabeca, 183, 376)
    marcar(c, segmento_pescoco, 265, 376)
    marcar(c, segmento_tronco, 335, 376)
    marcar(c, segmento_membros_inferiores, 415, 376)

    marcar(c, lado_superior_esquerdo, 182, 373)
    marcar(c, lado_superior_direito, 265, 373)
    marcar(c, lado_inferior_esquerdo, 335, 373)
    marcar(c, lado_inferior_direito, 413, 373)
    texto(c, limitacao_movimentos, 140, 363)
    texto(c, decorrente_de, 60, 325)
    texto(c, medico_1, 60, 277)
    texto(c, medico_2, 60, 236)
    texto(c, unidade_emissora, 58, 196)
    texto(c, responsavel_unidade, 58, 156)
    texto(c, especialidade_1, 329, 117)
    texto(c, especialidade_2, 331, 79)

    c.showPage()

    # =========================
    # PÁGINA 2
    # =========================

    texto(c, nome, 55, 742)
    texto(c, cpf, 384, 742)

    marcar(c, segmento_cabeca, 55, 635)
    marcar(c, segmento_pescoco, 154, 635)
    marcar(c, segmento_tronco, 235, 635)
    marcar(c, segmento_membros_inferiores, 307, 635)
    marcar(c, segmento_membros_superiores, 430, 635)

    marcar(c, chk_c, 54, 530)
    marcar(c, chk_d, 76, 530)
    marcar(c, chk_e, 92, 530)
    marcar(c, chk_f, 108, 530)
    marcar(c, chk_g, 127, 530)
    marcar(c, chk_h, 143, 530)
    marcar(c, chk_i, 160, 530)
    marcar(c, chk_j, 175, 530)
    marcar(c, chk_k, 189, 530)
    marcar(c, chk_l, 210, 530)
    marcar(c, chk_m, 223, 530)
    marcar(c, chk_n, 241, 530)
    marcar(c, chk_o, 259, 530)
    marcar(c, chk_p, 280, 530)
    marcar(c, chk_q, 295, 530)
    marcar(c, chk_r, 313, 530)
    marcar(c, chk_s, 332, 530)

    marcar(c, bool(outra_especificacao.strip()), 57, 517)
    texto(c, outra_especificacao, 210, 515)

    marcar(c, paraplegia, 53, 448)
    marcar(c, monoparesia, 150, 448)
    marcar(c, triplegia, 238, 449)
    marcar(c, hemiparesia, 314, 448)
    marcar(c, paralisia_cerebral, 423, 447)

    marcar(c, paraparesia, 51, 421)
    marcar(c, tetraplegia, 148, 420)
    marcar(c, triparesia, 239, 420)
    marcar(c, hemiplegia, 315, 421)
    marcar(c, nanismo, 423, 420)

    marcar(c, monoplegia, 51, 393)
    marcar(c, tetraparesia, 149, 392)
    marcar(c, amputacao, 240, 393)

    marcar(c, exame_ressonancia, 54, 181)
    texto(c, crm_ressonancia, 319, 179)
    texto(c, data_ressonancia, 462, 182)

    marcar(c, exame_eletroneuromiografia, 52, 150)
    texto(c, crm_eletroneuromiografia, 316, 151)
    texto(c, data_eletroneuromiografia, 460, 151)

    marcar(c, exame_cinefuncional, 51, 121)
    texto(c, crm_cinefuncional, 316, 122)
    texto(c, data_cinefuncional, 461, 123)

    marcar(c, exame_radiografia, 53, 94)
    texto(c, crm_radiografia, 315, 94)
    texto(c, data_radiografia, 461, 92)

    marcar(c, exame_cobb, 53, 70)
    texto(c, crm_cobb, 317, 64)
    texto(c, data_cobb, 461, 64)

    c.showPage()

    # =========================
    # PÁGINA 3
    # =========================

    marcar(c, exame_tomografia, 57, 785)
    texto(c, crm_tomografia, 316, 787)
    texto(c, data_tomografia, 461, 787)

    marcar(c, exame_anatomopatologico, 57, 756)
    texto(c, crm_anatomopatologico, 318, 759)
    texto(c, data_anatomopatologico, 461, 758)

    marcar(c, exame_medico_assistente, 58, 727)
    texto(c, crm_medico_assistente, 316, 730)
    texto(c, data_medico_assistente, 462, 726)

    marcar(c, exame_extra_1_check, 58, 703)
    texto(c, exame_extra_1, 65, 700)
    texto(c, crm_extra_1, 312, 700)
    texto(c, data_extra_1, 460, 695)

    texto(c, exame_extra_2, 64, 670)
    texto(c, crm_extra_2, 314, 673)
    texto(c, data_extra_2, 462, 668)

    texto(c, medico_assinatura_1, 62, 517)
    texto(c, medico_assinatura_2, 60, 476)
    texto(c, unidade_credenciada, 57, 432)
    texto(c, responsavel_credenciada, 56, 397)
    texto(c, especialidade_assinatura_1, 116, 347)
    texto(c, especialidade_assinatura_2, 389, 344)

    c.save()
    packet.seek(0)

    overlay = PdfReader(packet)
    original = PdfReader(modelo_pdf)

    writer = PdfWriter()

    for i in range(len(original.pages)):
        page = original.pages[i]

        if i < len(overlay.pages):
            page.merge_page(overlay.pages[i])

        writer.add_page(page)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("PDF fixo gerado com sucesso!")

    st.download_button(
        "📥 Baixar PDF fixo preenchido",
        data=output,
        file_name="anexo3_fixo_preenchido.pdf",
        mime="application/pdf"
    )