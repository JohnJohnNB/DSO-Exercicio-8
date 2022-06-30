from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):
    def __init__(self):
        super().__init__()
        self.__onibus = None

    def ligar(self) -> str:
        if self.__onibus.ligado:
            self.__onibus.ligar()

    def desligar(self) -> str:
        pass

    def embarca_pessoa(self) -> str:
        pass

    def desembarca_pessoa(self) -> str:
        pass

    @property
    def onibus(self) -> Onibus:
        return self.__onibus


