from career_expert.engine import diagnosticar
from career_expert.personas import PERSONAS


def test_personas():
    for persona in PERSONAS:
        resultado, regras = diagnosticar(persona["respostas"])
        assert resultado["trilha"] == persona["esperado"], persona["nome"]
        assert len(regras) > 0


def test_cientista_vs_engenheiro_de_dados():
    cientista = {"matematica": "alta", "atuacao": "dados_brutos", "ferramenta": "python",
                 "entrega": "insights", "foco_dados": "modelagem"}
    engenheiro = {"matematica": "media", "atuacao": "dados_brutos", "ferramenta": "python",
                  "entrega": "dados_confiaveis", "foco_dados": "pipelines"}
    assert diagnosticar(cientista)[0]["trilha"] == "ciencia_dados"
    assert diagnosticar(engenheiro)[0]["trilha"] == "eng_dados"


def test_devops_vs_cloud():
    devops = {"matematica": "media", "atuacao": "servidores", "ferramenta": "linux_redes",
              "entrega": "infra", "escala": "nao"}
    cloud = {"matematica": "media", "atuacao": "servidores", "ferramenta": "linux_redes",
             "entrega": "infra", "escala": "sim"}
    assert diagnosticar(devops)[0]["trilha"] == "devops"
    assert diagnosticar(cloud)[0]["trilha"] == "cloud"


def test_frontend_vs_mobile():
    web = {"matematica": "baixa", "atuacao": "layouts", "ferramenta": "nenhuma",
           "entrega": "produto", "plataforma": "web"}
    celular = {"matematica": "baixa", "atuacao": "layouts", "ferramenta": "nenhuma",
               "entrega": "produto", "plataforma": "mobile"}
    assert diagnosticar(web)[0]["trilha"] == "frontend"
    assert diagnosticar(celular)[0]["trilha"] == "mobile"
