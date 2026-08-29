import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

class Usuario:
    def __init__(self, Nome):
        self.Nome = Nome

    def dar_boas_vindas(self):
        return f"Bem-vindo(a) ao sistema de monitoramento, {self.Nome}!"


def exibir_painel_interativo():
    print(f"""╔══════════════════════════════════════════╗
             MENU PRINCIPAL                
╚══════════════════════════════════════════╝
[0] - Finalizar Execução do Sistema
[1] - Cadastrar / Adicionar Novo Som
[2] - Simular Detecção de Áudio (Câmera e HUD Tátil)
[3] - Acessar Painel de Descobertas (Relatório Semanal de Autonomia)
[4] - Configurar Intensidade da Vibração (Motor Háptico)""")

sons_pandas = [{"Som": "Alarme", "Intensidade": "Alta"}]
historico_pandas = [{
    "Historico_Alerta": "Som detectado a 240° vindo de Oeste (Esquerda)",
    "Direção": "Direita",
    "Ângulo": "90°"
}]

try:
    df_frequencia_sons = pd.read_csv("sons_cadastrados.csv")
    sons_pandas = df_frequencia_sons.to_dict(orient="records")
except FileNotFoundError:
    print("Arquivo 'sons_cadastrados.csv' não encontrado.")

try:
    df_direcao_sons = pd.read_csv("historico_alertas.csv")
    historico_pandas = df_direcao_sons.to_dict(orient="records")
except FileNotFoundError:
    print("Arquivo 'historico_alertas.csv' não encontrado.")


def cadastrar_som():
    while True:
        print("Redirecionando para a opção 1...\n")

        som = input("Insira o som que deseja registrar: ").strip()
        intensidade = input("Insira a intensidade do som que deseja registrar: ").strip()

        if som and intensidade and som.replace(" ", "").isalpha() and intensidade.replace(" ", "").isalpha():
            break
        else:
            print("Erro: Digite apenas nomes de texto, sem números!")

    sons_pandas.append({
        "Som": som,
        "Intensidade": intensidade
    })

    df = pd.DataFrame(sons_pandas)
    df.to_csv("sons_cadastrados.csv", index=False, encoding="utf-8")
    print(sons_pandas)


def simular_audio():
    print("Redirecionando para a opção 2...\n")

    while True:
        try:
            angulo = int(input("\nDigite o ângulo do som (0°-360°): "))
            if angulo < 0 or angulo > 360:
                print("Digite um ângulo de 0° a 360°.")
                continue
            break
        except ValueError:
            print("Digite um valor numérico válido. (0°-360°)")
            continue

    if angulo >= 45 and angulo < 135:
        direcao = "Leste (Direita)"
    elif angulo >= 135 and angulo < 225:
        direcao = "Sul (Atrás)"
    elif angulo >= 225 and angulo < 315:
        direcao = "Oeste (Esquerda)"
    else:
        direcao = "Norte (Frente)"

    alerta = f"Som detectado a {angulo}° vindo de {direcao}"
    print(alerta)

    historico_pandas.append({
        "Historico_Alerta": alerta,
        "Direção": direcao,
        "Ângulo": angulo
    })

    df = pd.DataFrame(historico_pandas)
    df.to_csv("historico_alertas.csv", index=False, encoding="utf-8")


def painel_descobertas():
    print("\nRedirecionando para a opção 3...\n")
    print("[1] - Ver registros de sons [2] - Ver registros de histórico de alertas")

    while True:
        try:
            opcao = int(input("Escolha uma opção do menu: "))
            if opcao not in (1, 2):
                print("Opção inválida! Escolha 1 ou 2.")
                continue
            break
        except ValueError:
            print("Opção inválida! Digite apenas 1 ou 2.")
            continue

    if opcao == 1:
        try:
            df_frequencia_sons = pd.read_csv("sons_cadastrados.csv")
            print(df_frequencia_sons)

            df_frequencia_sons = df_frequencia_sons.dropna(subset=["Intensidade"])
            df_frequencia_sons["Intensidade"] = df_frequencia_sons["Intensidade"].astype(str)
            contagem_frequencia = Counter(df_frequencia_sons["Intensidade"])

            x = list(contagem_frequencia.keys())
            y = list(contagem_frequencia.values())

            plt.title("Gráfico de média de intensidade")
            plt.xlabel("Intensidade")
            plt.ylabel("Frequência")
            plt.bar(x, y)
            plt.show()

        except FileNotFoundError:
            print("Arquivo 'sons_cadastrados.csv' não encontrado.")

    elif opcao == 2:
        try:
            df_direcao_sons = pd.read_csv("historico_alertas.csv")
            print(df_direcao_sons)

            df_direcao_sons = df_direcao_sons.dropna(subset=["Direção"])
            df_direcao_sons["Direção"] = df_direcao_sons["Direção"].astype(str)
            contagem_frequencia = Counter(df_direcao_sons["Direção"])

            x = list(contagem_frequencia.keys())
            y = list(contagem_frequencia.values())

            plt.title("Gráfico de média de alertas por sentido")
            plt.xlabel("Sentido")
            plt.ylabel("Quantidade de Alertas")
            plt.bar(x, y)
            plt.show()

        except FileNotFoundError:
            print("Arquivo 'historico_alertas.csv' não encontrado.")


def configurar_intensidade():
    print("\nRedirecionando para a opção 4...\n")
    print("[1] - Intensidade baixa [2] - Intensidade Média [3] - Intensidade Alta")

    while True:
        try:
            opcao = int(input("Escolha uma opção do menu: "))
            if opcao not in (1, 2, 3):
                print("Opção inválida! Escolha um número de 1-3.")
                continue
            break
        except ValueError:
            print("Opção inválida! Digite apenas 1, 2 ou 3.")
            continue

    if opcao == 1:
        print("Intensidade de vibração ajustada para baixa")
    elif opcao == 2:
        print("Intensidade de vibração ajustada para média")
    elif opcao == 3:
        print("Intensidade de vibração ajustada para alta")


Nome = Usuario(input("Digite seu nome: "))
print(Nome.dar_boas_vindas())

while True:
    exibir_painel_interativo()
    try:
        opcao = int(input("Escolha uma opção do menu: "))
    except ValueError:
        print("\nErro: Digite apenas números inteiros correspondentes às opções.\n")
        continue

    match opcao:
        case 0:
            print("\nFim!\n")
            break
        case 1:
            cadastrar_som()
        case 2:
            simular_audio()
        case 3:
            painel_descobertas()
        case 4:
            configurar_intensidade()
        case _:
            print("\nOpção inválida! Escolha um número listado no menu.\n")