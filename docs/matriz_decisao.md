# Matriz de Decisão (Fase 1 — Engenharia de Conhecimento)

## Variáveis de entrada (fatos do `Perfil`)

| Variável | Valores | Pergunta |
|---|---|---|
| `matematica` | baixa, media, alta | Afinidade com matemática e estatística |
| `atuacao` | algoritmos, layouts, servidores, dados_brutos, seguranca, automatizar, testar, priorizar, apps | Preferência de atuação diária |
| `ferramenta` | python, javascript, sql, linux_redes, mobile, nenhuma | Linguagem/ferramenta de maior afinidade |
| `entrega` | produto, infra, seguranca, insights, dados_confiaveis, qualidade, estrategia | Tipo de entrega de valor preferida |
| `foco_dados` | modelagem, pipelines | *Condicional:* só se `atuacao = dados_brutos` |
| `escala` | sim, nao | *Condicional:* só se `atuacao = servidores` ou `entrega = infra` |
| `plataforma` | web, mobile, indiferente | *Condicional:* só se atuação visual/lógica/apps ou ferramenta JS/mobile |
| `pessoas` | sim, nao | Gosta de lidar com clientes/stakeholders? |

## Mecanismo de pontuação

Cada regra que dispara soma (ou subtrai) pontos das trilhas. Regras de **sinal forte** (combinação de 2–3 variáveis) valem 5–7 pts; regras de **sinal de apoio** valem 2–4 pts; regras de **desambiguação** também **subtraem** pontos da trilha concorrente. A regra de decisão (salience −100) dispara por último e escolhe a trilha de maior pontuação (empate: mais regras favoráveis).

## Tabela de regras

| ID | Condição (SE) | Efeito (ENTÃO) |
|---|---|---|
| R01 | atuacao=algoritmos E ferramenta ∈ {python, sql, javascript} | Back-end +4 |
| R02 | atuacao=algoritmos E entrega ∈ {produto, infra} | Back-end +3 |
| R03 | atuacao=servidores E ferramenta ∈ {python, sql} E matematica ∈ {baixa, media} | Back-end +4 |
| R04 | atuacao=layouts E ferramenta=javascript | Front-end +6 |
| R05 | atuacao=layouts E entrega=produto | Front-end +4 |
| R06 | matematica=alta E atuacao=dados_brutos E foco_dados=modelagem | Ciência de Dados +7 |
| R07 | ferramenta=python E entrega=insights | Ciência de Dados +4 |
| R08 | foco_dados=modelagem E matematica ∈ {baixa, media} | Ciência de Dados −3, Eng. Dados +1 |
| R09 | atuacao=dados_brutos E foco_dados=pipelines | Eng. Dados +7 |
| R10 | entrega=dados_confiaveis E ferramenta ∈ {python, sql} | Eng. Dados +5 |
| R11 | atuacao=dados_brutos E foco_dados=pipelines E matematica ∈ {baixa, media} | Eng. Dados +2, Ciência de Dados −2 |
| R12 | atuacao=seguranca E ferramenta=linux_redes | Cibersegurança +6 |
| R13 | entrega=seguranca | Cibersegurança +5 |
| R14 | atuacao=automatizar E ferramenta=linux_redes | DevOps +6 |
| R15 | atuacao=automatizar E entrega=infra | DevOps +4 |
| R16 | atuacao=servidores E entrega=infra E escala=nao | DevOps +3, Cloud −1 |
| R17 | atuacao=servidores E entrega=infra E escala=sim | Cloud +6 |
| R18 | atuacao=apps | Mobile +6 |
| R19 | ferramenta=mobile | Mobile +5 |
| R20 | plataforma=mobile E atuacao ∈ {layouts, apps, algoritmos} | Mobile +5, Front-end −3 |
| R21 | atuacao=testar | QA +6 |
| R22 | entrega=qualidade | QA +5 |
| R23 | atuacao=priorizar | Produto +6 |
| R24 | entrega=estrategia | Produto +5 |
| R25 | pessoas=sim E ferramenta=nenhuma E entrega ∈ {estrategia, produto} | Produto +3 |

## Pontos de ambiguidade tratados

| Par confundível | Variável que desempata | Regras |
|---|---|---|
| Cientista de Dados × Engenheiro de Dados | `foco_dados` (modelagem × pipelines) e nível de matemática | R06, R08, R09, R11 |
| DevOps × Cloud | `escala` (operar × planejar arquitetura/custos) | R16, R17 |
| Front-end × Mobile | `plataforma` | R20 |
| Back-end × Eng. de Dados | `entrega` (lógica de negócio × dados confiáveis) | R02, R10 |
