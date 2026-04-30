import streamlit as st
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject, BooleanObject
from io import BytesIO

st.title("🧪 Teste forte - Anexo III")

nome = st.text_input("Nome", "TESTE NOME")
cpf = st.text_input("CPF", "123.456.789-00")
data = st.text_input("Data", "29/04/2026")

def preencher_campo_direto(writer, nome_campo, valor):
    for page in writer.pages:
        if "/Annots" not in page:
            continue

        for annot in page["/Annots"]:
            obj = annot.get_object()

            if obj.get("/T") == nome_campo:
                obj.update({
                    NameObject("/V"): TextStringObject(str(valor)),
                    NameObject("/DV"): TextStringObject(str(valor))
                })

def marcar_checkbox_direto(writer, nome_campo, marcado=True):
    valor = NameObject("/Sim") if marcado else NameObject("/Off")

    for page in writer.pages:
        if "/Annots" not in page:
            continue

        for annot in page["/Annots"]:
            obj = annot.get_object()

            if obj.get("/T") == nome_campo:
                obj.update({
                    NameObject("/V"): valor,
                    NameObject("/AS"): valor
                })

if st.button("Gerar teste"):

    reader = PdfReader("Anexo III - PCAT 18-2013.pdf")
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

    preencher_campo_direto(writer, "text_1aain", nome)
    preencher_campo_direto(writer, "text_2vzkg", data)
    preencher_campo_direto(writer, "text_3fmsf", cpf)

    marcar_checkbox_direto(writer, "checkbox_16fqts", True)
    marcar_checkbox_direto(writer, "checkbox_17tlov", False)

    output = BytesIO()
    writer.write(output)
    output.seek(0)

    st.download_button(
        "📥 Baixar PDF teste",
        output,
        "anexo3_teste.pdf",
        "application/pdf"
    )
