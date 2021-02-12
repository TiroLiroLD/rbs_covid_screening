class Introduction:

    def __init__(self, robios_intro=False, log_user=False, user=None):
        self.__log_user = log_user
        self.__user = user
        self.__robios_intro = robios_intro

    def start(self):
        self.intro()
        self.new_screening()

    def intro(self):
        '''
        Metodo destinado a introducao e explicacoes sobre a aplicacao
        de triagem do Covid-19, sua importancia e eventuais instrucoes
        adicionais.
        '''

        if self.__robios_intro:
            self.introduce_robios()

        print("Bem vindo a triagem do Covid-19\n"
              "Este formulario visa o bem de todos")
        # TODO

    def introduce_robios(self):
        '''
        Metodo destinado a introducao e explicacoes sobre o Robios
        e seu funcionamento. A execucao é condicional e depende do
        param robios_intro definido ao instanciar a classe.
        '''
        print("Olá, eu sou o Robios")

    def new_screening(self):
        '''
        Método destinado a iniciar nova triagem de corona virus.

        Caso log_user seja passado True na instancia da classe, a
        triagem é iniciada coletando nome e CPF do usuário, a fim de
        expandir a funcionalidade para lojas de franquias, shoppings
        ou uso interno empresarial.

        O registro do usuário foi feito de modo a ser escalável,
        podendo acrescentar novos campos de identificação criando um
        novo método em User e passando em seu construtor. Mais
        detalhes no arquivo user.py
        '''

        if self.__log_user:
            self.__user.sign()
            print(self.__user.get_user())
