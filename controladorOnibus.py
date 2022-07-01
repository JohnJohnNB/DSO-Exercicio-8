from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):
    def __init__(self):
        super().__init__()
        self.__onibus = None

    def ligar(self) -> str:
        self.__onibus.ligar()

    def desligar(self) -> str:
        self.__onibus.desligar()

    def embarca_pessoa(self) -> str:
        self.__onibus.embarca_pessoa()

    def desembarca_pessoa(self) -> str:
        self.__onibus.desembarca_pessoa()

    @property
    def onibus(self) -> Onibus:
        return self.__onibus

    def inicializar_onibus(self, capacidade: int,
                           total_passageiros: int, ligado: bool):
        if isinstance(capacidade, int) and isinstance(total_passageiros, int)\
                and isinstance(ligado, bool):
            if capacidade < 0 or total_passageiros < 0 or \
                    total_passageiros > capacidade or not ligado:
                raise ComandoInvalidoException
            onibus = Onibus(capacidade, total_passageiros, ligado)
            self.__onibus = onibus
        else:
            raise ComandoInvalidoException
