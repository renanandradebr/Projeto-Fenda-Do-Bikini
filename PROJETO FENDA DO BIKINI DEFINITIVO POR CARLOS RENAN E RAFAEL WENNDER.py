#Codigo de uma hamburgueria por Rafael Wennder e Carlos Renan - T03 
#==================================
import time

def imprimirCaracteres():
	print("====="*12)
 
def contagem():
	c = 0
	while (c < 5):
		print(c)
		time.sleep(1)
		c += 1
def imprimirMensagemDoCartão():
	print('inserir cartão')
	print('{:=^50}'.format("Aguarde um momento!"))
	time.sleep(2)
imprimirCaracteres()

Dr_Hamburgueiro= {'Hamburguer de siri': 12.99,
                'Thor Burguer': 16.99,
                'Monstro Burguer': 16.99,
                'Aquaman Burguer': 19.00,
                'El Locon': 22.00,
                'Água': 3.00,
                'GUARANÁ 1L': 7.00,
                'COCA COLA1L': 7.00,
                'COLA COLA LATA': 5.00,
                'PEPSI': 7.00,
                'SUCO DE MARACUJÁ': 5.00,
                'SUCO DE GRAVÍOLA': 4.50,
                }
print('{:=^60}'.format('Bem-Vindo ao Dr. Hamburgueiro'))
print('Cardápio:')

for produto, preco in Dr_Hamburgueiro.items():
	print(f"{produto}: R${preco:0.02f}")

Pedido = []
Valor = []

imprimirCaracteres()

while True:
 Cliente = input('Digite o que deseja: ')
 valor = Dr_Hamburgueiro[Cliente]
 print('O valor da(o)', Cliente, 'é: R$', valor)
 Pedido.append(Cliente)
 Valor.append(valor)
  
 Quantidade = int(input("Quantos? "))
 
 H = input('Deseja finalizar o pedido? ')
 H = H.upper()
 if H == 'SIM':
   break

preçoFinal=0
for valor in Valor:
  preçoFinal = ((preçoFinal+valor)*Quantidade)
  imprimirCaracteres()
print('O total do seu pedido é R$', preçoFinal)

imprimirCaracteres()

print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista/dinheiro
[ 2 ] à vista cartão/debito
[ 3 ] 2x no cartão de crédito
''')

opção = int(input('Qual é a opção? '))

if (opção == 1):
	imprimirCaracteres()
	dinheiro=float(input("Digite o dinheiro entregue: "))
	imprimirCaracteres()
	troco = dinheiro - preçoFinal
	if dinheiro < preçoFinal:
		print("Falta", preçoFinal - dinheiro, "pra completar seu lanche!")
		dinheiro2 = float(input("Digite o dinheiro entregue:"))
		imprimirCaracteres()
		troco2 = dinheiro2 + troco
		print("O seu troco é", troco2,". Obrigado pela preferencia!")
	else:
		print("O seu troco é", troco , ". Obrigado pela preferencia!")
	
elif (opção == 2):
  imprimirMensagemDoCartão()
  contagem()
  print('compra aprovada, Obrigado pela preferência, volte sempre!')

elif (opção == 3):
  total = preçoFinal
  parcela = preçoFinal / 2
  print('sua compra será parcelada em 2x')
  print('O valor da parcela será de: R$', parcela)
  imprimirCaracteres()
  cartaoParcela = input("Deseja continuar? Sim ou Não:")
  if(cartaoParcela == "Sim"){
  	imprimirMensagemDoCartão()
	contagem()
	print("Compra efetuada")
  	print("Obrigado pela Preferência, volte sempre!")
	}
  elif(cartaoParcela == "Não"):
  		print("Compra cancelada")
  		print("---"*12)
  		print('Sinto muito, tente novamente!')
  else:
  	print("Opção inválida!!! tente novamente")
  
else:
	print("Opção de pagamento inválida!")