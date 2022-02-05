# JOGO DA FORCA
# Túlio Falcão - fevereiro de 2022

import time
import random

# criando classe do jogo
class Jogo():
    # inicializando a classe 
    def __init__(self):
        print("Iniciando Jogo da Forca...")
        time.sleep(3)
    # tela inicial
    def telaInicial(self):

        print("")
        print("="*17)
        print("  JOGO DA FORCA")
        print("="*17)
        print("")
        print("")
    # pegando dado do jogador
    def jogador(self):
        self.jogador = input("Bem vindo ao Jogo da Forca! Digite seu nome: ")
        print("")
        print(f"Bem vindo(a), {self.jogador}! Carregando o jogo...")
        print("")
        time.sleep(3)
    # lista com momentos da forca, iniciando com index 0
    def forca(self, n=0):
        self.forca = ['''
         x====x
              |
              |
              |
              |
            =====
            ''','''
         x====x
         O    |
              |
              |
              |
            =====
            ''','''
         x====x
         O    |
        /     |
              |
              |
            =====
            ''','''
         x====x
         O    |
        /|    |
              |
              |
            =====
            ''','''
         x====x
         O    |
        /|\   |
              |
              |
            =====
            ''','''
         x====x
         O    |
        /|\   |
        /     |
              |
            =====
            ''','''
         x====x
         O    |
        /|\   |
        / \   |
              |
            =====       
        ''']
        print(self.forca[n])
        print("")

    def palavraSecreta(self):
        self.texto = open('palavras.txt', 'r', encoding='utf-8') #lê o arquivo txt com as palavras
        self.palavra = self.texto.readlines() # coloca as linhas do texto como elementos de uma lista salvas em uma variável
        self.texto.close() # fecha o arquivo de texto
        self.palavraSecreta = list(random.choice(self.palavra)) # escolhe uma palavra da lista 
        self.palavraEscondida = ["_ " for x in range(len(self.palavraSecreta)-1)] # pega a palavra escolhida e a mostra com traços: _ _ _ _ 
        for x in self.palavraEscondida:
            print(x, end="") # imprime os traços da palavra sem pular linha
        print("")
        print("")
        return self.palavraEscondida # retorna a palavra escondida
        
        

    def jogada(self, palavraescond):

        self.acertos = [] # cria lista que irá armazenar as letras acertadas
        self.erros = [] # cria lista que irá armazenar as letras erradas
        self.quantidadePalavra = len(self.palavraEscondida) # pega a quantidade de letras da palavra escondida
        self.quantAcertos = len(self.acertos) # pega a quantidade de elementos da lista de acertos
        self.quantErros = len(self.erros) # pega a quantidade de elementos da lista de erros
        self.palavraEscondida2 = palavraescond # armazena a palavra escondida em outra variável

        while(self.quantAcertos < self.quantidadePalavra  or self.quantErros < 6): # loop do jogo

            self.escolha = input("Escolha uma letra: ") # pega a palavra escolhida do jogador e a armazena em uma variável
            print("")
            print("")

            if self.escolha in self.palavraSecreta: # se a letra escolhida estiver na lista palavra secreta

                self.acertos.append(self.escolha) # coloca a letra na lista de acertos
               
                ind = [] # lista para armazenar o index da letra na palavra secreta
                for x in range(self.quantidadePalavra):
                    if self.palavraSecreta[x] == self.escolha: # varre cada letra da palavra secreta e se ela for igual a letra escolhida pelo usuário, é armazenado o index da letra
                        ind.append(x) # insere o index da letra na lista ind

                for x in range(self.quantidadePalavra):
                    if x in ind:
                        self.palavraEscondida2[x] = self.escolha # na segunda variável criada para a palavra escondida, troca-se a linha "_ " pela letra escolhida pelo usuário através do index
                    
                # imprime na tela as letras escolhidas que acarretaram em acerto
                print("ACERTOS: \n")
                for x in self.acertos:
                    print(x + " - ", end="")
                print("")
                print("")
                #imprime na tela as letras escolhidas que acarretaram em erro
                print("ERROS: \n")
                for x in self.erros:
                    print(x + " - ", end="")
                print("")
                print("")

                #imprime a palavra escondida com as letras acertadas pelo usuário
                for x in self.palavraEscondida2:
                    print(x, end="")
                print("")
                print("")

                self.quantAcertos += 1 # adiciona o número de acertos

                if self.quantAcertos == self.quantidadePalavra: # se a quantidade de acertos for igual a quantidade de letras da palavra secreta, o usuário vence o jogo
                    print("")
                    print("PARABÉNS! VOCÊ VENCEU!")
                    break

            else: # caso a letra escolhida acarrete em erro
                self.erros.append(self.escolha) # salva a letra na lista de erros
                print(self.forca[len(self.erros)]) # imprime na tela a figura da forca correspondente a quantidade de erros
                print("")
                print("")

                print("ACERTOS: \n") # imprime as letras acertadas
                for x in self.acertos:
                    print(x + " - ", end="")
                print("")
                print("")

                print("ERROS: \n") # imprime as letras erradas
                for x in self.erros:
                    print(x + " - ", end="")
                print("")
                print("")

                for x in self.palavraEscondida2:
                    print(x, end="") #imprime a variável com a palavra escondida com o as letras acertadas
                print("")
                print("")

                self.quantErros += 1 # adiciona a quantidade de erros
            
                if self.quantErros == 6: # se a quantidade de erros for igual a 6, o usuário perde o jogo
                    print("")
                    print("GAME OVER!")
                    break
        

if __name__ == "__main__":
    import sys
