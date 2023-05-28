import time
import json
from unittest.mock import MagicMock, ANY
from producer1 import generate

def test_generate_continuous_data_generation():
    # Configurar el estado inicial
    stream_name = "parcial3"
    kinesis_client = MagicMock()
    
    # Llamar a la función durante un período de tiempo
    start_time = time.time()
    while time.time() - start_time < 5:  # Generar datos durante 5 segundos
        generate(stream_name, kinesis_client)
    
    # Comprobar que se llamó a la función put_record varias veces
    assert kinesis_client.put_record.call_count > 1

