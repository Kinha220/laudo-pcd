def quebrar_texto(texto, limite=95):
    linhas = []
    atual = ""

    for palavra in texto.split():
        teste = f"{atual} {palavra}".strip()

        if len(teste) <= limite:
            atual = teste
        else:
            linhas.append(atual)
            atual = palavra

    if atual:
        linhas.append(atual)

    return "\n".join(linhas)


campos = {

    # Página 1
    "Text7": servico_medico,
    "Text8": cnpj,
    "Text9": data,

    "Text10": nome_requerente,
    "Text11": cpf_requerente,

    "Text12": cid_fisica,
    "Text13": cid_visual,

    # 🔥 AJUSTADO
    "Text14": quebrar_texto(
        descricao.upper(),
        95
    )[:1200],

    # Página 2 - 3. Assinaturas
    "Text15": nome_medico,
    "Text16": assinatura_medico,

    "Text17": responsavel_servico,
    "Text18": assinatura_responsavel_servico,

    # Página 2 - 4.1 Identificação do requerente
    "Text19": nome_requerente,
    "Text20": cpf_requerente,

    # Página 3 - 4.4 Assinaturas
    "Text21": nome_medico,
    "Text22": assinatura_medico,

    "Text23": responsavel_servico,
    "Text24": assinatura_responsavel_servico,

    # Página 3 - 4.5 Declaração
    "Text64": nome_requerente,
    "Text65": cpf_requerente,

    # 🔥 AJUSTADO
    "Text66": "expressões da verdade.",

    # Página 3 - 4.6 Assinatura final
    "Text25": nome_medico,
    "Text26": cpf_medico,

    "Text27": especialidade,
    "Text28": assinatura_medico,

    "Text29": unidade,
    "Text30": cnpj_unidade,

    "Text31": responsavel_unidade,
    "Text32": cpf_responsavel_unidade,

    # Checkboxes página 1
    "Check Box34": check(
        tipo_servico == "pelo Departamento de Trânsito (Detran)"
    ),

    "Check Box35": check(
        tipo_servico == "por setor privado credenciado pelo Detran"
    ),

    "Check Box36": check(
        tipo_servico == "pelo serviço público de saúde"
    ),

    "Check Box37": check(
        tipo_servico == "por setor privado que integra o Sistema Único de Saúde (SUS)"
    ),

    "Check Box38": check(
        tipo_servico == "pelo serviço social autônomo"
    ),

    # Checkboxes página 2
    "Check Box42": check(tem_def_fisica),

    "Check Box43": check("Cabeça" in segmentos),
    "Check Box44": check("Pescoço" in segmentos),
    "Check Box45": check("Tronco" in segmentos),
    "Check Box46": check("Membros Inferiores" in segmentos),
    "Check Box47": check("Membros Superiores" in segmentos),

    "Check Box48": check("Paraplegia" in formas),
    "Check Box49": check("Monoparesia" in formas),
    "Check Box50": check("Triplegia" in formas),
    "Check Box51": check("Hemiparesia" in formas),
    "Check Box52": check("Paralisia Cerebral" in formas),
    "Check Box53": check("Paraparesia" in formas),
    "Check Box54": check("Tetraplegia" in formas),
    "Check Box55": check("Triparesia" in formas),
    "Check Box56": check("Ostomia" in formas),
    "Check Box57": check("Nanismo" in formas),
    "Check Box58": check("Monoplegia" in formas),
    "Check Box59": check("Tetraparesia" in formas),
    "Check Box60": check("Hemiplegia" in formas),

    "Check Box61": check(
        "Amputação ou Ausência de Membro" in formas
    ),

    "Check Box67": check(
        "Deformidade congênita/adquirida" in formas
    ),

    "Check Box62": check(
        "Acuidade visual / campo visual" in condicoes
    ),

    "Check Box63": check(
        "Perda auditiva bilateral" in condicoes
    ),
}
