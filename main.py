from function import qrcode

#name = str(input('Digite o nome do usuário do ramal: '))
exten = str(input('Digite o número do ramal: '))
password = str(input('Digite a senha do ramal: '))
domain = str(input('Digite o IP/DDNS: '))
#port = 5060
# correio de voz = 

codigo = qrcode()
print(codigo)