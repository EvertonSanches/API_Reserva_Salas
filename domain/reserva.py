class Reserva:
    def __init__(
        self,
        id: int,
        usuario_id: int,
        sala_id: int,
        data: str,
        hora_inicio: str,
        hora_atual: str,
        hora_fim: str,
        status: str = "active"
    ):
        self.id = id
        self.usuario_id = usuario_id
        self.sala_id = sala_id
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_atual = hora_atual
        self.hora_fim = hora_fim
        self.status = status

    def cancelar(self, usuario_id, data, hora_fim, status)-> bool:
        if self.sala_id:
                status == "active"
                False
                raise ValueError("Essa reserva já está cancelada")
        return "Reserva Cancelada com sucesso!"
        

    def finalizar(self, hora_atual: str, hora_fim: str):
        if hora_atual >= hora_fim:
             return "Reserva Finalizada"
             

    def duracao_em_horas(self, hora_inicio: str, hora_fim: str) -> float:
        

    def conflita_com(self, outra_reserva) -> bool:
        pass