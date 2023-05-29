from producer1 import get_data

def test_get_data_valid_event_time():
    data = get_data()
    event_time = data.get('event_time')

    assert event_time is not None
    assert isinstance(event_time, str)
    assert len(event_time) > 0
    assert event_time.count(':') == 2  # Verificar el formato HH:MM:SS
    assert event_time.count('-') == 2  # Verificar el formato AAAA-MM-DD

def test_get_data_valid_stock():
    data = get_data()
    stock = data.get('stock')

    assert stock is not None
    assert isinstance(stock, str)
    assert len(stock) > 0
    assert stock in ['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']  # Verificar valores válidos

def test_get_data_valid_price():
    data = get_data()
    price = data.get('price')

    assert price is not None
    assert isinstance(price, (int, float))
    assert price >= 0
    assert price <= 200  # Verificar rango válido

