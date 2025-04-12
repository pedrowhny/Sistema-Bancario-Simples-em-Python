# 💸 Sistema Bancário em Python (Terminal)

Este projeto é um sistema bancário simples feito em Python, executado diretamente no terminal, com interface estilizada usando **cores ANSI**, **emojis** e **boas práticas de código**. Ele permite ao usuário realizar depósitos, saques, visualizar extrato e encerrar a sessão de forma intuitiva.

---

## 📋 Funcionalidades

- 💰 **Depósito**: Adiciona valores positivos à conta.
- 💸 **Saque**: Permite até 3 saques por sessão, com limite de R$ 500,00 por saque.
- 📄 **Extrato**: Exibe um histórico das transações realizadas, junto ao saldo atual.
- ❌ **Sair**: Finaliza a execução do programa com uma mensagem de despedida.

---

## 🧠 Tecnologias Utilizadas

- **Python 3.x**
- **Módulo `os`**: Utilizado para limpar o terminal em diferentes sistemas operacionais (Windows, Linux, macOS).
- **ANSI Escape Codes**: Para cores e realce visual no terminal.

---

## ▶️ Como Executar

1. **Clone este repositório ou copie o código**:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
2. **Navegue até o diretório do projeto**:
    ```bash
    cd sistema-bancario-terminal
    ```
3. **Execute o script Python**:
    ```bash
    python sistema_bancario.py
    ```

---

## 📷 Exemplo de Execução

```bash
==================== MENU ====================
[💰] [d] Depositar
[💸] [s] Sacar
[📄] [e] Extrato
[❌] [q] Sair
=============================================
=> d

=== DEPÓSITO ===
Informe o valor do depósito: R$ 150.00

✅ Depósito realizado com sucesso!
