ICA = {
    "consultoria": 8.66,
    "construccion": 7.12,
    "farmacias": 9.98,
    "financieras": 14,
}

YES_OR_NOT = ['Y', 'N']
class ProductWithVat:
    amount: float = None
    def __init__(self, amount: float):
        self.amount = amount

    def calculate_rte_f(self):
        rte_fuente_aplica = None
        while rte_fuente_aplica not in YES_OR_NOT:
            rte_fuente_aplica = input("ingrese la rt fuente Y/N: ")
        valor_rte_fuente = 0 if rte_fuente_aplica == 'N' else 0.28
        return self.amount * valor_rte_fuente

    def calculate_common_vat(self):
        return self.amount * 1.19

    def calculate_ica(self):
        ica = input("ingrese la actividad comercial: ")
        valor_ica = ICA.get(ica, 0)
        n_applicar_ica = int(self.amount / 1000)
        valor_a_cobrar_ica = n_applicar_ica * valor_ica
        return valor_a_cobrar_ica

    def calculate_vat(self):
        return self.calculate_common_vat() + self.calculate_ica() + self.calculate_rte_f()


if __name__ == "__main__":
    valor_producto = input("calcular el impuesto de: ")
    print(calculate_vat(float(valor_producto)))
