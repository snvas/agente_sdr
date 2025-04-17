import pysqlite3
import sys
sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")



import streamlit as st
from main import run_sales_development

# Configuração da página
st.set_page_config(
    page_title="Agente de SDR",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuração da sidebar
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        min-width: 400px;
        max-width: 600px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título da aplicação
st.title("🤝 Agente de SDR")
st.write("Assistente de Desenvolvimento de Vendas")

# Inicializa o estado da sessão
if 'resultado' not in st.session_state:
    st.session_state.resultado = None

# Sidebar com informações
with st.sidebar:
    st.header("⚙️ Informações da Empresa")
    company_name = st.text_input("Nome da Sua Empresa")
    company_services = st.text_area("Serviços/Produtos da Sua Empresa")
    company_icp = st.text_area(
        "ICP (Ideal Customer Profile)",
        help="Descreva o perfil ideal do seu cliente. Ex: Empresas de tecnologia com faturamento acima de R$ 10M, com mais de 50 funcionários, que buscam soluções de automação."
    )
    
    st.header("⚙️ Informações do Lead")
    lead_name = st.text_input("Nome da Empresa do Lead")
    industry = st.text_input("Setor/Indústria")
    key_decision_maker = st.text_input("Nome do Decisor")
    position = st.text_input("Cargo do Decisor")

    st.header("📌 Contexto da Abordagem")
    message_type = st.radio(
        "Tipo de Mensagem",
        ["E-mail", "LinkedIn"],
        help="Selecione o formato da mensagem que deseja gerar"
    )
    pergunta_usuario = st.text_area("Descreva o contexto ou objetivo da abordagem:")

# Botão de ação principal
if st.button("🚀 Iniciar Análise e Abordagem", key="main_button"):
    if not all([company_name, company_services, lead_name, industry, key_decision_maker, position, pergunta_usuario]):
        st.warning("⚠️ Por favor, preencha todos os campos obrigatórios antes de executar.")
    else:
        inputs = {
            "company_name": company_name,
            "company_services": company_services,
            "company_icp": company_icp,
            "lead_name": lead_name,
            "industry": industry,
            "key_decision_maker": key_decision_maker,
            "position": position,
            "message_type": message_type
        }
        
        with st.spinner("Analisando o lead e preparando a abordagem... Aguarde, por favor."):
            st.session_state.resultado = run_sales_development(pergunta_usuario, inputs=inputs)

# Exibe o resultado se existir
if st.session_state.resultado:
    st.markdown(st.session_state.resultado.tasks_output[0].raw)
    # Formata o resultado em markdown com borda sólida branca
    resultado_formatado = f"""
    <div style="font-family: Roboto, sans-serif; font-size: 16px; line-height: 1.6; color: #fff; border: 2px solid white; padding: 15px; border-radius: 5px;">
    {st.session_state.resultado}
    </div>
    """
    st.markdown(resultado_formatado, unsafe_allow_html=True)
    
    # Exibe o mesmo texto em um bloco de código para fácil cópia
    st.code(st.session_state.resultado, language="text", line_numbers=False)
