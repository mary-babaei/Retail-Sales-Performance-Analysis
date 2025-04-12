import pandas as pd
from generat_data import GenerateData  # دقت کن که اسم کلاس اصلاح شده

class AnalysisSalesPerformance:
    def __init__(self, df):
        self.df = df

    def total_sales(self):
        return (self.df['Price'] * self.df['Quantity']).sum()

    def max_sales(self):
        return (self.df['Price'] * self.df['Quantity']).max()

    def min_sales(self):
        return (self.df['Price'] * self.df['Quantity']).min()

    def mean_sales(self):
        return (self.df['Price'] * self.df['Quantity']).mean()

    def popular_products(self):
        return self.df.groupby('Products')['Quantity'].sum().idxmax()

    def sales_by_products(self):
        return self.df.groupby('Products')['Quantity'].sum()

    def sales_by_customer(self):
        return self.df.groupby('CustomersID').apply(lambda x: (x['Price'] * x['Quantity']).sum())

    def sales_by_order(self):
        return self.df.groupby('OrderID').apply(lambda x: (x['Price'] * x['Quantity']).sum())

    def sales_by_date(self):
        return self.df.groupby('OrderDate').apply(lambda x: (x['Price'] * x['Quantity']).sum())

    def filter_by_date(self, start_date, end_date):
        self.df['OrderDate'] = pd.to_datetime(self.df['OrderDate'])
        return self.df[(self.df['OrderDate'] >= start_date) & (self.df['OrderDate'] <= end_date)]

#تولید داده
data_generator = GenerateData()
df = data_generator.generate_random_data()


# ایجاد نمونه از کلاس آنالیز
analysis = AnalysisSalesPerformance(df)

# فیلتر کردن بر اساس تاریخ
filtered_data = analysis.filter_by_date('2020-01-01', '2025-03-10')
print("✅ Filtered Data:\n", filtered_data)
