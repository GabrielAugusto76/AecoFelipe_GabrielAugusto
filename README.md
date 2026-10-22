# 🧭 Consultor Inteligente de Carreiras em TI

Sistema Especialista baseado em regras que entrevista o usuário e recomenda **uma entre 10 trilhas de carreira em TI**, justificando a decisão com as regras disparadas.

> Trabalho da disciplina de **Inteligência Artificial** — Ciência da Computação, UNIPAC Barbacena.

## Trilhas
Back-end · Front-end & UI/UX · Ciência de Dados e ML · Engenharia de Dados · Cibersegurança · DevOps & SRE · Computação em Nuvem · Mobile · QA · Gestão de Produtos

## Tecnologias
Python 3.10+ · [Experta](https://github.com/nilp0inter/experta) (motor de regras, encadeamento para frente) · [Streamlit](https://streamlit.io) (interface web)

## Instalação e execução

```bash
# 1. clonar
git clone <URL-DO-SEU-REPOSITORIO>
cd consultor-carreiras-ti

# 2. (opcional) ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. instalar dependências
pip install -r requirements.txt

# 4. rodar a aplicação
streamlit run app.py
```

A aplicação abre em `http://localhost:8501`.

## Testes (validação com personas)

```bash
pytest -v
```

Os testes executam **10 personas** (as 4 exigidas — analítico, infra/segurança, visual/front-end, negócios/produto — mais 6 cobrindo as demais trilhas) e verificam casos de desambiguação (Ciência × Engenharia de Dados, DevOps × Cloud, Front-end × Mobile).

## Estrutura

```
├── app.py                    # Interface Streamlit
├── career_expert/
│   ├── compat.py             # Correção Experta x Python 3.10+
│   ├── questions.py          # Perguntas, opções e catálogo das trilhas
│   ├── engine.py             # Fatos + 25 regras @Rule + regra de decisão
│   └── personas.py           # Personas de teste
├── tests/test_personas.py    # Testes automatizados
├── docs/matriz_decisao.md    # Matriz de decisão (Fase 1)
└── requirements.txt
```

## Como funciona

1. **Entrevista dinâmica:** perguntas extras aparecem conforme as respostas (ex.: se você escolhe "analisar dados brutos", o sistema pergunta se prefere *modelagem* ou *pipelines*).
2. **Fatos:** as respostas viram um fato `Perfil` na memória de trabalho do Experta.
3. **Inferência:** cada regra `@Rule` que casa com o perfil dispara, soma/subtrai pontos de trilhas e registra o motivo.
4. **Decisão:** uma regra de menor prioridade (`salience=-100`) roda por último e escolhe a trilha vencedora.
5. **Justificativa:** a interface exibe a trilha, os motivos (regras disparadas e pontos), o ranking das 10 trilhas e a segunda opção.

Detalhes das regras em [`docs/matriz_decisao.md`](docs/matriz_decisao.md).

## Observação técnica
O Experta usa `collections.Mapping`, removido no Python 3.10. O módulo `career_expert/compat.py` recria o alias antes da importação, então o projeto funciona em Python 3.10, 3.11, 3.12 etc.

## Autor
**Nome:** _Gabriel Augusto Bedeschi DOmingos_ · **Professor:** Felipe Roncalli de Paula Carneiro

## Prints 

<img width="1363" height="669" alt="image" src="https://github.com/user-attachments/assets/5c091e44-d575-4254-85a1-b8b88a134b46" />
<img width="1364" height="624" alt="image" src="https://github.com/user-attachments/assets/5f4cd83a-de7d-4018-8866-9e5b9231f99e" />
<img width="1363" height="681" alt="image" src="https://github.com/user-attachments/assets/69965a05-ee63-4d38-888e-16faa6a8bce4" />
<img width="1366" height="641" alt="image" src="https://github.com/user-attachments/assets/77ab0c22-3800-4608-b478-2fe4bddd85cb" />
<img width="1366" height="644" alt="image" src="https://github.com/user-attachments/assets/8081aab9-0eb8-4e3c-b653-a6c48380111c" />
<img width="1366" height="636" alt="image" src="https://github.com/user-attachments/assets/0a42766f-e5f1-4459-9275-31750b686df7" />
<img width="1363" height="632" alt="image" src="https://github.com/user-attachments/assets/541eae32-c7bf-428f-8004-67ed081c5e9c" />
<img width="1366" height="633" alt="image" src="https://github.com/user-attachments/assets/be4c9f0a-8e22-49f8-9563-52fec33ca4ed" />







