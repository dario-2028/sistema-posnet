class Posnet:
    def efectuarPago(self, card, amount, installments):
        
        if card.getBankEntity() not in ["Birza", "CasterMard"]:
            print("Operación no exitosa. Entidad financiera no válida.")
            return None

        
        if installments == 1:
            total_amount = amount
        elif 1 < installments <= 6:
            total_amount = amount * (1 + 0.03 * (installments - 1))
        else:
            print("Operación no exitosa. Cantidad de cuotas no válida.")
            return None

        
        if card.getBalance() < total_amount:
            print("Operación no exitosa. Saldo insuficiente.")
            return None

        
        installment_amount = total_amount / installments
        print("Ticket:")
        print(f"Nombre y apellido del cliente: {card.getHolder().getName()} {card.getHolder().getLastName()}")
        print(f"Monto total a pagar: {total_amount}")
        print(f"Monto de cada cuota: {installment_amount}")

        
        card.setBalance(card.getBalance() - total_amount)

        
        return {
            "Cliente": f"{card.getHolder().getName()} {card.getHolder().getLastName()}",
            "Monto total": total_amount,
            "Monto por cuota": installment_amount
        }
