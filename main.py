# CDC Covid Screening flow at https://www.cdc.gov/screening/index.html
# Paper version available at https://www.cdc.gov/screening/paper-version.pdf


from introduction import Introduction
from screening_controller import ScreeningController
from mqtt import ClientMQTT
from user import User
import json


class Main:

    def __init__(self, log_user=True):
        self.__log_user = log_user
        self.__user = User()
        self.__form_result = {}

        self.intro()
        self.__form_rules = self.load_form_rules()
        self.__start_screening()
        self.send_result()

    def intro(self):
        introduction = Introduction(robios_intro=False)
        introduction.start()

    def load_form_rules(self):
        rules = open('screening_rules.json')
        return json.load(rules)

    def __start_screening(self):
        # self.user, self.form_result
        screening = ScreeningController(self.__form_rules,
                                        self.__form_result,
                                        log_user=self.__log_user,
                                        user=self.__user)
        screening.start()

    def send_result(self):
        client = ClientMQTT()
        client.publish(self.__form_result)


if __name__ == '__main__':
    main_activity = Main()
