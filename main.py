from cgitb import text
from turtle import bgcolor
from function import gerar_qrcode
import tkinter as tk

"""
name = str(input('Digite o nome do usuário do ramal: '))
exten = str(input('Digite o número do ramal: '))
password = str(input('Digite a senha do ramal: '))
domain = str(input('Digite o IP/DDNS: '))
port = 5060
# correio de voz = str(input('Digite o Número Correo de voz: ')) 

gerar_qrcode(exten, password, domain, port)
"""

# Criando a interface Gráfica com TkInter.
janela = tk.Tk()

janela.title('QR Code - Prisma Telecom')

mensagem = tk.Label(text='Sistema Gerar QRCode Prisma Telecom', font='bold',fg='white', bg='black', width='50', height='1') # Fonte = Batman Forever
mensagem.pack()

name_texto = tk.Label(text='Digite o nome do usuário do ramal: ')
name_texto.pack()

name = tk.Entry()
name.pack()

# exten = tk.Label(text='Digite o nome do usuário do ramal: ')
# exten.pack()

# password = tk.Label(text='Digite o nome do usuário do ramal: ')
# password.pack()

# domain = tk.Label(text='Digite o nome do usuário do ramal: ')
# domain.pack()

# port = tk.Label(text='Digite o nome do usuário do ramal: ')
# port.pack()

janela.mainloop()