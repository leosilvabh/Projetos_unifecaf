import os
os.system('cls') #executando cls do sistema operacional

opcao_Menu = ""


pecas_aprovadas = []
pecas_reprovadas = []

CAIXA_CAPACIDADE = 10
caixa_atual = []       # peças aprovadas ainda não fechadas
caixas_fechadas = []   # cada item é uma lista com até 10 peças



def limpa_tela():
    os.system('cls')# system é como se abrisse um prompt para executar o cls

def pausar():
    input("Digite ENTER para continuar")

def cadastrar_nova_peca(): #Função para cadastrar uma nova peça. 
    print("\n=== Cadastrar nova peça ===")
    id_peca = input("ID da peça: ")
    peso = float(input("Peso da peça (g): "))
    cor = input("Cor da peça: ").lower()
    comprimento = float(input("Comprimento da peça (cm): "))

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    aprovada, motivos = verificar_peca(peca)
    if aprovada:
        pecas_aprovadas.append(peca)
        print(f"✅ Peça {id_peca} APROVADA e armazenada.")
    else:
        pecas_reprovadas.append({"peca": peca, "motivos": motivos})
        print(f"❌ Peça {id_peca} REPROVADA. Motivos: {', '.join(motivos)}")

    pausar()
    limpa_tela()


    # --- Lógica de caixa ---
    caixa_atual.append(peca)
    print(f"Adicionada à caixa atual ({len(caixa_atual)}/{CAIXA_CAPACIDADE}).")

    if len(caixa_atual) >= CAIXA_CAPACIDADE:
        caixas_fechadas.append(list(caixa_atual))  # salva cópia da caixa cheia
        caixa_atual.clear()                         # inicia nova caixa
        print("📦 Caixa CHEIA e FECHADA! Nova caixa iniciada.")


def verificar_peca(peca):
    motivos = []

    if not (95 <= peca["peso"] <= 105):
        motivos.append("Peso fora do limite")

    if peca["cor"] not in ["azul", "verde"]:
        motivos.append("Cor inválida")

    if not (10 <= peca["comprimento"] <= 20):
        motivos.append("Comprimento fora do limite")

    if motivos:
        return False, motivos  # reprovada
    else:
        return True, []         # aprovada

def listar_pecas():
    print("\n=== Listar peças ===")

    print(f"\nAprovadas (total {len(pecas_aprovadas)}):")
    if pecas_aprovadas:
        for peca in pecas_aprovadas:
            print(f"  - ID {peca['id']} | {peca['peso']}g | {peca['comprimento']}cm | cor={peca['cor']}")
    else:
        print("  (nenhuma)")

    print(f"\nReprovadas (total {len(pecas_reprovadas)}):")
    if pecas_reprovadas:
        for r in pecas_reprovadas:
            p = r["peca"]
            print(f"  - ID {p['id']}: {', '.join(r['motivos'])}")
    else:
        print("  (nenhuma)")

    pausar()
    limpa_tela()
def remover_pecas():
    print("\n=== Remover peça cadastrada ===")
    ID_Digitado = input("Informe o ID da peça a remover: ").strip()#Strip serve para retirar possiveis espacos do texto, no inicio e no final
    if not ID_Digitado:
        print("ID não pode ser vazio.")
        pausar()
        return

    # Remover da lista de peças reprovadas
    for indice, registro in enumerate(pecas_reprovadas): #enumerate busca a posição do item na lista e o item em si
        if registro["peca"]["id"] == ID_Digitado:
            pecas_reprovadas.pop(indice)
            print(f"Peça {ID_Digitado} removida da lista de reprovadas.")
            pausar()
            return# encerra a função

    # Remover da lista de peças aprovadas 
    for indice, peca in enumerate(pecas_aprovadas):
        if peca["id"] == ID_Digitado:
            pecas_aprovadas.pop(indice)
            print(f"Peça {ID_Digitado} removida da lista de aprovadas.")
            pausar()
            return

    # 3) Não encontrada
    print("Peça não encontrada nas listas.")
    pausar()
    limpa_tela()

def listar_caixas():
    print("\n=== Caixas fechadas ===")
    if not caixas_fechadas:
        print("(nenhuma caixa fechada ainda)")
    else:
        for numero_caixa, caixa in enumerate(caixas_fechadas, start=1):
            print(f"\nCaixa #{numero_caixa} - {len(caixa)}/{CAIXA_CAPACIDADE} peças")
            for p in caixa:
                print(f"  - ID {p['id']} | {p['peso']}g | {p['comprimento']}cm | cor={p['cor']}")

    print(f"\nCaixa atual (aberta): {len(caixa_atual)}/{CAIXA_CAPACIDADE} peças")
    if caixa_atual:
        for peca in caixa_atual:
            print(f"  - ID {peca['id']} | {peca['peso']}g | {peca['comprimento']}cm | cor={peca['cor']}")

    pausar()
    limpa_tela()

def gerar_relatorio():
    print("\n=== Relatório Final ===")

    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    # conta caixas fechadas + a caixa atual (se tiver algo dentro)
    total_caixas = len(caixas_fechadas) + (1 if caixa_atual else 0)

    print(f"Total de peças aprovadas: {total_aprovadas}")
    print(f"Total de peças reprovadas: {total_reprovadas}")
    print(f"Quantidade de caixas utilizadas: {total_caixas}")

    print("\nMotivos das reprovações:")
    if pecas_reprovadas:
        for r in pecas_reprovadas:
            p = r["peca"]
            print(f"  - Peça {p['id']}: {', '.join(r['motivos'])}")
    else:
        print("  (sem reprovações)")

    pausar()
    limpa_tela()

while opcao_Menu != 0:#serve para repetir as coisas. Nesse caso ele foi utilizado para só sair do menu se a pessoa digitar o 0 !=(enquanto for diferente)
    print ("\n=========== Menu de opcoes:===========")
    print ("1 - Cadastrar nova peça")
    print ("2 - Listar pecas aprovadas/reprovadas")
    print ("3 - Remover peça cadastrada")
    print ("4 - Listar caixas fechadas")
    print ("5 - Gerar relatorio final")
    print ("0 - Sair")
    print ('=' * 38)#repete 38x o sinal de =

    opcao_Menu = input ("Digite a opção desejada: ")
    if opcao_Menu == "1": #Se vai sempre ser a primeira opção. 
        limpa_tela()
        cadastrar_nova_peca()
        
    elif opcao_Menu == "2":
        print ("-------------")
        limpa_tela()
        listar_pecas()
        print ("-------------")
    elif opcao_Menu == "3":
        print ("-------------")
        limpa_tela()
        remover_pecas()
        print ("-------------")
    elif opcao_Menu == "4":
        print ("-------------")
        limpa_tela()
        listar_caixas()
        print ("-------------")
    elif opcao_Menu == "5":
        print ("-------------")
        limpa_tela()
        gerar_relatorio()
        print ("-------------")
         
    elif opcao_Menu == "0":
        print ("-------------")
        print ("Sistema encerrado!")
        print ("-------------")
        break
    else:#se o else existir, ele sempre tem que ser a ultima opção.(else: caso os outros forem falsos)
        print ("-------------")
        print ("Opção inválida. Tente novamente...")
        print ("-------------")

