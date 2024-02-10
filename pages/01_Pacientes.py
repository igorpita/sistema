import streamlit as st

# Definir os campos do cadastro
campos = {
    "Nome completo": "",
    "Data de nascimento": "",
    "Endereço": "",
    "Telefone": "",
    "Email": "",
    "Plano de saúde": "",
    "Observações": "",
}

# Formulário de Cadastro de Pacientes
with st.form(key="cadastro_paciente"):
    for campo in campos:
        campos[campo] = st.text_input(campo)

    submitted = st.form_submit_button("Salvar")

# Salvar os dados no banco de dados
if submitted:
    # Conectar ao banco de dados
    # ...

    # Inserir os dados do paciente
    # ...

    # Exibir mensagem de sucesso
    st.success("Paciente cadastrado com sucesso!")

