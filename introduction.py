robios_welcome_message = "Olá, eu sou o Robios"

welcome_message = "Bem vindo a triagem do Covid-19\n" \
                  "Para a sua seguranca e dos demais clientes, por favor\n" \
                  "preencha com atencao o formulario de triagem a seguir."

class Introduction:

    def __init__(self, robios_intro = False):
        self.__robios_intro = robios_intro

    def start(self):
        self.intro()

    def intro(self):
        '''
        Metodo destinado a introducao e explicacoes sobre a aplicacao
        de triagem do Covid-19, sua importancia e eventuais instrucoes
        adicionais.
        '''
        if self.__robios_intro:
            self.introduce_robios()
        print(welcome_message)

    def introduce_robios(self):
        '''
        Metodo destinado a introducao e explicacoes sobre o Robios
        e seu funcionamento. A execucao é condicional e depende do
        param robios_intro definido ao instanciar a classe.
        '''
        print(robios_welcome_message)