class User:
    """
    Caso seja ativado o registro de usuario na classe Main, a
    triagem é iniciada coletando dados do usuário, a fim de
    expandir a funcionalidade para lojas de franquias, shoppings
    ou uso interno empresarial.
    
    O registro do usuário foi feito de modo a ser escalável,
    podendo acrescentar novos campos de identificação criando um
    novo método em User e passando em seu construtor.
    
    Adicionando novos campos:
    Para adicionar novos campos de identificacao, crie um novo
    metodo destinado a tal campo e chame no metodo sign(self)
    Alem disso, para armazenar o valor, adicione uma nova key
    e seu valor de entrada no dicionario self.__user_data.
    """

    __user_data = {}

    def sign(self):
        self.request_name()
        self.request_cpf()

    def request_name(self):
        name = input("Por favor, insira seu nome")
        print(f"Nome: {name}, confirmar?")
        confirm = input("(Yes/No)")
        if confirm.lower() == "y" or confirm.lower() == "yes":
            self.__user_data['name'] = name
        else:
            self.request_name()
        print(name)

    def request_cpf(self):
        cpf = input(f"Olá {self.__user_data.get('name')}\nPor favor, digite o seu CPF")
        print(f"CPF: {cpf}, confirmar?")
        confirm = input("(Yes/No)")
        if confirm.lower() == "y" or confirm.lower() == "yes":
            self.__user_data['cpf'] = cpf
        else:
            self.request_cpf()
        print(cpf)

    def get_user(self):
        return self.__user_data
