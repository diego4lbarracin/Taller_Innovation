import argparse

# Tasas de cambio almacenadas en el modelo (última información disponible)
exchange_rates = {
    'USD': {
        'EUR': 0.88,
        'JPY': 115.15,
        'GBP': 0.74,
        'MXN': 20.50
    },
    'EUR': {
        'USD': 1.14,
        'JPY': 130.50,
        'GBP': 0.84,
        'MXN': 23.30
    },
    'JPY': {
        'USD': 0.0087,
        'EUR': 0.0077,
        'GBP': 0.0064,
        'MXN': 0.18
    },
    'GBP': {
        'USD': 1.35,
        'EUR': 1.19,
        'JPY': 156.50,
        'MXN': 27.80
    },
    'MXN': {
        'USD': 0.049,
        'EUR': 0.043,
        'JPY': 5.56,
        'GBP': 0.036
    }
}

def get_exchange_rate(from_currency, to_currency):
    """
    Obtiene la tasa de cambio de una divisa a otra desde las tasas almacenadas.

    :param from_currency: Código de la divisa de origen (por ejemplo, 'USD')
    :param to_currency: Código de la divisa de destino (por ejemplo, 'EUR')
    :return: Tasa de cambio de la divisa de origen a la divisa de destino
    """
    try:
        return exchange_rates[from_currency][to_currency]
    except KeyError:
        raise ValueError(f"Tasa de cambio no disponible para {from_currency} a {to_currency}")

def convert_currency(amount, from_currency, to_currency):
    """
    Convierte una cantidad de una divisa a otra utilizando la tasa de cambio actual.

    :param amount: Cantidad de dinero a convertir
    :param from_currency: Código de la divisa de origen (por ejemplo, 'USD')
    :param to_currency: Código de la divisa de destino (por ejemplo, 'EUR')
    :return: Cantidad convertida en la divisa de destino
    """
    rate = get_exchange_rate(from_currency, to_currency)
    return amount * rate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convertir divisas utilizando tasas de cambio almacenadas.")
    parser.add_argument("amount", type=float, help="Cantidad de dinero a convertir")
    parser.add_argument("from_currency", type=str, help="Código de la divisa de origen (por ejemplo, 'USD')")
    parser.add_argument("to_currency", type=str, help="Código de la divisa de destino (por ejemplo, 'EUR')")

    args = parser.parse_args()

    try:
        converted_amount = convert_currency(args.amount, args.from_currency, args.to_currency)
        print(f"{args.amount} {args.from_currency} son {converted_amount:.2f} {args.to_currency}")
    except ValueError as e:
        print(e)