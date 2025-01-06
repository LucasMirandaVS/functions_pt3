import time
import logging
import pandas as pd
from functools import wraps

# Configuração do Log
logging.basicConfig(
    filename='logs/etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

# Decorador de Log
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executando {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Finalizou {func.__name__}")
        return result
    return wrapper

# Decorador de Timer
def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"{func.__name__} executou em {end_time - start_time:.2f} segundos")
        return result
    return wrapper

# Decorador de Qualidade
def qualidade_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, pd.DataFrame):
            nulos = result.isnull().sum().sum()
            logger.info(f"{func.__name__} retornou um DataFrame com {nulos} valores nulos")
        return result
    return wrapper
