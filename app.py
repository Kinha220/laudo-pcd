import streamlit as st
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
from io import BytesIO

st.title("📄 Gerador de Laudo PCD")

# FORMULÁRIO
nome = st.text_input("Nome")
cpf = st.text_input("CPF")
data = st.text_input("Data de nascimento")
cid = st.text_input("CID")
descricao = st.text_area("Descrição da deficiência")

if st.button("Gerar PDF"):

    packet = BytesIO()
    c = canvas.Canvas(packet)

    # POSIÇÕES (vamos ajustar depois certinho)
c.setFont("Helvetica", 9)

# Serviço Médico / Unidade de Saúde
c.drawString(35, 580, servico_medico)

# CNPJ
c.drawString(400, 580, cnpj)

# Data
c.drawString(35, 538, data)

# Nome do requerente
c.drawString(35, 392, nome)

# CPF
c.drawString(400, 392, cpf)

# CID Deficiência Física
c.drawString(300, 300, cid)

# Descrição detalhada
text = c.beginText(35, 205)
text.setFont("Helvetica", 9)

for linha in descricao.split("\n"):
    text.textLine(linha)

c.drawText(text)

    c.save()
    packet.seek(0)

    # PDF base (vamos colocar depois)
    reader = PdfReader("Anexo Unico.pdf")
    writer = PdfWriter()

    page = reader.pages[0]
    overlay = PdfReader(packet).pages[0]

    page.merge_page(overlay)
    writer.add_page(page)

    with open("laudo_preenchido.pdf", "wb") as f:
        writer.write(f)

    st.success("PDF gerado com sucesso!")
    st.download_button("Baixar PDF", open("laudo_preenchido.pdf", "rb"), "laudo.pdf")
