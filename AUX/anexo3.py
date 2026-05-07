import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject
from io import BytesIO

st.set_page_config(page_title="Anexo III", layout="centered")
st.title("📄 Gerador Anexo III")


def marcar_checkbox_por_opcao(writer, opcao_yes, marcado):
    for page in writer.pages:
        if "/Annots" in page:
            for annot in page["/Annots"]:
                obj = annot.get_object()
                if "/AP" in obj and "/N" in obj["/AP"]:
                    opcoes = list(obj["/AP"]["/N"].keys())
                    if opcao_yes in opcoes:
                        obj.update({
                            NameObject("/AS"): NameObject(opcao_yes if marcado else "/Off")
                        })


with st.expander("1. Identificação", expanded=True):
    data_emissao = st.text_input("Data de emissão")
    nome = st.text_input("Nome")
    cpf = st.text_input("CPF")
    data_nascimento = st.text_input("Data de nascimento")
    identidade = st.text_input("Identidade nº")
    orgao_emissor = st.text_input("Órgão emissor")
    uf = st.text_input("UF")
    mae = st.text_input("Mãe")
    pai = st.text_input("Pai")
    responsavel_legal = st.text_input("Responsável legal")
    sexo = st.radio("Sexo", ["Não marcar", "Masculino", "Feminino"], horizontal=True)

with st.expander("2. Laudo pericial", expanded=True):
    cid_fisica = st.text_input("CID - Deficiência Física")
    sequelas_fisica = st.text_input("Sequelas - Deficiência Física")
    cid_visual = st.text_input("CID - Deficiência Visual")
    sequelas_visual = st.text_input("Sequelas - Deficiência Visual")
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


