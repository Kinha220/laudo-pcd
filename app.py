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
    c.drawString(100, 700, f"Nome: {nome}")
    c.drawString(100, 680, f"CPF: {cpf}")
    c.drawString(100, 660, f"Data: {data}")
    c.drawString(100, 640, f"CID: {cid}")
    c.drawString(100, 620, f"Descrição: {descricao}")

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
