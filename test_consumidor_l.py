from consumidorL import check_bollinger

def test_no_alert_triggered():
    # Configurar datos de prueba
    price_window = [120, 140, 160, 180, 200]
    price = 190
    stock = "AAPL"

    # Ejecutar la función que se está probando
    result = check_bollinger(price_window, price, stock)

    # Verificar que no se generó ninguna alerta
    assert result is None

# Ejecutar la prueba
if __name__ == '__main__':
    test_no_alert_triggered()

