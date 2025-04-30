import tkinter as tk
import random
from tkinter import messagebox

# Gera um novo número aleatório entre 0 e 10
def gerar_novo_numero():
    return random.randint(0, 10)

# Variáveis globais
numero_secreto = gerar_novo_numero()
acertos = 0
erros = 0
tentativas = 0
tentativas_rodada = 0

# Atualiza estatísticas na interface
def atualizar_estatisticas():
    estatisticas['text'] = f"Tentativas: {tentativas} | Acertos: {acertos} | Erros: {erros}"

# Verifica o número digitado
def verificar_numero(event=None):
    global numero_secreto, acertos, erros, tentativas, tentativas_rodada
    try:
        numero_escolhido = int(entrada.get())
        if 0 <= numero_escolhido <= 10:
            tentativas += 1
            tentativas_rodada += 1
            if numero_escolhido == numero_secreto:
                acertos += 1
                porcentagem = (1 / tentativas_rodada) * 100
                messagebox.showinfo(
                    "Resultado",
                    f"Parabéns! Você acertou!\n"
                    f"Tentativas nessa rodada: {tentativas_rodada}\n"
                    f"Porcentagem de acerto: {porcentagem:.2f}%"
                )
                numero_secreto = gerar_novo_numero()
                tentativas_rodada = 0  # reinicia para próxima rodada
            else:
                erros += 1
                messagebox.showinfo("Resultado", f"Que pena! O número era {numero_secreto}. Tente novamente!")
                numero_secreto = gerar_novo_numero()
            entrada.delete(0, tk.END)
            atualizar_estatisticas()
        else:
            messagebox.showwarning("Aviso", "Digite um número entre 0 e 10.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")

# Interface gráfica
janela = tk.Tk()
janela.title("Jogo de Adivinhação")
janela.geometry("400x250")

# Texto de instrução
frase = tk.Label(janela, text="Escolha um número de 0 a 10 e veja se você conseguiu acertar")
frase.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(janela)
entrada.pack(pady=5)
entrada.focus()

# Botão de verificação
botao = tk.Button(janela, text="Verificar", command=verificar_numero)
botao.pack(pady=10)

# Texto das estatísticas
estatisticas = tk.Label(janela, text="Tentativas: 0 | Acertos: 0 | Erros: 0", fg="blue")
estatisticas.pack(pady=10)

# Atalho para tecla Enter
janela.bind('<Return>', verificar_numero)

# Inicia o programa
janela.mainloop()
