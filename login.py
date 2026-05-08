import streamlit as st
from app import main as anexo_unico
from anexo3Nedit import main as anexo_iii

st.set_page_config(
    page_title="Sistema Laudos PCD",
    layout="centered"
)

# =========================
# LOGIN
# =========================

SENHA_APP = "laudo2026"

if "logado" not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:

    st.markdown("""
    <div class="app-header">
        <div class="app-title">🔐 Sistema Laudos PCD</div>
        <div class="app-subtitle">
            Faça login para acessar os formulários.
        </div>
    </div>
    """, unsafe_allow_html=True)

    senha = st.text_input(
        "Digite a senha",
        type="password"
    )

    if st.button("Entrar"):

        if senha == SENHA_APP:
            st.session_state.logado = True
            st.rerun()

        else:
            st.error("Senha incorreta")

    st.stop()
    
    # check_login()
# =========================
# HOME
# =========================

st.markdown("""
<div class="app-header">
    <div class="app-title">📄 Sistema de Laudos PCD</div>
    <div class="app-subtitle">
        Escolha abaixo qual formulário deseja preencher.
    </div>
</div>
""", unsafe_allow_html=True)

opcao = st.selectbox(
    "Selecione o formulário",
    [
        "Selecione...",
        "📘 Anexo Único",
        "📗 Anexo III"
    ]
)

# =========================
# FORMULÁRIOS
# =========================

if opcao == "📘 Anexo Único":
    anexo_unico()

elif opcao == "📗 Anexo III":
    anexo_iii()