if st.button("Gerar PDF"):
    reader = PdfReader("Anexo III - PCAT 18-2013.pdf")
    writer = PdfWriter()
    writer.clone_reader_document_root(reader)
    writer.set_need_appearances_writer(True)

    campos = {
        "text_113jmbp": data_emissao,
        "text_1aain": nome,
        "text_2vzkg": data_nascimento,
        "text_3fmsf": identidade,
        "text_4uvdc": orgao_emissor,
        "text_5xlcb": uf,
        "text_8ylvx": mae,
        "text_10mrxo": pai,
        "text_11yhb": responsavel_legal,

        "text_12xfw": cid_fisica,
        "text_14amyd": sequelas_fisica,
        "text_13wate": cid_visual,
        "text_15vxpx": sequelas_visual,
        "text_21lsif": limitacao_movimentos,
        "text_23zdpk": decorrente_de,

        "text_24ezmf": medico_1,
        "text_25lnty": especialidade_1,
        "text_26fdqd": medico_2,
        "text_27ey": especialidade_2,
        "text_28bslb": unidade_emissora,
        "text_30jooj": cnpj_unidade,
        "text_29lviz": responsavel_unidade,
        "text_31tqp": cpf_responsavel,

        "text_32ktxf": nome,
        "text_33ybmg": cpf,
        "text_39llvk": outra_especificacao,

        "text_70srgd": crm_ressonancia,
        "text_75mane": data_ressonancia,
        "text_71wkor": crm_eletroneuromiografia,
        "text_76pbiu": data_eletroneuromiografia,
        "text_72vzps": crm_cinefuncional,
        "text_77nzod": data_cinefuncional,
        "text_73qovk": crm_radiografia,
        "text_78jitp": data_radiografia,
        "text_74gssz": crm_cobb,
        "text_79tyhz": data_cobb,

        "text_50zfqc": crm_tomografia,
        "text_55oexl": data_tomografia,
        "text_51rdnw": crm_anatomopatologico,
        "text_56ndnw": data_anatomopatologico,
        "text_52gwsg": crm_medico_assistente,
        "text_57wmet": data_medico_assistente,
        "text_48xuhq": exame_extra_1,
        "text_53pxvb": crm_extra_1,
        "text_58upow": data_extra_1,
        "text_49onvg": exame_extra_2,
        "text_54oomj": crm_extra_2,
        "text_59syrt": data_extra_2,

        "text_45hgka": medico_assinatura_1,
        "text_44uiwt": especialidade_assinatura_1,
        "text_43sfbc": medico_assinatura_2,
        "text_42uvgx": especialidade_assinatura_2,
        "text_41ztdr": unidade_credenciada,
        "text_46vxkc": cnpj_credenciada,
        "text_40gqli": responsavel_credenciada,
        "text_47swsv": cpf_credenciada,
    }

    for page in writer.pages:
        writer.update_page_form_field_values(page, campos)

    marcar_checkbox_por_opcao(writer, "/Yes_yzh", sexo == "Masculino")
    marcar_checkbox_por_opcao(writer, "/Yes_kcbz", sexo == "Feminino")

    marcar_checkbox_por_opcao(writer, "/Yes_hxqo", segmento_cabeca)
    marcar_checkbox_por_opcao(writer, "/Yes_pnwq", segmento_pescoco)
    marcar_checkbox_por_opcao(writer, "/Yes_xfmy", segmento_tronco)
    marcar_checkbox_por_opcao(writer, "/Yes_orru", segmento_membros_inferiores)
    marcar_checkbox_por_opcao(writer, "/Yes_oyxh", segmento_membros_superiores)

    marcar_checkbox_por_opcao(writer, "/Yes_ygdz", chk_c)
    marcar_checkbox_por_opcao(writer, "/Yes_nntj", chk_d)
    marcar_checkbox_por_opcao(writer, "/Yes_rlty", chk_e)
    marcar_checkbox_por_opcao(writer, "/Yes_gfis", chk_f)
    marcar_checkbox_por_opcao(writer, "/Yes_pven", chk_g)
    marcar_checkbox_por_opcao(writer, "/Yes_ttlb", chk_h)
    marcar_checkbox_por_opcao(writer, "/Yes_ynfs", chk_i)
    marcar_checkbox_por_opcao(writer, "/Yes_uoov", chk_j)
    marcar_checkbox_por_opcao(writer, "/Yes_ppwl", chk_k)
    marcar_checkbox_por_opcao(writer, "/Yes_kwxm", chk_l)
    marcar_checkbox_por_opcao(writer, "/Yes_mazr", chk_m)
    marcar_checkbox_por_opcao(writer, "/Yes_rbtz", chk_n)
    marcar_checkbox_por_opcao(writer, "/Yes_tpkq", chk_o)
    marcar_checkbox_por_opcao(writer, "/Yes_hjew", chk_p)
    marcar_checkbox_por_opcao(writer, "/Yes_krok", chk_q)
    marcar_checkbox_por_opcao(writer, "/Yes_unhh", chk_r)
    marcar_checkbox_por_opcao(writer, "/Yes_vblt", chk_s)

    marcar_checkbox_por_opcao(writer, "/Yes_rdo", bool(outra_especificacao.strip()))

    marcar_checkbox_por_opcao(writer, "/Yes_wunf", paraplegia)
    marcar_checkbox_por_opcao(writer, "/Yes_jkck", monoparesia)
    marcar_checkbox_por_opcao(writer, "/Yes_cbkm", triplegia)
    marcar_checkbox_por_opcao(writer, "/Yes_tslm", hemiparesia)
    marcar_checkbox_por_opcao(writer, "/Yes_akg", paralisia_cerebral)

    marcar_checkbox_por_opcao(writer, "/Yes_ivas", paraparesia)
    marcar_checkbox_por_opcao(writer, "/Yes_cmpf", tetraplegia)
    marcar_checkbox_por_opcao(writer, "/Yes_bono", triparesia)
    marcar_checkbox_por_opcao(writer, "/Yes_fgwk", hemiplegia)
    marcar_checkbox_por_opcao(writer, "/Yes_uyk", nanismo)

    marcar_checkbox_por_opcao(writer, "/Yes_lihq", monoplegia)
    marcar_checkbox_por_opcao(writer, "/Yes_nvgd", tetraparesia)
    marcar_checkbox_por_opcao(writer, "/Yes_abuj", amputacao)

    marcar_checkbox_por_opcao(writer, "/Yes_qati", exame_ressonancia)
    marcar_checkbox_por_opcao(writer, "/Yes_gryq", exame_eletroneuromiografia)
    marcar_checkbox_por_opcao(writer, "/Yes_htrw", exame_cinefuncional)
    marcar_checkbox_por_opcao(writer, "/Yes_ouuu", exame_radiografia)
    marcar_checkbox_por_opcao(writer, "/Yes_gkhr", exame_cobb)

    marcar_checkbox_por_opcao(writer, "/Yes_spiz", exame_tomografia)
    marcar_checkbox_por_opcao(writer, "/Yes_qdfh", exame_anatomopatologico)
    marcar_checkbox_por_opcao(writer, "/Yes_cawl", exame_medico_assistente)
    marcar_checkbox_por_opcao(writer, "/Yes_qegw", exame_extra_1_check)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("PDF gerado com sucesso!")

    st.download_button(
        "📥 Baixar PDF preenchido",
        data=output,
        file_name="anexo3_preenchido.pdf",
        mime="application/pdf"
    )