import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import datetime
from datetime import date
from tela_inicial import Tela_inicial
from tela_cadastro import Tela_cadastro
from tela_saque import Tela_saque
from tela_extrato import Tela_extrato
from tela_depositar import Tela_depositar
from tela_transacoes import Tela_transacoes
from tela_transferencia import Tela_transferencia
from login_efetuado import Login_efetuado

import socket


ip = '192.168.1.4'
port = 1235
#name = input('Qual seu nome?')
addr = ((ip, port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
#client_socket.send(name.encode())
while True:

    

    class Ui_Main(QtWidgets.QWidget):
        def setupUi(self, Main):
            Main.setObjectName('Main')
            Main.resize(640, 480)

            self.QtStack = QtWidgets.QStackedLayout()

            self.stack0 = QtWidgets.QMainWindow()
            self.stack1 = QtWidgets.QMainWindow()
            self.stack2 = QtWidgets.QMainWindow()
            self.stack3 = QtWidgets.QMainWindow()
            self.stack4 = QtWidgets.QMainWindow()
            self.stack5 = QtWidgets.QMainWindow()
            self.stack6 = QtWidgets.QMainWindow()
            self.stack7 = QtWidgets.QMainWindow()

            self.tela_inicial = Tela_inicial()
            self.tela_inicial.setupUi(self.stack0)

            self.tela_cadastro = Tela_cadastro()
            self.tela_cadastro.setupUi(self.stack1)

            self.tela_saque = Tela_saque()
            self.tela_saque.setupUi(self.stack2)

            self.tela_extrato = Tela_extrato()
            self.tela_extrato.setupUi(self.stack3)

            self.tela_depositar = Tela_depositar()
            self.tela_depositar.setupUi(self.stack4)

            self.tela_transacoes = Tela_transacoes()
            self.tela_transacoes.setupUi(self.stack5)

            self.tela_transferencia = Tela_transferencia()
            self.tela_transferencia.setupUi(self.stack6)

            self.login_efetuado = Login_efetuado()
            self.login_efetuado.setupUi(self.stack7)

            self.QtStack.addWidget(self.stack0)
            self.QtStack.addWidget(self.stack1)
            self.QtStack.addWidget(self.stack2)
            self.QtStack.addWidget(self.stack3)
            self.QtStack.addWidget(self.stack4)
            self.QtStack.addWidget(self.stack5)
            self.QtStack.addWidget(self.stack6)
            self.QtStack.addWidget(self.stack7)


    class Main(QMainWindow, Ui_Main):
        def __init__(self):
            super(Main, self).__init__(None)
            self.setupUi(self)

            

            self.tela_inicial.pushButton_3.clicked.connect(self.abrir_tela_login)
            self.tela_inicial.pushButton_2.clicked.connect(
                self.abrir_tela_cadastro)
            self.tela_inicial.pushButton_4.clicked.connect(self.botaoSair)

            self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastrar)
            self.tela_cadastro.pushButton_2.clicked.connect(self.botaoVoltar)

            self.login_efetuado.pushButton_2.clicked.connect(self.abrir_tela_saque)
            self.login_efetuado.pushButton_3.clicked.connect(
                self.abrir_tela_depositar)

            self.login_efetuado.pushButton_4.clicked.connect(
                self.abrir_tela_extrato)
            self.login_efetuado.pushButton_5.clicked.connect(
                self.abrir_tela_transacoes)
            self.login_efetuado.pushButton_6.clicked.connect(
                self.abrir_tela_transferencia)
            self.login_efetuado.pushButton_7.clicked.connect(self.botaoVoltar)

            self.tela_saque.pushButton.clicked.connect(self.botaoSaque)
            self.tela_saque.pushButton_2.clicked.connect(self.botaoVoltarLogin)

            self.tela_extrato.pushButton.clicked.connect(self.botaoExtrato)
            self.tela_extrato.pushButton_2.clicked.connect(self.botaoVoltarLogin)

            self.tela_depositar.pushButton.clicked.connect(self.botaoDepositar)
            self.tela_depositar.pushButton_2.clicked.connect(self.botaoVoltarLogin)

            self.tela_transferencia.pushButton.clicked.connect(
                self.botaoTransferencia)
            self.tela_transferencia.pushButton_2.clicked.connect(
                self.botaoVoltarLogin)

            self.tela_transacoes.pushButton.clicked.connect(self.botaoTransacoes)
            self.tela_transacoes.pushButton_2.clicked.connect(
                self.botaoVoltarLogin)

        def botaoCadastrar(self):
            """
            Lida com a entrada do usu??rio na tela "Cadastro" de um aplicativo banc??rio.
    
    Obt??m a entrada do usu??rio para nome, CPF, endere??o, data de nascimento, senha, limite de cr??dito e saldo e envia
    esses valores para o servidor realizar o cadastro. Se algum desses valores estiver faltando, uma mensagem ser??
    exibido ao usu??rio. Caso o CPF informado j?? exista, uma mensagem ser?? exibida ao usu??rio.
    
    Argumentos:
        Nenhum
    
    Retorna:
        Nenhum
    """

            nome = self.tela_cadastro.lineEdit.text()
            cpf = self.tela_cadastro.lineEdit_2.text()
            endereco = self.tela_cadastro.lineEdit_3.text()
            nascimento = self.tela_cadastro.lineEdit_4.text()
            senha = self.tela_cadastro.lineEdit_5.text()
            limite = self.tela_cadastro.lineEdit_6.text()
            saldo = self.tela_cadastro.lineEdit_7.text()

            # Verifica se todos os campos est??o preenchidos
            if not (nome == '' or endereco == '' or cpf == '' or nascimento == '' or senha == '' or limite == '' or saldo == ''):
                mensagem = 'cadastrar'
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(nome)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(cpf)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(endereco)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(nascimento)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(senha)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(limite)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(saldo)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                certo = client_socket.recv(1024).decode()

                # Se o registro foi bem-sucedido, exibe uma mensagem para o usu??rio e limpa os campos de entrada
                if certo == 'False':
                    QMessageBox.information(None, 'POOII', 'Cadastro realizado com sucesso')
                    self.tela_cadastro.lineEdit.setText('')
                    self.tela_cadastro.lineEdit_2.setText('')
                    self.tela_cadastro.lineEdit_3.setText('')
                    self.tela_cadastro.lineEdit_4.setText('')
                    self.tela_cadastro.lineEdit_5.setText('')
                    self.tela_cadastro.lineEdit_6.setText('')
                    self.tela_cadastro.lineEdit_7.setText('')
                    self.QtStack.setCurrentIndex(0)
                # If the CPF entered already exists, display a message to the user and clear the input fields
                else:
                    QMessageBox.information(
                        None, 'POOII', 'O cpf informado j?? est?? cadastrado')
                    self.tela_cadastro.lineEdit.setText('')
                    self.tela_cadastro.lineEdit_2.setText('')
                    self.tela_cadastro.lineEdit_3.setText('')
                    self.tela_cadastro.lineEdit_4.setText('')
                    self.tela_cadastro.lineEdit_5.setText('')
                    self.tela_cadastro.lineEdit_6.setText('')
                    self.tela_cadastro.lineEdit_7.setText('')
            else:
                QMessageBox.information(
                    None, 'POOII', 'Todos os valores devem estar preenchidos')

        def botaoExtrato(self):


            """Recupera o CPF do usu??rio em um campo de entrada, cria uma mensagem para solicitar o extrato da conta desse usu??rio,
    envia a mensagem para o servidor e recebe uma resposta do servidor. A resposta cont??m o extrato da conta
    na forma de uma string dividida em uma lista de itens. O primeiro item da lista ?? o saldo da conta, que ??
    exibido em um campo de entrada na GUI. O segundo item ?? o CPF do usu??rio, que tamb??m ?? exibido na GUI. O terceiro
    item ?? o pr??prio extrato da conta, que ?? exibido em uma janela separada.
    """
            cpf = self.tela_inicial.lineEdit.text()
            mensagem = str('extrato')
            print ('A mensagem foi enviada com sucesso')
            client_socket.send(mensagem.encode())
            print(client_socket.recv(1024).decode())

            mensagem = str(cpf)
            print ('A mensagem foi enviada com sucesso')
            client_socket.send(mensagem.encode())
            certo = client_socket.recv(1024).decode()

            lista = certo.split()

            self.tela_extrato.lineEdit_3.setText(lista[0])
            self.tela_extrato.lineEdit_4.setText(cpf)
            self.tela_extrato.lineEdit_5.setText(lista[1])


    
        def botaoSaque(self):

            valor = self.tela_saque.lineEdit.text()

            cpf = self.tela_inicial.lineEdit.text()
            if valor == '':    
                QMessageBox.information(None, 'POOII', 'Preencha o campo')
            else:
                mensagem = 'sacar'
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(valor)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(cpf)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                certo = client_socket.recv(1024).decode()
            
                if certo == 'True':
                    QMessageBox.information(None, 'POOII', 'Saque realizado')
                elif certo == 'False':
                    QMessageBox.information(None, 'POOII', 'Nao foi possivel realizar o saque')
                else:
                    QMessageBox.information(None, 'POOII', 'Cpf nao encontrado')



        def botaoTransacoes(self):
            """
                Esse m??todo ?? respons??vel por enviar uma mensagem para um servidor remoto via socket de rede para solicitar as transa????es
                associadas a um CPF fornecido pelo usu??rio. A mensagem ?? enviada ao servidor usando a codifica????o UTF-8.
                
                Par??metros:
                -----------
                Nenhum
                
                Retorno:
                --------
                Nenhum
            """
            # L?? o CPF inserido na caixa de texto da tela inicial
            cpf = self.tela_inicial.lineEdit.text()
            # Limpa a lista de transa????es na tela de transa????es
            self.tela_transacoes.listWidget.clear()
            
            # Envia uma mensagem "transacoes" ao servidor e imprime uma mensagem de sucesso no console
            mensagem = str('transacoes')
            print ('A mensagem foi enviada com sucesso')
            client_socket.send(mensagem.encode())
            print(client_socket.recv(1024).decode())
            # Envia o CPF para o servidor e aguarda uma resposta
            mensagem = str(cpf)
            print ('A mensagem foi enviada com sucesso')
            client_socket.send(mensagem.encode())
            certo = client_socket.recv(1024).decode()

            # Divide a resposta em uma lista de transa????es separadas por v??rgulas
            lista = certo.split(',')

            for c in lista:
                self.tela_transacoes.listWidget.addItem(c)
            

            
        
        def botaoDepositar(self):
            """
                Esse m??todo ?? respons??vel por enviar uma mensagem para um servidor remoto via socket de rede para fazer um dep??sito em uma
                conta associada a um CPF fornecido pelo usu??rio. A mensagem ?? enviada ao servidor usando a codifica????o UTF-8.
                
                Par??metros:
                -----------
                Nenhum
                
                Retorno:
                --------
                Nenhum
            """

            # L?? o valor do dep??sito inserido na caixa de texto da tela de dep??sito
            valor = self.tela_depositar.lineEdit.text()
            # L?? o CPF inserido na caixa de texto da tela inicial
            cpf = self.tela_inicial.lineEdit.text()
            # Verifica se o valor do dep??sito foi fornecido pelo usu??rio
            if valor == '':
                # Exibe uma mensagem informando que todos os campos precisam ser preenchidos
                QMessageBox.information(None, 'POOII', 'Preencha todos')
            else:
                mensagem = 'depositar'
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())
                
                # Envia o valor do dep??sito para o servidor e aguarda uma resposta
                mensagem = str(valor)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                # Envia o CPF para o servidor e aguarda uma resposta
                mensagem = str(cpf)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                certo = client_socket.recv(1024).decode()

                # Verifica se o dep??sito foi realizado com sucesso e exibe uma mensagem de confirma????o 
                if certo == 'True':
                    QMessageBox.information(None, 'POOII', 'Deposito realizado')



        def botaoTransferencia(self):
            """ Esse m??todo obt??m tr??s informa????es digitadas pelo usu??rio: o valor da transfer??ncia, 
            o CPF do usu??rio que est?? realizando a transfer??ncia e o CPF do destinat??rio. """
            cpf = self.tela_inicial.lineEdit.text()
            valor = self.tela_transferencia.lineEdit.text()
            destino = self.tela_transferencia.lineEdit_2.text()
            
            """ O m??todo primeiro verifica se o campo de valor da transfer??ncia foi preenchido.
            Se n??o foi preenchido, uma mensagem de aviso ?? exibida. Se o campo foi preenchido,
            o m??todo envia uma mensagem ao servidor indicando que uma transfer??ncia ser?? realizada. 
            Em seguida, a mensagem de valor da transfer??ncia ?? enviada, 
            seguida pela mensagem com o CPF do destinat??rio 
            e, finalmente, a mensagem com o CPF do usu??rio que est?? realizando a transfer??ncia."""

            if valor == '':
                QMessageBox.information(None, 'POOII', 'Preencha todos')
            else:
                mensagem = 'transferir'
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(valor)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(destino)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(cpf)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                certo = client_socket.recv(1024).decode()

                #Se o servidor responder com 'None', significa que o CPF do destinat??rio ?? inv??lido.
                if certo == 'None':
                    QMessageBox.information(None, 'POOII', 'Destino n??o encontrado')
                #Se o servidor responder com 'False', significa que a transfer??ncia n??o foi poss??vel
                elif certo == 'False':
                    QMessageBox.information(None, 'POOII', 'N??o foi possivel concluir transfer??ncia')
                #Caso contr??rio, o servidor respondeu com sucesso e a transfer??ncia foi conclu??da com ??xito.
                else:
                    QMessageBox.information(None, 'POOII', 'Transfer??ncia concluida')


        
        def botaoSair(self):
            """ Este c??digo define um m??todo chamado botaoSair que ?? usado como um manipulador de eventos para um clique de bot??o. Ao clicar no bot??o, 
        o m??todo envia uma mensagem ao servidor para encerrar a conex??o e fecha o aplicativo usando sys.exit()."""
            mensagem = 'bye'
            print ('A mensagem foi enviada com sucesso')
            client_socket.send(mensagem.encode())
            sys.exit()
            
                

        def botaoVoltarLogin(self):
            self.QtStack.setCurrentIndex(7)

        def botaoVoltar(self):
            self.tela_inicial.lineEdit.setText('')
            self.tela_inicial.lineEdit_2.setText('')
            self.tela_extrato.lineEdit_3.setText('')
            self.tela_extrato.lineEdit_4.setText('')
            self.tela_extrato.lineEdit_5.setText('')
            self.QtStack.setCurrentIndex(0)

        def abrir_tela_cadastro(self):
            self.QtStack.setCurrentIndex(1)

        def abrir_tela_saque(self):
            self.QtStack.setCurrentIndex(2)

        def abrir_tela_extrato(self):
            self.tela_extrato.lineEdit_3.setText('')
            self.tela_extrato.lineEdit_4.setText('')
            self.tela_extrato.lineEdit_5.setText('')
            self.QtStack.setCurrentIndex(3)

        def abrir_tela_depositar(self):
            self.QtStack.setCurrentIndex(4)

        def abrir_tela_transacoes(self):
            self.tela_transacoes.listWidget.clear()
            self.QtStack.setCurrentIndex(5)

        def abrir_tela_transferencia(self):
            self.QtStack.setCurrentIndex(6)

        def abrir_tela_login(self):
            """ M??todo que ?? chamado quando o bot??o "Entrar" na tela de login ?? clicado.
    Verifica se os campos CPF e senha foram preenchidos e, em seguida, envia uma mensagem ao servidor
    com a inten????o de entrar na conta do usu??rio. Se o servidor responder com 'True', a aplica????o exibe a
    tela de opera????es banc??rias, caso contr??rio, uma mensagem de erro ?? exibida.
    """
            
            
            cpf = self.tela_inicial.lineEdit.text()
            senha = self.tela_inicial.lineEdit_2.text()

            # Verifica se os campos CPF e senha foram preenchidos  
            if cpf == '' or senha == '':
                QMessageBox.information(None, 'POOII', 'Preencha todos os campos')
            else:
                # Envia uma mensagem ao servidor com a inten????o de entrar na conta do usu??rio
                mensagem = 'entrar'
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(cpf)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                print(client_socket.recv(1024).decode())

                mensagem = str(senha)
                print ('A mensagem foi enviada com sucesso')
                client_socket.send(mensagem.encode())
                # Verifica a resposta do servidor
                certo = client_socket.recv(1024).decode()
                

                
                # Exibe a tela de opera????es banc??rias se a resposta for 'True', sen??o exibe uma mensagem de erro
                if certo == 'True':
                    self.QtStack.setCurrentIndex(7)
    
                else:
                    QMessageBox.information(None, 'POOII', 'ALGO DEU ERRADO =(')

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        show_main = Main()
        sys.exit(app.exec_())
