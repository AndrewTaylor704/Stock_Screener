import numpy as np
import pandas as pd
import requests

class Stock():
    def __init__(self, current_price, price_history, fundamentals):
        self.current_price = current_price
        self.price_history = price_history
        self.fundamentals = fundamentals