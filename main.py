from function import gerar_qrcode

#name = str(input('Digite o nome do usuário do ramal: '))
exten = str(input('Digite o número do ramal: '))
password = str(input('Digite a senha do ramal: '))
domain = str(input('Digite o IP/DDNS: '))
port = 5060
# correio de voz = str(input('Digite o Número Correo de voz: ')) 

gerar_qrcode(exten, password, domain, port)
