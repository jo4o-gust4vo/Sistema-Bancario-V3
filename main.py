from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf






class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        excedeu_saldo = valor > self._saldo

        if valor > self._saldo:
            self._saldo -= valor
            print('Saldo realizado com sucesso!')
            return True

        elif excedeu_saldo:
            print('Valor excedeu o saldo.')
            return False
        else:
            print('Algo deu errado. Tente novamente.')

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Deposito realizado com sucesso!')
            return True
        else:
            print('Algo deu errado. Tente novamente.')
            return False
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero,cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques =  len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
               )
        execedeu_limite = valor > self._limite
        execedeu_saques = valor > self._limite_saques

        if execedeu_limite or execedeu_saques:
            print('Execedeu Limites!')

        elif execedeu_saques :
            print('Excedeu numero de saques!')

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f'''\
            Agência: \t{self._agencia}
            C/C:\t\t{self._numero}
            Titular:\t{self.cliente.nome}
        '''

class Historico:
    def __init__(self):
        self._transacoes = []

        @property
        def transacoes(self):
            return self._transacoes
        def adicionar_transacao(self, transacao):
            self._transacoes.append(
                {
                    'tipo': transacao.__class__.__name__,
                    'valor': transacao.valor,
                    'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                }
            )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)






