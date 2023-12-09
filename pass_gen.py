#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import StringVar
import random
import string

def gerar_senha():
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(6))
    senha_var.set(senha)

# Configuração da janela
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Variável para armazenar a senha
senha_var = StringVar()

# Rótulo para exibir a senha
rotulo_senha = tk.Label(janela, text="Senha:")
rotulo_senha.pack(pady=10)

# Campo de entrada para exibir a senha gerada
entrada_senha = tk.Entry(janela, textvariable=senha_var, state="readonly", width=10)
entrada_senha.pack(pady=10)

# Botão para gerar senha
botao_gerar_senha = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
botao_gerar_senha.pack(pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()


# In[ ]:




