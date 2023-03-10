# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:49:41 2023

@author: Domingos_Gnd
"""
import datetime
import webbrowser
import os
import random

# Função para saudação
def saudacao():
    # Defina as saudações
    saudacoes = ['Olá!', 'Oi!', 'E aí?', 'Tudo bem?']
    # Escolha uma saudação aleatória
    saudacao = random.choice(saudacoes)
    # Obter a hora atual
    hora_atual = datetime.datetime.now().hour
    # Defina a mensagem de acordo com a hora
    if hora_atual < 12:
        mensagem = f'{saudacao} Bom dia!'
    elif 12 <= hora_atual < 18:
        mensagem = f'{saudacao} Boa tarde!'
    else:
        mensagem = f'{saudacao} Boa noite!'
    # Imprimir a mensagem de saudação
    print(mensagem)

# Função para abrir um site
def abrir_site(url):
    # Verificar se o site começa com http ou https
    if url.startswith('http://') or url.startswith('https://'):
        webbrowser.open(url)
    else:
        webbrowser.open('http://' + url)

# Função para abrir um arquivo
def abrir_arquivo(caminho):
    # Verificar se o arquivo existe
    if os.path.exists(caminho):
        os.startfile(caminho)
    else:
        print('Arquivo não encontrado!')

# Função principal
def main():
    # Saudar o usuário
    saudacao()
    # Loop infinito para receber os comandos do usuário
    while True:
        # Obter o comando do usuário
        comando = input('O que você deseja fazer? ')
        # Verificar se o comando é "sair"
        if comando == 'sair':
            print('Até logo!')
            break
        # Verificar se o comando é "abrir site"
        elif comando.startswith('abrir site'):
            # Obter o URL do comando
            url = comando.split(' ')[-1]
            # Abrir o site
            abrir_site(url)
        # Verificar se o comando é "abrir arquivo"
        elif comando.startswith('abrir arquivo'):
            # Obter o caminho do arquivo do comando
            caminho = comando.split(' ')[-1]
            # Abrir o arquivo
            abrir_arquivo(caminho)
        # Comando inválido
        else:
            print('Comando inválido! Tente novamente.')

# Chamar a função principal
if __name__ == '__main__':
    main()
