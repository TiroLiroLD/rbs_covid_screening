# CDC Covid Screening flow at https://www.cdc.gov/screening/index.html
# Paper version available at https://www.cdc.gov/screening/paper-version.pdf


from introduction import Introduction
from screening_controller import ScreeningController
from mqtt import ClientMQTT
from user import User
import json


class Main:

    def __init__(self, log_user = True):
        self.__log_user = log_user
        self.__user = User()
        self.__form_result = {}

        self.intro()
        self.__form_rules = self.load_form_rules()
        self.__start_screening()
        self.screening_send_result()

    def intro(self):
        introduction = Introduction(robios_intro=True, log_user=self.__log_user, user=self.__user)
        introduction.start()

    def load_form_rules(self):
        rules = open('screening_rules.json')
        return json.load(rules)

    def __start_screening(self):
        # self.user, self.form_result
        screening = ScreeningController(self.__form_rules, self.__form_result)
        screening.start()


    def screening_send_result(self):
        self.__prepare_result()
        client = ClientMQTT()
        client.publish(self.__form_result)


    def __prepare_result(self):
        if self.__log_user:
            self.__form_result['user'] = self.__user.get_user()


if __name__ == '__main__':
    main_activity = Main()
