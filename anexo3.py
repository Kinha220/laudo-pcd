import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject, BooleanObject
from io import BytesIO

st.title("🧪 Teste forte Anexo III")

nome = st.text_input("Nome", "GESSICA TESTE")
data_nasc = st.text_input("Data nascimento", "29/04/2026")
rg = st.text_input("RG", "123456789")
orgao = st.text_input("Órgão", "SSP")
uf = st.text_input("UF", "SP")

def preencher_texto(writer, campo, valor):
    for page in writer.pages:
        if "/Annots" not in page:
            continue

        for annot in page["/Annots"]:
            obj = annot.get_object()

            if obj.get("/T") == campo:
                obj.update({
                    NameObject("/V"): TextStringObject(str(valor)),
                    NameObject("/DV"): TextStringObject(str(valor)),
                })

            if "/Parent" in obj:
                parent = obj["/Parent"].get_object()
                if parent.get("/T") == campo:
                    parent.update({
                        NameObject("/V"): TextStringObject(str(valor)),
                        NameObject("/DV"): TextStringObject(str(valor)),
                    })

if st.button("Gerar teste"):

    reader = PdfReader("Anexo III - PCAT 18-2013.pdf")
    writer = PdfWriter()
    writer.clone_reader_document_root(reader)

    if "/AcroForm" in writer._root_object:
        writer._root_object["/AcroForm"].update({
            NameObject("/NeedAppearances"): BooleanObject(True)
        })

    preencher_texto(writer, "text_2omgi", nome)
    preencher_texto(writer, "text_3qmhu", data_nasc)
    preencher_texto(writer, "text_4iybw", rg)
    preencher_texto(writer, "text_5ihyi", orgao)
    preencher_texto(writer, "text_6bofk", uf)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.download_button(
        "📥 Baixar teste",
        output,
        "teste_anexo3.pdf",
        "application/pdf"
    )
