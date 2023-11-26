###################################################
#
# POR: WALLYSON S. SOUZA, ROBERTO CARLOS e JONATAS N. FREITAS
# PROJETO DESENVOLVIDO COM: Qt Designer e PySide6
# V: 1.0.0
#
###################################################
from typing import Optional
from telas.ui_main import Ui_MainWindow
from database.database import DB_Gerentia
from importacoes import *


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

        ###########################################################################################
        # AÇÃO PARA OS BTS DE CONFIGURAÇÕES
        self.btn_cadUsuario.clicked.connect(self.cadastro_de_usuario)
        self.btn_removerFunci.clicked.connect(self.remover_usuario)
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
    
    ####################################################################################################
    # FUNÇÕES PARA OS PRODUTOS
    def limpar_area_cadastro(self):
        self.txt_nome.clear()
        self.txt_descricao.clear()
        self.txt_quantidade.clear()
        self.txt_pCompra.clear()
        self.txt_pVenda.clear()

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
            self.limpar_area_cadastro()
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

    ####################################################################################################

    ####################################################################################################
    # FUNÇÕES PARA OS FUNCIOONÁRIOS
    def limpa_lineEdit(self):
        self.txt_cUsuario.clear()
        self.txt_cSenha.clear()
        self.txt_cConfiSenha.clear()

    def cadastro_de_usuario(self):
        usuario = str(self.txt_cUsuario.text().strip())
        senha = str(self.txt_cSenha.text().strip())
        confirma_senha = str(self.txt_cConfiSenha.text().strip())
        
        self.limpa_lineEdit()

        if usuario == "" or senha == "" or confirma_senha == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro de cadastro!")
            msg.setText("Não foi possível cadastrar o usuário.\nPor favor, preencha todos os campos!")
            msg.exec()
            return -1
        
        if senha != confirma_senha:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Aviso!")
            msg.setText("As senhas não são iguais. Tente novamente!")
            msg.exec()
            return -1
        
        else:
            nome_funcionario, nome_ok = QInputDialog.getText(None, 'IDENTIFICAÇÃO DO FUNCIONÁRIO', 'Nome do funcionário:')
            if nome_ok:
                cargos = ["ADMINISTRADOR", "VENDEDOR", "ESTOQUE"]
                cargo, cargo_ok = QInputDialog.getItem(None, "CARGOS", "Qual será o cargo?", cargos, 0, False)
                
                if cargo_ok:
                    matricula = secrets.token_hex(5)
                    dados_funcionario = (matricula, nome_funcionario, cargo, usuario, senha)

                    db = DB_Gerentia()
                    db.conexao()
                    resposta = db.cadastrar_usuario(dados_funcionario)

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

                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle("Aviso!")
                    msg.setText("Não foi possível cadastrar o usuário.\nDados insuficientes!")
                    msg.exec()
                    return -1
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Aviso!")
                msg.setText("Não foi possível cadastrar o usuário.\nDados insuficientes, tente novamente!")
                msg.exec()
                    

    def remover_usuario(self):
        db = DB_Gerentia()
        db.conexao()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Remover Funcionário")
        msg.setText("O funcionário será excluído do sistema.")
        msg.setInformativeText("Tem certeza que deseja remove-lo?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        # ALTERAR TEXTO PADRÃO DOS BOTÕES
        msg.button(QMessageBox.StandardButton.Yes).setText("Sim")
        msg.button(QMessageBox.StandardButton.No).setText("Não")
        resposta = msg.exec()

        if resposta == QMessageBox.Yes:
            matricula = self.txt_matricula.text().strip()
            nome = self.txt_nomeFunci.text().strip()
            self.txt_matricula.clear()
            self.txt_nomeFunci.clear()
            resultado = db.remover_funcionario(matricula, nome)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Usuário")
            msg.setText(resultado)
            msg.exec()

        db.fechar_conexao()

    ####################################################################################################

            
if __name__ == "__main__":
    db = DB_Gerentia()
    db.conexao()
    db.criar_tabela()
    db.criar_tabela_funcionarios()
    db.adicionar_admin_padrao()
    db.fechar_conexao()

    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()