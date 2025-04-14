import streamlit as st
from main import run_compliance_assistant

st.title("🛡️ Assistente IA de Compliance da Segurança da Informação")
st.write("Traduza normas complexas como **ISO 27001**, **LGPD**, **GDPR** e outras em explicações claras e práticas, adaptadas ao seu contexto técnico.")

with st.sidebar:
    st.header("⚙️ Selecione uma tarefa")
    tipo_tarefa = "Responder pergunta sobre conformidade"
    pergunta_usuario = st.text_area("📌 Digite uma pergunta sobre conformidade:")

if st.button("🚀 Executar verificação de conformidade"):
    if not pergunta_usuario.strip():
        st.warning("⚠️ Por favor, digite sua pergunta antes de executar.")
    else:
        with st.spinner("Processando sua solicitação... Aguarde, por favor."):
            resultado = run_compliance_assistant(pergunta_usuario)

        st.subheader("✅ Resposta da IA sobre conformidade:")
        st.markdown(resultado)
