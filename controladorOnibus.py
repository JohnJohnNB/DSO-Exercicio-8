from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):
    def __init__(self, capacidade, total_passageiros, ligado):
        super().__init__()
        self.__onibus = self.inicializar_onibus(capacidade, total_passageiros, ligado)

    def ligar(self) -> str:
        pass

    def desligar(self) -> str:
        pass

    def embarca_pessoa(self) -> str:
        pass

    def desembarca_pessoa(self) -> str:
        pass

    @property
    def onibus(self) -> Onibus:
        return self.__onibus

    def inicializar_onibus(self, capacidade: int, total_passageiros: int, ligado: bool):
        if isinstance(capacidade, int) and isinstance(total_passageiros, int) and isinstance(ligado, bool):
            if capacidade < 0 or total_passageiros < 0 or total_passageiros > capacidade or not ligado:
                raise ComandoInvalidoException
            onibus = Onibus(capacidade, total_passageiros, ligado)
            return onibus
        else:
            raise ComandoInvalidoException
