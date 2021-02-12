# CDC Covid Screening flow at https://www.cdc.gov/screening/index.html
# Paper version available at https://www.cdc.gov/screening/paper-version.pdf

class ScreeningController:
    '''
    Controlador do processo de realizacao da triagem atraves de um
    formulario.

    O controlador respeita o primeiro principio SOLID, uma vez que
    apenas serve para controlar a parte de triagem, apresentando as
    perguntas e recebendo as respostas, nao se preocupando em como
    esse resultado sera divulgado ou utilizado posteriormente.
    '''

    def __init__(self, form_rules, form_results, log_user=False, user=None):
        self.form_rules = form_rules
        self.form_results = form_results
        self.__log_user = log_user
        self.__user = user
        self.form_results['risk'] = False
        self.form_results['answers'] = {}
        self.fast = False

    def start(self):
        '''
        Aqui, as questoes disponiveis em form_rules.json sao formatadas
        em perguntas de um formulario.

        As configuracoes estao preparadas para serem incrementadas com
        pacotes de linguas, como estamos apenas com o pacote de lingua
        portuguesa, os campos sao selecionados com o parametro ['pt_br'].

        A formatacao esta sendo realizada de forma independente do numero
        de perguntas, visando a alteracao futura sem refatoracao do codigo.

        Preencimento Rapido:
        (bool)self.fast liga/desliga o modo de preenchimento rapido. Ao
        ser ativado (True), o processo verifica as respostas do formulario
        enquanto sao preenchidas, de forma a terminar o processo quanto
        antes ao identificar potenciais sintomas/declaracoes que indiquem
        a presenca de COVID-19

        Log user:
        (bool0)self.__log_user liga/desliga o modo de preenchimento com
        dados de usuario, como nome e cpf. Mais informacoes em user.py
        '''
        if self.__log_user:
            self.__user.sign()
            self.form_results['user'] = self.__user.get_user()

        for id in self.form_rules['pt_br']['rules']:
            for key in id['condition'].keys():
                answer = input(id['pre_message']
                               + id['question'].format(id['condition'].get(key))
                               + id['post_message'])
                if answer.lower() == 'y' or answer.lower() == 'yes' or answer.lower() == 's' or answer.lower() == 'sim':
                    self.form_results['answers'][key] = True
                    self.form_results['risk'] = True
                    if not self.fast:
                        return
                else:
                    self.form_results['answers'][key] = False
