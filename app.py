import streamlit as st
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
from io import BytesIO
import textwrap

st.set_page_config(page_title="Gerador de Laudo PCD", layout="centered")

st.title("📄 Gerador de Laudo PCD")
st.write("Preencha os dados abaixo para gerar o PDF preenchido.")

# CAMPOS DO FORMULÁRIO
servico_medico = st.text_input("Serviço Médico / Unidade de Saúde")
cnpj = st.text_input("CNPJ")
data_emissao = st.text_input("Data de emissão")

nome = st.text_input("Nome do requerente")
cpf = st.text_input("CPF")
cid = st.text_input("CID")
descricao = st.text_area("Descrição detalhada da deficiência")

if st.button("Gerar PDF"):

    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(595, 842))  # tamanho A4

    c.setFont("Helvetica", 9)

    # ===== PREENCHIMENTO PAGE 1 - ANEXO ÚNICO =====

    # Serviço Médico / Unidade de Saúde
    c.drawString(35, 582, servico_medico)

    # CNPJ
    c.drawString(405, 582, cnpj)

    # Data
    c.drawString(35, 538, data_emissao)

    # Nome do requerente
    c.drawString(35, 393, nome)

    # CPF
    c.drawString(405, 393, cpf)

    # CID - Deficiência Física
    c.drawString(300, 300, cid)

    # Descrição detalhada da deficiência
    text = c.beginText(35, 205)
    text.setFont("Helvetica", 9)

    linhas = textwrap.wrap(descricao, width=90)

    for linha in linhas:
        text.textLine(linha)

    c.drawText(text)

    c.save()
    packet.seek(0)

    # PDF MODELO
    modelo_pdf = "Anexo Unico.pdf"

    reader = PdfReader(modelo_pdf)
    overlay_reader = PdfReader(packet)
    writer = PdfWriter()

    # aplica preenchimento apenas na primeira página
    page = reader.pages[0]
    page.merge_page(overlay_reader.pages[0])
    writer.add_page(page)

    # mantém as demais páginas do PDF original
    for i in range(1, len(reader.pages)):
        writer.add_page(reader.pages[i])

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("PDF gerado com sucesso!")

    st.download_button(
        label="📥 Baixar PDF preenchido",
        data=output,
        file_name=f"Laudo_PCD_{nome}.pdf",
        mime="application/pdf"
    )
