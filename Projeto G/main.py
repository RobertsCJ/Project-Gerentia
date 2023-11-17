###################################################
#
# POR: WALLYSON S. SOUZA, ROBERTO CARLOS e JONATAS N. FREITAS
# PROJETO DESENVOLVIDO COM: Qt Designer e PySide6
# V: 1.0.0
#
###################################################
from typing import Optional
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
from ui_main import Ui_MainWindow
from database import DB_Gerentia
import uuid
from datetime import *
import sqlite3
import pandas


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gerentia - Sistema de Gerenciamento")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        ###########################################################################################
        # BTN MENU
        self.btn_menu.clicked.connect(self.abrir_fechar_menu)
        ###########################################################################################

        ###########################################################################################
        # NAVEGAÇÃO ENTRE AS PÁGINAS
        self.btn_home.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_home))
        self.btn_estoque.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_estoque))
        self.btn_contatos.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_contatos))
        self.btn_configuracoes.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_configuracoes))
        self.btn_sobre.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_sobre))
        ###########################################################################################

        ###########################################################################################
        # AÇÃO PARA OS BTS DO ESTOQUE
        self.btn_cadastrar.clicked.connect(self.adicinar_produtos)
        self.btn_alterar.clicked.connect(self.atualizar_produto)
        self.btn_excluir.clicked.connect(self.excluir_produto)
        self.btn_relatorio.clicked.connect(self.gerar_relatorio)
        self.btn_pesquisar.clicked.connect(self.pesquisar)
        ###########################################################################################

        ###########################################################################################
        # VISUALIZAÇÃO DE PRODUTOS NA TABELA
        self.mostrar_produtos()
        ###########################################################################################

        # MOSTRANDO A JANELA
        self.show()

    def abrir_fechar_menu(self):
        # TAMANHO INICIAL DO MENU
        largura = self.frame_menu_lateral.width()
        
        if largura == 0:
            novoTamanho = 240
        else:
            novoTamanho = 0

        # ANIMAÇÃO DO MENU
        self.animacao = QPropertyAnimation(self.frame_menu_lateral, b"maximumWidth")
        self.animacao.setDuration(400)
        self.animacao.setStartValue(largura)
        self.animacao.setEndValue(novoTamanho)
        # TIPO DE ANIMAÇÃO
        self.animacao.setEasingCurve(QEasingCurve.InOutQuart)
        # INICIANDO ANIMAÇÃO
        self.animacao.start()
    
    def adicinar_produtos(self):
        try:
            cod = str(uuid.uuid4())
            nome = str(self.txt_nome.text().strip().upper())
            descricao = str(self.txt_descricao.text().strip().upper())
            quantidade = int(self.txt_quantidade.text())
            preco_compra = float(self.txt_pCompra.text().replace(",", "."))
            preco_venda = float(self.txt_pVenda.text().replace(",", "."))
            data_atual = date.today().strftime('%d/%m/%Y')
            hora_atual = datetime.now().strftime('%H:%M:%S')
            dadosProduto = (cod, nome, descricao, quantidade, preco_compra, preco_venda, data_atual, hora_atual)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
            msg.exec()
        
        db = DB_Gerentia()
        db.conexao()

        # CADASTRAR NO BANCO DE DADODS
        resposta = db.cadastrar_produto(dadosProduto)

        if resposta == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Cadastro Realizado com sucesso")
            msg.exec()
            db.fechar_conexao()
            self.mostrar_produtos()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
            msg.exec()
            db.fechar_conexao()
            return

    def mostrar_produtos(self):
        db = DB_Gerentia()
        db.conexao()

        visualizacao = db.mostrar_produtos()

        self.tb_estoque.clearContents()
        self.tb_estoque.setRowCount(len(visualizacao))

        for linhas, infos in enumerate(visualizacao):
            for colunas, dados in enumerate(infos):
                self.tb_estoque.setItem(linhas, colunas, QTableWidgetItem(str(dados)))
        db.fechar_conexao()

    def atualizar_produto(self):
        dados = []
        dados_att = []

        for linhas in range(self.tb_estoque.rowCount()):
            for colunas in range(self.tb_estoque.columnCount()):
                dados.append(self.tb_estoque.item(linhas, colunas).text())
            dados_att.append(dados)
            dados = []

        # ATUALIZANDO DADOS
        db = DB_Gerentia()
        db.conexao()

        for produto in dados_att:
            db.alterar_produto(tuple(produto))

        db.fechar_conexao()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de dados")
        msg.setText("Os dados foram atualizados com sucesso!")
        msg.exec()

        self.tb_estoque.reset()
        self.mostrar_produtos()

    def excluir_produto(self):
        db = DB_Gerentia()
        db.conexao()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Excluir Produto")
        msg.setText("O produto será excluído do sistema.")
        msg.setInformativeText("Tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        # ALTERAR TEXTO PADRÃO DOS BOTÕES
        msg.button(QMessageBox.StandardButton.Yes).setText("Sim")
        msg.button(QMessageBox.StandardButton.No).setText("Não")
        resposta = msg.exec()

        if resposta == QMessageBox.Yes:
            cod_barras = self.tb_estoque.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.excluir_estoque(cod_barras)
            self.mostrar_produtos()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Estoque")
            msg.setText(resultado)
            msg.exec()

        db.fechar_conexao()

    def gerar_relatorio(self):
        data_atual = date.today().strftime('%d-%m-%Y')
        hora_atual = datetime.now().strftime('%H-%M-%S')

        conn = sqlite3.connect("gerentia.db")
        estoque = pandas.read_sql_query("""SELECT * FROM estoque""", conn)

        estoque.to_excel(excel_writer=f"Relatório do estoque do dia {data_atual} às {hora_atual}.xlsx", sheet_name="Estoque", index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatório")
        msg.setText("O relatório foi gerado com sucesso!")
        msg.exec()

    def pesquisar(self):
        pesquisa = self.txt_pesquisa.text().upper().strip()
        
        db = DB_Gerentia()
        db.conexao()
        produtos = db.mostrar_produto_especifico(pesquisa)

        if len(produtos) != 0:
            # LIMPAR A TELA DA TABELA PESQUISAR
            self.tb_pesquisa.clearContents()

            # DEFINIR O NÚMERO DE LINHAS NA TABELA PARA CORRESPONDER AO NÚMERO DE PRODUTOS
            self.tb_pesquisa.setRowCount(len(produtos))

            # PREENCHER A TABELA COM OS DADOS DOS PRODUTOS
            for linhas, infos in enumerate(produtos):
                for colunas, dados in enumerate(infos):
                    self.tb_pesquisa.setItem(linhas, colunas, QTableWidgetItem(str(dados)))

            db.fechar_conexao()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Pesquisa")
            msg.setText("O produto informado, não foi localizado!")
            msg.exec()


            
if __name__ == "__main__":
    db = DB_Gerentia()
    db.conexao()
    db.criar_tabela()
    db.fechar_conexao()

    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()