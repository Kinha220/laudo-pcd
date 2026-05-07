from pypdf import PdfReader

reader = PdfReader("Anexo III - PCAT 18-2013.pdf")
fields = reader.get_fields()

for nome, info in fields.items():
    tipo = info.get("/FT")
    print(f"{nome} | {tipo}")