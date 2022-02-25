from math import tan, cos, sin, radians, hypot

#import pygame

from random import shuffle, choice, randint

from time import sleep

from datetime import date

def desafio001():
  print ('Olá, Mundo!')

def desafio002():
  nome = input('Digite seu nome: ')
  print(f'É um prazer te conhecer, {nome}!')



def desafio003():
  n1 = int(input('Digite um valor: '))
  n2 = int(input('Digite outro valor: '))
  soma = n1 + n2
  return soma



def desafio004():
  a = input('Digite algo: ')
  print('O tipo primitivo desse valor é', type(a))
  print('Só tem espaços?', a.isspace())
  print('É um número?', a.isnumeric())
  print('É alfabético?', a.isalpha())
  print('É alfanumérico?', a.isalnum())
  print('Está em maiúsculas?', a.isupper())
  print('Está em minúsculas?', a.islower())
  print('Está capitalizada?', a.istitle())



def desafio005():
  n = int(input('Digite um número: '))

  print(f'analisando o valor {n}, seu antecessor é {n-1} e o sucessor é {n+1}')



def desafio006():
  n = int(input('Digite um número: '))
  
  print(f' O dobro de {n} vale {n*2}.')
  print(f' O triplo de {n} vale {n*3} \n A raiz quadrada de {n} é igual a {n**(1/2)}.')



def desafio007():
  n1 = float(input('Primeira nota do aluno: '))
  n2 = float(input('Segunda nota do aluno: '))
  m = (n1 + n2) / 2

  print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, m))


def desafio008():
  média = float(input('Uma distância em metros: '))
  dam = média / 10
  hm = média / 100
  km = média / 1000
  dm = média * 10
  cm = média * 100
  mm = média * 1000

  print('a média  de  {}m coresponde a \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(média, km, hm, dam, dm, cm, mm))



def desafio009():
  n = int(input('Digite um número para ver sua tabuada: '))

  print('_' * 12)
  print('{} * {:2} = {}'.format(n, 1, n*1))
  print('{} * {:2} = {}'.format(n, 2, n*2))
  print('{} * {:2} = {}'.format(n, 3, n*3))
  print('{} * {:2} = {}'.format(n, 4, n*4))
  print('{} * {:2} = {}'.format(n, 5, n*5))
  print('{} * {:2} = {}'.format(n, 6, n*6))
  print('{} * {:2} = {}'.format(n, 7, n*7))
  print('{} * {:2} = {}'.format(n, 8, n*8))
  print('{} * {:2} = {}'.format(n, 9, n*9))
  print('{} * {:2} = {}'.format(n, 10, n*10))
  print('_' * 12)



def desafio010():
  real = float(input('Quanto dinheiro você tem na carteira? R$'))
  dolar = real / 5.06
  euro = dolar / 5.74

  print('Com R${:.2f} você pode comprar US${:.2f} e também €{:.2f}'.format(real, dolar, euro))



def desafio011():
  larg = float(input('Largura da parede: '))
  alt = float(input('Altura da parede: '))
  área = larg * alt
  print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {área}m²')
  tinta = área / 2
  print(f'para pintar a parede, você precisará de {tinta}l de tinta')

def desafio012():
  preço = float(input('Qual é o preço do produto? R$'))
  novo = preço - (preço * 5 / 100)

  print('O produto que custava R${:.2f}, na promoção de 5% vai custa R${:.2f}'.format(preço, novo))



def desafio013():
  salário = float(input('Qual é o salário do funcionário R$'))
  novo = salário + (salário * 15 / 100)
  print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))



def desafio014():
  c = float(input('Informe a temperatura em °C: '))
  f = 9 * c / 5  + 32
  print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))



def desafio015():
  dias = int(input('Quantos dias alugados? '))
  km = float(input('Quantos km rodados? '))
  pago = (dias * 60) + (km * 0.15)
  print('O total a pagar é de R${:.2f}'.format(pago))



def desafio016():
  num = float(input('Digite um valor: '))
  print('O valor digitado foi de {} e sua porção inteira é {}'.format(num, int(num)))
 


def desafio017():
  co = float(input('Comprimento do cateto oposto: '))
  ca = float(input('comprimento do cateto adjacente: '))
  hi = hypot(co, ca)
  print(' A hipotenusa vai medir {:.2f}'.format(hi))



def desafio018():
  ângulo = float(input('Digite o ângulo que você deseja: '))
  seno = sin(radians(ângulo))
  print('O ângulo de {} tem SENO de {:.2f}'.format(ângulo, seno))
  cosseno = cos(radians(ângulo))
  print('O ângulo de {} tem COSSENO de {:.2f}'.format(ângulo, cosseno))
  tangente = tan(radians(ângulo))
  print('O ângulo de {} tem TANGENTE de {:.2f}'.format(ângulo, tangente))



