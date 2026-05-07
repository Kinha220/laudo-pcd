from pypdf import PdfReader

reader = PdfReader("Anexo III - PCAT 18-2013.pdf")

for numero_pagina, page in enumerate(reader.pages, start=1):

    print(f"\n========== PÁGINA {numero_pagina} ==========")

    if "/Annots" in page:

        for annot in page["/Annots"]:

            obj = annot.get_object()

            nome = obj.get("/T")
            rect = obj.get("/Rect")
            tipo = obj.get("/FT")

            print(f"""
CAMPO: {nome}
TIPO: {tipo}
RECT: {rect}
""")