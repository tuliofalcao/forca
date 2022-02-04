import time
import random

class Jogo():

    def __init__(self):
        print("Iniciando Jogo da Forca...")
        time.sleep(3)

    def telaInicial(self):

        print("")
        print("="*17)
        print("  JOGO DA FORCA")
        print("="*17)
        print("")
        print("")

    def jogador(self):
        self.jogador = input("Bem vindo ao Jogo da Forca! Digite seu nome: ")
        print("")
        print(f"Bem vindo(a), {self.jogador}! Carregando o jogo...")
        print("")
        time.sleep(3)

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
        self.texto = open('palavras.txt', 'r', encoding='utf-8')
        self.palavra = self.texto.readlines()
        self.texto.close()
        self.palavraSecreta = list(random.choice(self.palavra))
        self.palavraEscondida = ["_ " for x in range(len(self.palavraSecreta)-1)]
        for x in self.palavraEscondida:
            print(x, end="")
        print("")
        print("")
        return self.palavraEscondida
        
        

    def jogada(self, palavraescond):

        self.acertos = []
        self.erros = []
        self.quantidadePalavra = len(self.palavraEscondida)
        self.quantAcertos = len(self.acertos)
        self.quantErros = len(self.erros)
        self.palavraEscondida2 = palavraescond

        while(self.quantAcertos < self.quantidadePalavra  or self.quantErros < 6):

            self.escolha = input("Escolha uma letra: ")
            print("")
            print("")

            if self.escolha in self.palavraSecreta:

                self.acertos.append(self.escolha)
               
                ind = []
                for x in range(self.quantidadePalavra):
                    if self.palavraSecreta[x] == self.escolha:
                        ind.append(x)

                for x in range(self.quantidadePalavra):
                    if x in ind:
                        self.palavraEscondida2[x] = self.escolha
                    
                
                print("ACERTOS: \n")
                for x in self.acertos:
                    print(x + " - ", end="")
                print("")
                print("")

                print("ERROS: \n")
                for x in self.erros:
                    print(x + " - ", end="")
                print("")
                print("")

                for x in self.palavraEscondida2:
                    print(x, end="")
                print("")
                print("")

                self.quantAcertos += 1

                if self.quantAcertos == self.quantidadePalavra:
                    print("")
                    print("PARABÉNS! VOCÊ VENCEU!")
                    break

            else:
                self.erros.append(self.escolha)
                print(self.forca[len(self.erros)])
                print("")
                print("")

                print("ACERTOS: \n")
                for x in self.acertos:
                    print(x + " - ", end="")
                print("")
                print("")

                print("ERROS: \n")
                for x in self.erros:
                    print(x + " - ", end="")
                print("")
                print("")

                for x in self.palavraEscondida2:
                    print(x, end="")
                print("")
                print("")

                self.quantErros += 1
            
                if self.quantErros == 6:
                    print("")
                    print("GAME OVER!")
                    break
        

if __name__ == "__main__":
    import sys
