import pandas as pd
from generat_data import *
import matplotlib.pyplot as plt
import seaborn as sns

class StatisticAnalysis:
    def __init__(self, df):
        self.df = df

        # تبدیل داده‌ها به عددی و جایگزینی خطاها با NaN
        self.df['Price'] = pd.to_numeric(self.df['Price'], errors='coerce')
        self.df['Quantity'] = pd.to_numeric(self.df['Quantity'], errors='coerce')

        # حذف مقادیر NaN
        self.df = self.df.dropna(subset=['Price', 'Quantity'])

    def describe_data(self):
        print("📋 Summary Statistics:")
        print(self.df.describe())

    def mean_quantity(self):
        print("Mean Quantity:", self.df['Quantity'].mean())

    def median_quantity(self):
        print("Median Quantity:", self.df['Quantity'].median())

    def mean_price(self):
        print("Mean Price:", self.df['Price'].mean())

    def std_quantity(self):
        print("Std of Quantity:", self.df['Quantity'].std())

    def mode_products(self):
        print("Mode Products:", self.df['Quantity'].mode())
    def correlation_matrix(self):
        print("🔗 Correlation Matrix:")
        print(self.df.corr())

    def sales_analysis(self):
        price = self.df['Price']
        quantity = self.df['Quantity']
        sales = price * quantity

        print("📊 Sales Statistics:")
        print("Mean Sales:", sales.mean())
        print("Median Sales:", sales.median())
        print("Std Sales:", sales.std())
        print("Skewness:", sales.skew())
        print("Kurtosis:", sales.kurtosis())
        print("Variance:", sales.var())


    # def plot_histogram(self, column='Price'):
    #     plt.figure(figsize=(10, 6))
    #     plt.hist(self.df[column], bins=20, color='skyblue', edgecolor='black')
    #     plt.title(f"Histogram of {column}")
    #     plt.xlabel(column)
    #     plt.ylabel("Frequency")
    #     plt.grid(True)
    #     plt.savefig(r"C:\Users\Maryam\Desktop\charts\Histogram_of_{0}.png".format(column))
    #
    # def plot_heatmap(self):
    #     self.df['Price'] = pd.to_numeric(self.df['Price'], errors='coerce')
    #     self.df['Quantity'] = pd.to_numeric(self.df['Quantity'], errors='coerce')
    #     self.df = self.df.dropna(subset=['Price', 'Quantity'])
    #     # انتخاب فقط ستون‌های عددی
    #     numeric_df = self.df.select_dtypes(include=['number'])
    #
    #     plt.figure(figsize=(10, 6))
    #     sns.heatmap(numeric_df.corr(), cmap='coolwarm', fmt='.2f', linewidths=0.5)
    #     plt.title("Correlation Heatmap")
    #     plt.savefig(r"C:\Users\Maryam\Desktop\charts\Correlation_Heatmap.png")
    #
