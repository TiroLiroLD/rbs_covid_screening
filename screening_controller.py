# CDC Covid Screening flow at https://www.cdc.gov/screening/index.html
# Paper version available at https://www.cdc.gov/screening/paper-version.pdf

class ScreeningController:
    '''
    Controlador do processo de realizacao da triagem
    atraves de um formulario.
    '''

    def __init__(self, form_rules, form_results):
        self.form_rules = form_rules
        self.form_results = form_results
        self.form_results['risk'] = False
        self.form_results['answers'] = {}
        self.full = False

    def start(self):
        '''
        TODO
        '''
        for id in self.form_rules['pt_br']['rules']:
            for key in id['condition'].keys():
                answer = input(id['question'].format(id['condition'].get(key)))
                if answer.lower() == 'y' or answer.lower() == 'yes' or answer.lower() == 's' or answer.lower() == 'sim':
                    self.form_results['answers'][key] = True
                    self.form_results['risk'] = True
                    if not self.full:
                        return
                else:
                    self.form_results['answers'][key] = False