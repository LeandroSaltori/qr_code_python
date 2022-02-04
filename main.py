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

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text='Sistema Gerar QRCode Prisma Telecom', font='bold',fg='white', bg='black', width='35', height='1') # Fonte = Batman Forever
mensagem.grid(row=0, column=0, columnspan=2, sticky='NSEW')

name_texto = tk.Label(text='Digite o nome do usuário do ramal: ')
name_texto.grid(row=1, column=0)

name = tk.Entry()
name.grid(row=1, column=1)

# exten = tk.Label(text='Digite o nome do usuário do ramal: ')
# exten.pack()

# password = tk.Label(text='Digite o nome do usuário do ramal: ')
# password.pack()

# domain = tk.Label(text='Digite o nome do usuário do ramal: ')
# domain.pack()

# port = tk.Label(text='Digite o nome do usuário do ramal: ')
# port.pack()

janela.mainloop()