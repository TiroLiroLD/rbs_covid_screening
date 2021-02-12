# CDC Covid Screening flow at https://www.cdc.gov/screening/index.html
# Paper version available at https://www.cdc.gov/screening/paper-version.pdf

class ScreeningController:
    '''
    TODO
    '''

    def __init__(self, form_rules, form_results):
        self.form_rules = form_rules
        self.form_results = form_results
        self.form_results['answers'] = {}

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
                else:
                    self.form_results['answers'][key] = False