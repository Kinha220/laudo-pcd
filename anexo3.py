import streamlit as st
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
from io import BytesIO

st.title("🧪 Teste visual Anexo III")

if st.button("Gerar teste visual"):

    original = PdfReader("Anexo III - PCAT 18-2013.pdf")
    page = original.pages[0]

    largura = float(page.mediabox.width)
    altura = float(page.mediabox.height)

    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(largura, altura))

    c.setFont("Helvetica-Bold", 30)
    c.drawString(50, altura - 100, "TESTE VISUAL")
    c.drawString(50, altura - 150, "SE APARECER, FUNCIONOU")

    c.save()
    packet.seek(0)

    overlay = PdfReader(packet)
    writer = PdfWriter()

    page.merge_page(overlay.pages[0])
    writer.add_page(page)

    for i in range(1, len(original.pages)):
        writer.add_page(original.pages[i])

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.download_button(
        "📥 Baixar teste",
        output,
        "teste_visual_anexo3.pdf",
        "application/pdf"
    )
