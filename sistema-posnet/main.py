from Posnet import Posnet
from CreditCard import CreditCard
from CardHolder import CardHolder

if __name__ == "__main__":
    
    posnet = Posnet()

    
    card_holder = CardHolder("12345678", "John", "Doe", "123456789", "john.doe@example.com")

    
    credit_card = CreditCard("Birza", "1234-5678-9012-3456", 15000, card_holder)

    
    result = posnet.efectuarPago(credit_card, 10000, 5)

    
    if result is not None:
        print("Pago exitoso. Detalles del ticket:")
        print(f"Cliente: {result['Cliente']}")
        print(f"Monto total: {result['Monto total']}")
        print(f"Monto por cuota: {result['Monto por cuota']}")
    else:
        print("Pago no exitoso. Se encontraron problemas durante la transacción.")


