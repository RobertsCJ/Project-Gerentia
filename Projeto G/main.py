######################################################################
#
# POR: WALLYSON S. SOUZA, ROBERTO CARLOS e JONATAS N. FREITAS
# PROJETO DESENVOLVIDO COM: Qt Designer e PySide6
# V: 1.0.0
#
#####################################################################

import requests
from dotenv import load_dotenv
from os import getenv
from telas.ui_main import Ui_MainWindow
from telas.ui_login import Ui_Form
from database.database import DB_Gerentia
from importacoes import *

load_dotenv()


class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        """
        Template visual da construção da tela de login
        :returns: nothing
        """
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gerentia - Login do sistema")

        self.btn_login.clicked.connect(self.abrir_sistema)

        self.tentativas = 0

    def abrir_sistema(self):
        """
        Função que realiza a verificação lógica de login, captura da entrada padrão do usuário o nome de usuário e senha, se os dados estiverem correto, leva o usuário a tela principal, caso contrário, após três tentativas, o sistema se encerra
        :return: nothing
        """
        db = DB_Gerentia()
        db.conexao()
        user = str(self.txt_nomeUser.text().strip())
        senha = str(self.txt_senhaUser.text().strip())

        self.txt_nomeUser.clear()
        self.txt_senhaUser.clear()

        resultado = db.verificar_login(user, senha)

        if resultado == "Usuário validado!":
            self.w = MainWindow()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao logar")
                msg.setText(
                    f"Usuário ou senha inválidos!\n\nTentativa: {self.tentativas+1} de 3.")
                msg.exec()
                self.tentativas += 1

            if self.tentativas == 3:
                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """Template visual da tela principal"""
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
        self.btn_home.clicked.connect(
            lambda: self.paginas.setCurrentWidget(self.pg_home))
        self.btn_estoque.clicked.connect(
            lambda: self.paginas.setCurrentWidget(self.pg_estoque))
        self.btn_contatos.clicked.connect(
            lambda: self.paginas.setCurrentWidget(self.pg_contatos))
        self.btn_configuracoes.clicked.connect(
            lambda: self.paginas.setCurrentWidget(self.pg_configuracoes))
        self.btn_sobre.clicked.connect(
            lambda: self.paginas.setCurrentWidget(self.pg_sobre))
        ###########################################################################################

        ###########################################################################################
        # AÇÃO PARA OS BTS DO ESTOQUE
        self.btn_cadastrar.clicked.connect(self.adicinar_produtos)
        self.btn_alterar.clicked.connect(self.atualizar_produto)
        self.btn_excluir.clicked.connect(self.excluir_produto)
        self.btn_relatorio.clicked.connect(self.gerar_relatorio)
        self.btn_pesquisar.clicked.connect(self.pesquisar)
        self.btn_sincronizar.clicked.connect(self.sincronizar_manualmente)
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
        """Função para realizar expansão da barra lateral"""
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
    # FUNÇÕES PARA REQUISIÇÕES COM A API
        
    def sincronizar_estoque_servidor(self, req):
        """
        Realiza a requisição dos arquivos do projeto estoque, retorna 1 se for bem sucedido, ou retorna um log em forma de objeto em caso de erro.
        :req: dict = requisição da API
        :returns: int | obj 
        """
        try:
            api_host = getenv("API_HOST")
            res = requests.post(f'{api_host}/api/stock/sinc', json=req)
        except requests.exceptions.ConnectionError as err:
            return err
        else:
            if res.status_code == 200:
                # Requisição feita com sucesso
                return 1
            
            # Requisição com erros
            return res.json()

    ####################################################################################################
    # FUNÇÕES PARA OS PRODUTOS
    

    def limpar_area_cadastro(self):
        """
        Limpa todos os campos de texto do produto.
        :return: none
        """
        self.txt_nome.clear()
        self.txt_descricao.clear()
        self.txt_quantidade.clear()
        self.txt_pCompra.clear()
        self.txt_pVenda.clear()

    def adicinar_produtos(self):
        """
        
        :returns: none
        """
        try:
            cod = str(uuid.uuid4())
            nome = str(self.txt_nome.text().strip().upper())
            descricao = str(self.txt_descricao.text().strip().upper())
            quantidade = int(self.txt_quantidade.text())
            preco_compra = float(self.txt_pCompra.text().replace(",", "."))
            preco_venda = float(self.txt_pVenda.text().replace(",", "."))
            data_atual = date.today().strftime('%d/%m/%Y')
            hora_atual = datetime.now().strftime('%H:%M:%S')
            dadosProduto = (cod, nome, descricao, quantidade,
                            preco_compra, preco_venda, data_atual, hora_atual, 0, 0)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(
                "Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
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
            
            # Tentativa de sinconizar com a API
            
            request = {"cod": cod, "nome": nome, "descricao": descricao, "quantidade": quantidade, "preco_compra": preco_compra, "preco_venda": preco_venda, "data_atual": data_atual, "hora_atual": hora_atual, "status": 0, "sincronizado": 0}

            resp = self.sincronizar_estoque_sevidor(request)
            if type(resp) is int and resp == 1:
                db.atualizar_sincronizado(cod)
            elif type(resp) is requests.exceptions.ConnectionError:
                print(resp.args[0])
            else:
                for key, value in resp.items():
                    print(f'{key} = {value}')
                
            # fechar a conexão com o database

            db.fechar_conexao()
            self.mostrar_produtos()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(resposta.args[0])
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
                self.tb_estoque.setItem(
                    linhas, colunas, QTableWidgetItem(str(dados)))
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
            try:
                db.alterar_produto(tuple(produto))
            except Exception as err:
                print(f'ERROR DB: {err}')
            else:
                # Tentativa de sinconizar com a API
                request = {"cod": produto[0], "nome": produto[1], "descricao": produto[2], "quantidade": produto[3], "preco_compra": produto[4], "preco_venda": produto[5], "data_atual": produto[6], "hora_atual": produto[7], "status": 1, "sincronizado": 0}

                resp = self.sincronizar_estoque_sevidor(request)
                if type(resp) is int and resp == 1:
                    db.atualizar_sincronizado(cod)
                elif type(resp) is requests.exceptions.ConnectionError:
                    print(resp.args[0])
                else:
                    for key, value in resp.items():
                        print(f'{key} = {value}')

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
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        # ALTERAR TEXTO PADRÃO DOS BOTÕES
        msg.button(QMessageBox.StandardButton.Yes).setText("Sim")
        msg.button(QMessageBox.StandardButton.No).setText("Não")
        resposta = msg.exec()

        if resposta == QMessageBox.Yes:
            cod_barras = self.tb_estoque.selectionModel().currentIndex().siblingAtColumn(0).data()
            try:
                resultado = db.excluir_estoque_pelo_status(cod_barras)
            except Exception as err:
                print(f'ERROR DB: {err}')
            else:
                request = {"cod": cod_barras, "status": 2, "sincronizado": 0}
                resp = self.sincronizar_estoque_sevidor(request)
                if type(resp) is int and resp == 1:
                    db.atualizar_sincronizado(cod_barras)
                elif type(resp) is requests.exceptions.ConnectionError:
                    print(resp.args[0])
                else:
                    for key, value in resp.items():
                        print(f'{key} = {value}')

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
        estoque = pandas.read_sql_query("""SELECT * FROM tb_estoque WHERE status != 2""", conn)

        estoque.to_excel(excel_writer=f"relatorios/Relatório do estoque do dia {data_atual} às {hora_atual}.xlsx", sheet_name="Estoque", index=False)

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
                    self.tb_pesquisa.setItem(
                        linhas, colunas, QTableWidgetItem(str(dados)))

            db.fechar_conexao()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Pesquisa")
            msg.setText("O produto informado, não foi localizado!")
            msg.exec()

    def verificar_conexão_api(self):
        try:
            api_host = getenv("API_HOST")
            requests.get(f'{api_host}/')
        except requests.exceptions.ConnectionError:
            return False
        else:
            return True
            
    def montar_objeto_estoque(self, dados):
        estoques = list()
        for data in dados:
            estoque = dict()
            estoque['cod'] = data[0]
            estoque['nome'] = data[1]
            estoque['descricao'] = data[2]
            estoque['quantidade'] = data[3]
            estoque['preco_compra'] = data[4]
            estoque['preco_venda'] = data[5]
            estoque['data_atual'] = data[6]
            estoque['hora_atual'] = data[7]
            estoque['status'] = data[8]
            estoque['sincronizado'] = data[9]
            estoques.append(estoque)
        
        return estoques
        

    def sincronizar_manualmente(self):
        db = DB_Gerentia()
        db.conexao()
        
        requisição_bem_sucessida = self.verificar_conexão_api()

        if requisição_bem_sucessida:
            dados_local_estoque = db.mostrar_produtos()
            estoques = self.montar_objeto_estoque(dados_local_estoque)
        
            for estoque in estoques:
                if estoque['sincronizado'] == 0:
                    request = {"cod": estoque["cod"], "nome": estoque["nome"], "descricao": estoque["descricao"], "quantidade": estoque["quantidade"], "preco_compra": estoque["preco_compra"], "preco_venda": estoque["preco_venda"], "data_atual": estoque["data_atual"], "hora_atual": estoque["hora_atual"], "status": estoque["status"], "sincronizado": estoque["sincronizado"]}

                    resp = self.sincronizar_estoque_sevidor(request)
                    if type(resp) is int and resp == 1:
                        db.atualizar_sincronizado(request['cod'])
                    elif type(resp) is requests.exceptions.ConnectionError:
                        requisição_bem_sucessida = False
                        print(resp.args[0])
                    else:
                        requisição_bem_sucessida = False
                        for key, value in resp.items():
                            print(f'{key} = {value}')
                
        if requisição_bem_sucessida:               
            dados_removidos_local_estoque = db.mostrar_produtos_removidos()
            estoques = self.montar_objeto_estoque(dados_removidos_local_estoque)
            
            for estoque in estoques:
                request = {"cod": estoque["cod"], "nome": estoque["nome"], "descricao": estoque["descricao"], "quantidade": estoque["quantidade"], "preco_compra": estoque["preco_compra"], "preco_venda": estoque["preco_venda"], "data_atual": estoque["data_atual"], "hora_atual": estoque["hora_atual"], "status": estoque["status"], "sincronizado": 0}

                resp = self.sincronizar_estoque_sevidor(request)
                if type(resp) is int and resp == 1:
                    db.excluir_estoque_permanentemente(request['cod'])
                elif type(resp) is requests.exceptions.ConnectionError:
                    requisição_bem_sucessida = False
                    print(resp.args[0])
                else:
                    requisição_bem_sucessida = False
                    for key, value in resp.items():
                        print(f'{key} = {value}')
                

        if requisição_bem_sucessida:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Sincronização")
            msg.setText("A sincronização com o servidor foi feita com sucesso!")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Não foi possível sincronizar agora, tente novamente mais tarde!")
            msg.exec()
    
        db.fechar_conexao()
  
        

    ####################################################################################################

    ####################################################################################################
    # FUNÇÕES PARA OS FUNCIONÁRIOS
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
            msg.setText(
                "Não foi possível cadastrar o usuário.\nPor favor, preencha todos os campos!")
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
            nome_funcionario, nome_ok = QInputDialog.getText(
                None, 'IDENTIFICAÇÃO DO FUNCIONÁRIO', 'Nome do funcionário:')
            if nome_ok:
                cargos = ["ADMINISTRADOR", "VENDEDOR", "ESTOQUE"]
                cargo, cargo_ok = QInputDialog.getItem(
                    None, "CARGOS", "Qual será o cargo?", cargos, 0, False)

                if cargo_ok:
                    matricula = secrets.token_hex(5)
                    dados_funcionario = (
                        matricula, nome_funcionario, cargo, usuario, senha)

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
                        msg.setText(
                            "Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
                        msg.exec()
                        db.fechar_conexao()
                        return

                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle("Aviso!")
                    msg.setText(
                        "Não foi possível cadastrar o usuário.\nDados insuficientes!")
                    msg.exec()
                    return -1
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Aviso!")
                msg.setText(
                    "Não foi possível cadastrar o usuário.\nDados insuficientes, tente novamente!")
                msg.exec()

    def remover_usuario(self):
        db = DB_Gerentia()
        db.conexao()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Remover Funcionário")
        msg.setText("O funcionário será excluído do sistema.")
        msg.setInformativeText("Tem certeza que deseja remove-lo?")
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

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
    window = Login()
    window.show()
    app.exec()