def desafio019():
  n1 = input('Primeiro aluno: ')
  n2 = input('Segundo aluno: ')
  n3 = input('Terceiro aluno: ')
  n4 = input('Quarto aluno: ')
  lista = [n1, n2, n3, n4]
  escolhido = choice(lista)
  print(f'O aluno escolhido foi {escolhido}')



def desafio020():
  n1 = input('Primeiro aluno: ')
  n2 = input('Segundo aluno: ')
  n3 = input('Terceiro aluno: ')
  n4 = input('Quarto aluno: ')
  lista = [n1, n2, n3, n4]
  shuffle(lista)
  print('A ordem de apresentação será ')
  print(lista)



'''def desafio021():
  pygame.init()
  pygame.mixer.music.load("musica.mp3")
  pygame.mixer.music.play()
  pygame.event.wait()'''



def desafio022():
  nome = str(input('Digite seu nome completo: ')).strip()
  print('Analisando seu nome...')
  print('Seu nome em maiusculo é {}'.format(nome.upper()))
  print('Seu nome em minuscula é {}'.format(nome.lower()))
  print('Seu nome ao todo tem {}'.format(len(nome) - nome.count(' ')))
  separa = nome.split()
  print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))



def desafio023():
  num = int(input('Informe um numero: '))
  u = num // 1 % 10
  d = num // 10 % 10
  c = num // 100 % 10
  m = num // 1000 % 10
  print(f'Analisando o numero: {num}')
  print(f'Unidade {u}')
  print(f'Dezena {d}')
  print(f'Centena {c}')
  print(f'milhar {m}')



def desafio024():
  cid = str(input('Em que cidade você nasceu? ')).strip()
  print(cid[:5].upper() == 'SANTO')



def desafio025():
  nome = input('Qual seu nome completo? ').strip()
  print(f'Seu nome tem Silva? {"silva" in nome.lower()}')


def desafio026():
  frase = input('Digite uma frase:').upper().strip()
  print(f'A letra A apareceu {frase.count("A")} vezes na frase')
  print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')
  print(f'A ultima letra A apareceu na posição {frase.rfind("A")+1}')



def desafio027():
  n = str(input('Digite seu nome completo: ')).strip()
  nome = n.split()
  print('Muito prazer em te conhecer!')
  print(f'Seu primeiro nome é {nome[0]}')
  print(f'Seu último nome é {nome[len(nome)-1]}')



def desafio028():
  computador = randint(0, 5)
  print('-=-' * 20)
  print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')  
  print('-=-' * 20)
  jogador = int(input('Em que número eu pensei? '))
  print('PROCESSANDO...')
  sleep(3)
  if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
  else:
    print(f'EU GANHEI! Eu pensei no número {computador} e não no {jogador}')



def desafio029():
  velocidade = float(input('Qual é a velocidade atual do carro? '))
  if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é 80Km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R$ {multa}')
  else:
    print('Tenha um bom dia! Dirija com segurança ')



def desafio030():
  número = int(input('Me diga um número qualque: '))
  resultado = número % 2
  print(f'Resultado foi {resultado}')
  
  if resultado == 0:
    print(f'O número {número} é PAR')
  else:
    print(f'O número {número} é IMPAR')



def desafio031():
  distancia = float(input('Qual a distância da sua viagem? '))
  print(f'Você esta prestes uma viagem de {distancia}Km.')
  if distancia <= 200:
    preço = distancia * 0.50
  else:
    preço = distancia * 0.45
  print(f'E o preço da sua passagem será de R$ {preço}')



def desafio032():
  ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
  if ano == 0:
    ano = date.today().year
  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
  else:
    print(f'O ano {ano} NÃO é BISSEXTO')



def desafio033():
  a = int(input('Primeiro valor: '))
  b = int(input('Segundo valor: '))
  c = int(input('Terceiro valor: '))
  menor = a
  if b < a and b < c:
    menor = b
  if c < a and c < b:
    menor = c

  maior = a
  if b > a and b > c:
    maior = b
  if c > a and c > b:
    maior = c
  print(f'Menor valor digitado foi {menor}')
  print(f'O maior valor digitado foi {maior}')



def desafio034():
  salário = float(input('Qual é o salário do funcionário? R$ '))
  if salário <= 1250:
    novo = salário + (salário * 15 / 100)
  else:
    novo = salário + (salário * 10 / 100)
  print(f'Quem ganhava R${salário} passa a ganhar R$ {novo} agora.')



def desafio035():
  print('-=' * 20)
  print('Analisador de triângulos')
  print('-=' * 20)
  r1 = float(input('Primeiro segmento: '))
  r2 = float(input('Segundo segmento: '))
  r3 = float(input('Terceiro segmento: '))
  if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo! ')
  else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
  