import random


def introducao():
    print('\n-=-=-= JOGO DE PALAVRAS -=-=-=\n')
    print('Você deverá adivinhar qual palavra o computador escolheu!')
    print('Vamos Começar!!\n')


def dicas(numero: int) -> str:
    if numero == 0:
        return 'Local onde as pessoas residem!'
    if numero == 1:
        return 'Objeto usado para fazer ligações, enviar mensagens etc'
    if numero == 2:
        return 'Local onde as pessoas podem comprar medicamentos'
    if numero == 3:
        return 'Usado para escrever, muito útil para alunos, por exemplo'
    if numero == 4:
        return 'Local fora da casa das pessoas onde podem guardar seus pertences, como móveis e documentos'



palavras = ('Casa', 'Celular', 'Farmácia', 'Caderno', 'Storage')
numeroPalavra = random.randint(0,4) #Número de 0 até 4 sorteado

introducao()
palavra = palavras[numeroPalavra]

dicas(numeroPalavra)

while True:
    
    palavraUsuario = str(input("Digite seu palpite ou 'exit' para sair: "))
    if palavraUsuario == 'exit':
        print('Saindo do jogo!')
        break
        
    
