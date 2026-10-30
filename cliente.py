class Cliente:
    def __init__(self, nome, cpf, email):
        self._nome = nome
        self._cpf = cpf
        self._email = email

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def email(self):
        return self._email

    def exibir_dados(self):
        return (
            f"Nome: {self._nome}\n"
            f"CPF: {self._cpf}\n"
            f"E-mail: {self._email}"
        )