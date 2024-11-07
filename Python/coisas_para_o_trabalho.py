from colorama import Fore, Back # aqui nos importamos cores para usar nos textos # Fore serve para chamar as cores # o Back serve para mudar a cor do fundo 
from getpass import getpass # aqui importamos o getpass que serve para dar um enter para iniciar o programa
from random import randrange, randint # servera para o jogo para pormos um posição aliatoria 

print(Fore.GREEN + Back.WHITE + "Bem vindo ao jogo das Naves "+ Fore.RESET + Back.RESET) # aqui damos uma cor para o texto e um fundo 
getpass("Prima ENTER para continuar...")#o getpass serve para iniciar o programa quando damos enter
print(Fore.BLUE + "Outro Texto" + Fore.RESET)