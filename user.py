class User:

    __user_data = {}

    def sign(self):
        self.request_name()
        self.request_cpf()

    def request_name(self):
        '''
        TODO
        '''
        name = input("Por favor, insira seu nome")
        print(f"Nome: {name}, confirmar?")
        confirm = input("(Yes/No)")
        if confirm.lower() == "y" or confirm.lower() == "yes":
            self.__user_data['name'] = name
        else:
            self.request_name()
        print(name)

    def request_cpf(self):
        '''
        TODO
        '''
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
