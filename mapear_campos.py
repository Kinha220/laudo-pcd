from pypdf import PdfReader, PdfWriter

entrada = "Anexo III - PCAT 18-2013.pdf"
saida = "MAPA_CAMPOS_ANEXO_III.pdf"

reader = PdfReader(entrada)
writer = PdfWriter()

writer.clone_reader_document_root(reader)

campos = reader.get_fields()
valores = {}

for nome, info in campos.items():
    tipo = info.get("/FT")

    if tipo == "/Tx":
        valores[nome] = nome

    elif tipo == "/Btn":
        valores[nome] = "/Yes"

for page in writer.pages:
    writer.update_page_form_field_values(page, valores)

with open(saida, "wb") as f:
    writer.write(f)

print(f"PDF gerado: {saida}")