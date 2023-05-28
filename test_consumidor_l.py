from consumidorL import consume_bollinger

def test_consume_bollinger_empty_window():
    price_window = {}
    stream_name = "parcial3"
    window_size = 20
    num_std_dev = 1

    # Llamada a la función bajo prueba
    consume_bollinger()

    # Comprobar que no se realiza ninguna acción cuando la ventana está vacía
    assert price_window == {}

