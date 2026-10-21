import streamlit as st

from career_expert.engine import diagnosticar
from career_expert.questions import (
    ATUACAO, DESCRICOES, ENTREGA, FERRAMENTA, FOCO_DADOS, MATEMATICA,
    PLATAFORMA, SIM_NAO, TRILHAS,
)

st.set_page_config(page_title="Consultor de Carreiras em TI", page_icon="🧭")

st.title("🧭 Consultor Inteligente de Carreiras em TI")
st.caption("Sistema especialista baseado em regras (Experta) - UNIPAC Barbacena")
st.write("Responda às perguntas e descubra a trilha de carreira mais adequada para você.")


def perguntar(texto, opcoes, chave):
    return st.radio(texto, list(opcoes), format_func=opcoes.get, key=chave)


st.subheader("1. Seu perfil")
matematica = perguntar("Qual sua afinidade com matemática e estatística?", MATEMATICA, "matematica")
atuacao = perguntar("O que você prefere fazer no dia a dia?", ATUACAO, "atuacao")
ferramenta = perguntar("Qual linguagem ou ferramenta você mais domina hoje?", FERRAMENTA, "ferramenta")
entrega = perguntar("Que tipo de entrega de valor você prefere?", ENTREGA, "entrega")

respostas = {
    "matematica": matematica,
    "atuacao": atuacao,
    "ferramenta": ferramenta,
    "entrega": entrega,
}

st.subheader("2. Aprofundando")

if atuacao == "dados_brutos":
    respostas["foco_dados"] = perguntar("Com dados, o que mais te atrai?", FOCO_DADOS, "foco_dados")

if atuacao == "servidores" or entrega == "infra":
    respostas["escala"] = perguntar(
        "Você gosta de planejar arquiteturas escaláveis, migrações e custos de nuvem?",
        SIM_NAO, "escala")

if atuacao in ["layouts", "algoritmos", "apps"] or ferramenta in ["javascript", "mobile"]:
    respostas["plataforma"] = perguntar("Em qual plataforma prefere atuar?", PLATAFORMA, "plataforma")

respostas["pessoas"] = perguntar(
    "Você gosta de conversar com clientes e entender necessidades?", SIM_NAO, "pessoas")

st.divider()

if st.button("🔎 Diagnosticar minha trilha", type="primary"):
    resultado, regras = diagnosticar(respostas)

    if resultado["inconclusivo"]:
        st.warning("Suas respostas não ativaram regras suficientes. Tente revisar as respostas.")
    else:
        st.success("Trilha recomendada: " + resultado["nome"])
        st.write(DESCRICOES[resultado["trilha"]])

        st.subheader("📋 Por que essa recomendação?")
        for regra, motivo, pontos in resultado["motivos"]:
            st.write("- " + regra + ": " + motivo + " (" + str(pontos) + " pontos)")
        st.write("Pontuação total: " + str(resultado["pontos"]))

        st.subheader("📊 Ranking das trilhas")
        nomes = []
        valores = []
        for trilha, pontos in resultado["ranking"]:
            nomes.append(TRILHAS[trilha])
            valores.append(pontos)
        st.bar_chart(dict(zip(nomes, valores)))

    with st.expander("🔧 Regras disparadas (" + str(len(regras)) + ")"):
        for regra in regras:
            st.write(regra)
