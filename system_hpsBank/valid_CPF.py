import re

class verification_CPF:
    def __init__(self, cpf):
        self.cpf = cpf



    @property
    def cpf(self):
        return self.cpf

    @cpf.setter
    def cpf(self, cpf):
        self.cpf = self._so_numbers(cpf)

    @staticmethod
    def _so_numbers(cpf):
        return.re.sub('[0-9]', '', cpf)
