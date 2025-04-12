import pandas as pd
import numpy as np
import random

class GenerateData:
    def __init__(self):
        self.df = self.generate_random_data()

    def generate_random_data(self):
        products = ['laptop', 'phone', 'computer', 'keyboard', 'tablet', 'mouse', 'book', 'speaker']

        def generate_random_date(start, end):
            return pd.to_datetime(np.random.choice(pd.date_range(start=start, end=end, freq='D')))

        data = []
        for orderid in range(1, 1000):
            product = random.choice(products)
            customers_id = 'C' + str(random.randint(1, 999)).zfill(3)
            price = random.randint(1, 1000)
            quantity = random.randint(1, 1000)
            orderdate = generate_random_date('2020-01-01', '2025-03-10')

            data.append([customers_id, product, price, quantity, orderid, orderdate])

        return pd.DataFrame(data, columns=['CustomersID', 'Products', 'Price', 'Quantity', 'OrderID', 'OrderDate'])

