import os  # Importa o módulo 'os' para limpar o terminal (funciona em Windows, Linux e Mac)

# Menu principal com estilo e cores usando ANSI escape codes
menu = """
\033[1;32m
==================== MENU ====================
\033[0m
[💰] [d] Depositar
[💸] [s] Sacar
[📄] [e] Extrato
[❌] [q] Sair
\033[1;32m=============================================
\033[0m
=> """

# Variáveis principais do sistema bancário
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite máximo por saque
extrato = ""  # Histórico de transações
numero_saques = 0  # Contador de saques feitos
LIMITE_SAQUES = 3  # Máximo de saques permitidos por sessão

# Função para limpar o terminal, mantendo a interface limpa
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# Loop principal que mantém o programa rodando até o usuário escolher sair
while True:
    limpar_terminal()  # Limpa a tela antes de exibir o menu
    opcao = input(menu).lower().strip()  # Lê a opção do usuário e normaliza o texto

    # DEPÓSITO
    if opcao == "d":
        limpar_terminal()
        print("\n\033[1;34m=== DEPÓSITO ===\033[0m")
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor  # Atualiza o saldo
            extrato += f"[+ 💰] Depósito: R$ {valor:.2f}\n"  # Registra no extrato
            print("\n✅ Depósito realizado com sucesso!")
        else:
            print("\n❌ Operação falhou! Valor inválido.")

    # SAQUE
    elif opcao == "s":
        limpar_terminal()
        print("\n\033[1;34m=== SAQUE ===\033[0m")
        valor = float(input("Informe o valor do saque: R$ "))

        # Validações de segurança para o saque
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        # Mensagens específicas de erro
        if excedeu_saldo:
            print("\n❌ Saldo insuficiente.")
        elif excedeu_limite:
            print("\n❌ O valor do saque excede o limite de R$ 500,00.")
        elif excedeu_saques:
            print("\n❌ Número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor  # Atualiza o saldo
            extrato += f"[- 💸] Saque: R$ {valor:.2f}\n"  # Registra no extrato
            numero_saques += 1  # Incrementa contador de saques
            print("\n✅ Saque realizado com sucesso!")
        else:
            print("\n❌ Operação falhou! Valor inválido.")

    # EXTRATO
    elif opcao == "e":
        limpar_terminal()
        print("\n\033[1;35m========= 📄 EXTRATO 📄 =========\033[0m")
        print(extrato if extrato else "⚠️  Nenhuma movimentação registrada.")  # Mostra o extrato ou uma mensagem padrão
        print(f"\n💼 Saldo disponível: \033[1;32mR$ {saldo:.2f}\033[0m")
        print("\033[1;35m=================================\033[0m")
        input("\nPressione [Enter] para voltar ao menu...")

    # SAIR DO SISTEMA
    elif opcao == "q":
        limpar_terminal()
        print("\n👋 Obrigado por usar nosso sistema bancário!\n")
        break  # Encerra o loop e finaliza o programa

    # OPÇÃO INVÁLIDA
    else:
        limpar_terminal()
        print("\n❌ Opção inválida. Tente novamente.")
        input("Pressione [Enter] para voltar ao menu...")
