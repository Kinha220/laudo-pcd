import streamlit as st
from pypdf import PdfReader, PdfWriter
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

sexo = st.radio("Sexo", ["Masculino", "Feminino"])

if st.button("Gerar PDF"):

    reader = PdfReader("Anexo III - PCAT 18-2013.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # ===== MAPEAMENTO =====
    dados = {
        "text_1aain": nome,
        "text_2vzkg": data_nasc,
        "text_3fmsf": rg,
        "text_4uvdc": orgao,
        "text_5xlcb": uf,
        "text_8ylvx": mae,
        "text_10mrxo": pai,

        # SEXO (checkbox)
        "checkbox_16fqts": "/Sim" if sexo == "Masculino" else "/Off",
        "checkbox_17tlov": "/Sim" if sexo == "Feminino" else "/Off",
    }

    writer.update_page_form_field_values(
        writer.pages[0],
        dados
    )

    # 🔥 IMPORTANTE (faz aparecer no PDF)
    writer._root_object.update({
        "/NeedAppearances": True
    })

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.download_button("📥 Baixar PDF", output, "anexo3.pdf")
