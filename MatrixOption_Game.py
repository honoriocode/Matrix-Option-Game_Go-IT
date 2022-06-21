#Code by HonorioCode

print('Olá Jovem! ')
escolha = input('...')
print('Aqui é a inteligência artificial da GO-IT')
escolha = input('...')
print('O seu eu de outro universo quer falar com você')
escolha = input('...')
print('Oi')

while escolha != 'oi' or escolha != 'Oi':
    escolha = input('...')
    if escolha == 'oi' or escolha == 'Oi':
        break
    else:
        print('Seja educado')
        continue

print('Preciso te informar sobre algo!')
escolha = input('...')
print('Calma, antes tenho que confirmar alguns dados')
escolha = input('...')
print('Qual o seu nome no seu universo ?')
nome = input('...')
print(f'Seu nome nessa realidade é {nome} ?')

while escolha != 'sim' or escolha != 'Sim':
    escolha = input('...')
    if escolha == 'sim' or escolha == 'Sim':
        break
    else:
        print('Não minta!')
        continue

print(f'Ok {nome} nesse caso podemos prosseguir')
escolha = input('...')
print(f'Então {nome} tenho uma notícia difícil pra te dar!')
escolha = input('...')
print('Você tem coragem de ouvir ?')

while escolha != 'sim' or escolha != 'Sim':
    escolha = input('...')
    if escolha == 'sim' or escolha == 'Sim':
        print('hm...')
        break
    else:
        print('Game Over Covarde!')
        quit()
print(f'Ok {nome}')
escolha = input('...')
print('Mas antes de dar a notícia, preciso de mais uma informação!')

while escolha != 'o que?' or escolha != 'O que?':
    escolha = input('...')
    if escolha == 'o que?' or escolha == 'O que?':
        break
    else:
        print('Pergunte da maneira correta!')
        continue

year = int(input('Em que ano você está na sua realidade ? '))
birth = int(input('Em que ano você nasceu na sua realidade ?'))
age = year - birth
print(f'Nessa realidade, você tem ou terá {age} anos de idade no ano de {year} ?')

while escolha != 'sim' or escolha != 'Sim':
    escolha = input('...')
    if escolha == 'sim' or escolha == 'Sim':
        break
    else:
        print('Não minta para si mesmo!')
        continue

print(f'{age} anos de idade! Interessante')

if age >= 18:
    print('Então, você já tem idade para receber a notícia!')
else:
    print('Você ainda é muito jovem para ouvir o que tenho a dizer')
    print('Sinto muito, mas nossa conversa se encerra por aqui!')
    print(f'Adeus {nome}')
    quit()

print(f'Nesse caso {nome} irei te dizer')
escolha = input('...')
print('A notícia é que...')
print('O mundo vai acabar daqui a um ano e só você pode mudar isso!!')

while escolha != 'como?' or escolha != 'Como?':
    escolha = input('...')
    if escolha == 'como?' or escolha == 'Como?':
        break
    else:
        print('Pergunte da maneira correta na sua linha do tempo!')
        continue

print('Fazendo a escolha certa!!')

while escolha != 'qual?' or escolha != 'Qual?':
    escolha = input('...')
    if escolha == 'qual?' or escolha == 'Qual?':
        break
    else:
        print('Pergunte da maneira correta!')
        continue

print("""Imagino que você deva estar se sentindo como a Alice escorregando...
...pela toca do coelho.
Você é uma pessoa que aceita o que vê porque pensa estar sonhando""")
print(f'Você acredita em destino {nome} ?')
escolha = input('...')
print('Por que ? ')
escolha = input('...')
print('Eu sei exatamente o que quer dizer!')
escolha = input('...')
print("""Deixa eu dizer porque está aqui, está aqui porque sabe de uma coisa, uma
coisa que vocÊ não sabe explicar, mas você sente.
Você sentiu a vida inteira, que há alguma coisa errada com o mundo. Você ainda não
sabe o que é, mas está ali como uma farpa na sua mente deixando o louco.
Foi essa sensação que o trouxe até aqui.
Você sabe do que estou falando ? """)

while escolha != 'programação' or escolha != 'Programação':
    escolha = input('...')
    if escolha == 'programação' or escolha == 'Programação':
        break
    else:
        print('Pense bem!')
        continue

print('Você quer saber o que é programação ? ')

while escolha != 'sim' or escolha != 'Sim':
    escolha = input('...')
    if escolha == 'sim' or escolha == 'Sim':
        break
    else:
        print('Tem certeza? Você chegou até aqui pra nada ?!')
        continue

print("""Programação está em toda parte. Está em nossa volta.
Mesmo agora, nessa sala aqui. Você a vê quando olha pela janela, ou quando liga a 
televisão. Você acende quando vai trabalhar, quando vai a igreja. Quando paga seus
impostos. É o mundo que acredita ser real para que não veja a verdade""")

while escolha != 'que verdade?' or escolha != 'Que verdade?':
    escolha = input('...')
    if escolha == 'que verdade?' or escolha == 'Que verdade?':
        break
    else:
        print('Questione corretamente!')
        continue

print(f'Que você é um escravo {nome}, como todo mundo você nasceu em cativeiro.')
print('E só a programação pode te libertar')
print("""Infelizmente não se pode explicar o que é programação, é preciso que
veja por si mesmo. Essa é a sua última chance, depois disso não haverá retorno""")


def menuPill():
    print('[1] Pílula azul ')
    print('[2] Pílula vermelha')
    print("""\n Se escolher a pílula azul, fim da história. Vai acordar na sua cama e
    acreditar no que quiser \n""")
    print("""Se escolher a pílula vermelha, fica no país das maravilhas...e eu vou
    mostrar até onde vai a toca do coelho.""")

menuPill()
escolha = input('...')
print('Lembre-se, eu estou oferecendo a verdade, nada mais')

option = None

while option != '1':
    option = input('...')
    if option == '2':
        print('Bem vindo ao mundo real...da programação!')
        print("Você finalizou o jogo, o seu mundo será salvo graças aos seus...")
        print('...conhecimentos de programação adquiridos na GO-IT! O Mundo é seu!!')
        break
    else:
        print('O mundo dependia de você e você falhou!! Game Over!!')
        quit()
