from . import compat
from experta import DefFacts, Fact, KnowledgeEngine, L, Rule

from .questions import TRILHAS


class Perfil(Fact):
    pass


class Fase(Fact):
    pass


class ConsultorCarreiras(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.pontos = {}
        self.motivos = {}
        for trilha in TRILHAS:
            self.pontos[trilha] = 0
            self.motivos[trilha] = []
        self.regras_disparadas = []
        self.resultado = None

    def somar(self, trilha, pontos, regra, texto):
        self.pontos[trilha] = self.pontos[trilha] + pontos
        self.motivos[trilha].append((regra, texto, pontos))
        self.regras_disparadas.append(regra + " - " + texto)

    @DefFacts()
    def inicio(self):
        yield Fase(etapa="pontuacao")

    @Rule(Perfil(atuacao="algoritmos", ferramenta=L("python") | L("sql") | L("javascript")))
    def r01(self):
        self.somar("backend", 4, "R01", "Gosta de algoritmos e domina uma linguagem de servidor ou banco")

    @Rule(Perfil(atuacao="algoritmos", entrega=L("produto") | L("infra")))
    def r02(self):
        self.somar("backend", 3, "R02", "Quer entregar a lógica de negócio que sustenta o sistema")

    @Rule(Perfil(atuacao="servidores", ferramenta=L("python") | L("sql"), matematica=L("baixa") | L("media")))
    def r03(self):
        self.somar("backend", 4, "R03", "Trabalha com servidores usando programação (APIs e bancos)")

    @Rule(Perfil(atuacao="layouts", ferramenta="javascript"))
    def r04(self):
        self.somar("frontend", 6, "R04", "Gosta de criar layouts e já usa JavaScript")

    @Rule(Perfil(atuacao="layouts", entrega="produto"))
    def r05(self):
        self.somar("frontend", 4, "R05", "Valoriza o produto final que o usuário vê")

    @Rule(Perfil(matematica="alta", atuacao="dados_brutos", foco_dados="modelagem"))
    def r06(self):
        self.somar("ciencia_dados", 7, "R06", "Matemática alta, dados brutos e foco em modelagem")

    @Rule(Perfil(ferramenta="python", entrega="insights"))
    def r07(self):
        self.somar("ciencia_dados", 4, "R07", "Python e entrega de insights")

    @Rule(Perfil(foco_dados="modelagem", matematica=L("baixa") | L("media")))
    def r08(self):
        self.somar("ciencia_dados", -3, "R08", "Modelagem exige mais base em estatística")
        self.somar("eng_dados", 1, "R08", "Perfil de dados com menos matemática combina com engenharia")

    @Rule(Perfil(atuacao="dados_brutos", foco_dados="pipelines"))
    def r09(self):
        self.somar("eng_dados", 7, "R09", "Prefere construir pipelines a modelar dados")

    @Rule(Perfil(entrega="dados_confiaveis", ferramenta=L("python") | L("sql")))
    def r10(self):
        self.somar("eng_dados", 5, "R10", "Quer entregar dados confiáveis usando Python ou SQL")

    @Rule(Perfil(atuacao="dados_brutos", foco_dados="pipelines", matematica=L("baixa") | L("media")))
    def r11(self):
        self.somar("eng_dados", 2, "R11", "Engenharia de dados não exige estatística avançada")
        self.somar("ciencia_dados", -2, "R11", "Sem foco em modelagem estatística")

    @Rule(Perfil(atuacao="seguranca", ferramenta="linux_redes"))
    def r12(self):
        self.somar("ciberseguranca", 6, "R12", "Interesse em segurança e base em Linux e redes")

    @Rule(Perfil(entrega="seguranca"))
    def r13(self):
        self.somar("ciberseguranca", 5, "R13", "Quer entregar proteção contra invasões")

    @Rule(Perfil(atuacao="automatizar", ferramenta="linux_redes"))
    def r14(self):
        self.somar("devops", 6, "R14", "Gosta de automatizar e domina Linux")

    @Rule(Perfil(atuacao="automatizar", entrega="infra"))
    def r15(self):
        self.somar("devops", 4, "R15", "Automação com foco na infraestrutura")

    @Rule(Perfil(atuacao="servidores", entrega="infra", escala="nao"))
    def r16(self):
        self.somar("devops", 3, "R16", "Prefere operar servidores a planejar arquitetura em nuvem")
        self.somar("cloud", -1, "R16", "Não demonstra interesse em planejar escalabilidade")

    @Rule(Perfil(atuacao="servidores", entrega="infra", escala="sim"))
    def r17(self):
        self.somar("cloud", 6, "R17", "Infraestrutura com interesse em escalabilidade e custos")

    @Rule(Perfil(atuacao="apps"))
    def r18(self):
        self.somar("mobile", 6, "R18", "Quer criar aplicativos para celular")

    @Rule(Perfil(ferramenta="mobile"))
    def r19(self):
        self.somar("mobile", 5, "R19", "Já usa Dart, Kotlin ou Swift")

    @Rule(Perfil(plataforma="mobile", atuacao=L("layouts") | L("apps") | L("algoritmos")))
    def r20(self):
        self.somar("mobile", 5, "R20", "Plataforma preferida é o celular")
        self.somar("frontend", -3, "R20", "Prefere celular em vez de web")

    @Rule(Perfil(atuacao="testar"))
    def r21(self):
        self.somar("qa", 6, "R21", "Gosta de testar e caçar bugs")

    @Rule(Perfil(entrega="qualidade"))
    def r22(self):
        self.somar("qa", 5, "R22", "Quer entregar software confiável")

    @Rule(Perfil(atuacao="priorizar"))
    def r23(self):
        self.somar("produto", 6, "R23", "Gosta de ouvir clientes e priorizar o que construir")

    @Rule(Perfil(entrega="estrategia"))
    def r24(self):
        self.somar("produto", 5, "R24", "Valoriza resultado de negócio e estratégia")

    @Rule(Perfil(pessoas="sim", ferramenta="nenhuma", entrega=L("estrategia") | L("produto")))
    def r25(self):
        self.somar("produto", 3, "R25", "Gosta de lidar com pessoas e não tem foco técnico")

    @Rule(Fase(etapa="pontuacao"), salience=-100)
    def decidir(self):
        melhor = None
        for trilha in self.pontos:
            if melhor is None or self.pontos[trilha] > self.pontos[melhor]:
                melhor = trilha

        ranking = sorted(self.pontos.items(), key=pegar_pontos, reverse=True)

        self.resultado = {
            "trilha": melhor,
            "nome": TRILHAS[melhor],
            "pontos": self.pontos[melhor],
            "ranking": ranking,
            "motivos": self.motivos[melhor],
            "inconclusivo": self.pontos[melhor] <= 0,
        }


def pegar_pontos(item):
    return item[1]


def diagnosticar(respostas):
    if "foco_dados" not in respostas:
        respostas["foco_dados"] = "nao_se_aplica"
    if "escala" not in respostas:
        respostas["escala"] = "nao"
    if "plataforma" not in respostas:
        respostas["plataforma"] = "indiferente"
    if "pessoas" not in respostas:
        respostas["pessoas"] = "nao"

    motor = ConsultorCarreiras()
    motor.reset()
    motor.declare(Perfil(**respostas))
    motor.run()
    return motor.resultado, motor.regras_disparadas
