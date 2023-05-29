from consumidorL import check_bollinger

def test_empty_price_window():
    # Configurar datos de prueba
    price_window = []
    price = 190
    stock = "AAPL"

    # Ejecutar la función que se está probando
    result = check_bollinger(price_window, price, stock)

    # Verificar que no se generó ninguna alerta
    assert result is None

# Ejecutar la prueba
if __name__ == '__main__':
    test_no_alert_triggered()

