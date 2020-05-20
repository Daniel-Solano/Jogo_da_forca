# -*- coding: utf-8 -*-
# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.letras_corretas = []
		self.letras_erradas = []
		self.escondida = []
		for x in self.word:
			self.escondida.append('_')
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word:
			self.letras_corretas.append(letter)
		else:
			self.letras_erradas.append(letter)
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if len(self.letras_erradas) > 5 or self.escondida.count('_') == 0:
			return True
		else:
			return False

	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if self.escondida.count('_') == 0:
			return True
		

	# Método para não mostrar a letra no board
	def hide_word(self, x):
		for i, x in enumerate(self.word):
			if x in self.letras_corretas:
				self.escondida[i] = x

		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.letras_erradas)])
		print('Palavra: ', ' '.join(self.escondida))
		print('Letras erradas: ', ' '.join(self.letras_erradas))
		print('Letras corretas: ', ' '.join(self.letras_corretas))

		

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
	return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while game.hangman_over() == False:
		game.print_game_status()
		while 1 > 0:
			letra = input('Digite uma letra: ')
			if letra.isdigit():
				print("Não pode ser número!")
			elif len(letra) > 1:
				print("Favor digitar apenas UMA letra!")
			elif letra in (game.letras_erradas or game.letras_corretas):
				print("Você já escolheu essa letra.")
			else:
				break
		game.guess(letra)
		game.hide_word(letra)

	# Verifica o status do jogo

	# De acordo com o status, imprime mensagem na tela para o usuário
	else:
		if game.hangman_won():
			print ('\nParabéns! Você venceu!!')
			print('\nA palavra era ' + game.word)
		else:
			print(board[len(game.letras_erradas)])
			print ('\nGame over! Você perdeu.')
			print ('A palavra era ' + game.word)

		print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
