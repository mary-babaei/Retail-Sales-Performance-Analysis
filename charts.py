import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from Analysis import AnalysisSalesPerformance  # ✅ ایمپورت صحیح کلاس تحلیل داده


class Charts:
    def __init__(self, df):
        self.analysis = AnalysisSalesPerformance(df)  # ✅ ساخت شیء تحلیل داده

    def plt_products_sales(self):
        products_sales = self.analysis.sales_by_products()
        if products_sales.empty:
            print("⚠ No data to plot for product sales!")
            return

        plt.figure(figsize=(10, 5))
        plt.bar(products_sales.index, products_sales.values, color='g', alpha=0.7)
        plt.xlabel('Products', fontsize=14, fontweight='bold')
        plt.ylabel('Sales', fontsize=14, fontweight='bold')
        plt.title('Product Sales', fontsize=16, fontweight='bold', color='darkblue')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.savefig(r"C:\Users\Maryam\Desktop\charts\filtered_data.png")

    def plt_filtered_date(self, start_date, end_date):
        f_date = self.analysis.filter_by_date(start_date, end_date)
        products_sales = f_date.groupby('Products')['Quantity'].sum()

        if products_sales.empty:
            print("⚠ No sales data in this date range!")
            return

        plt.figure(figsize=(10, 5))
        plt.plot(products_sales.index, products_sales.values, marker='o', linestyle='-', color='b')
        plt.xlabel('Products', fontsize=12)
        plt.ylabel('Total Quantity Sold', fontsize=12)
        plt.xticks(rotation=45)
        plt.title(f'Product Sales from {start_date} to {end_date}', fontsize=16, fontweight='bold', color='darkblue')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.savefig(r"C:\Users\Maryam\Desktop\charts\filtered_product_sales.png")

    def plt_filtered_product_sales(self, product_name, start_date, end_date):
        f_data = self.analysis.filter_by_date(start_date, end_date)
        product_sales = f_data[f_data['Products'] == product_name]
        sales_trend = product_sales.groupby('OrderDate')['Quantity'].sum()

        if sales_trend.empty:
            print(f"⚠ No sales data for {product_name} in this date range!")
            return

        plt.figure(figsize=(10, 5))
        plt.plot(sales_trend.index, sales_trend.values, marker='o', linestyle='-', color='b')
        plt.xlabel('Date')
        plt.ylabel('Sales Quantity')
        plt.xticks(rotation=45)
        plt.title(f'Sales Trend for {product_name}', fontsize=16, fontweight='bold', color='darkblue')
        plt.savefig(r"C:\Users\Maryam\Desktop\charts\pie_products_sales.png")

    def plt_pie_product_sales(self):
        products_sales = self.analysis.sales_by_products()

        if products_sales.empty:
            print("⚠ No data to plot for pie chart!")
            return

        plt.figure(figsize=(10, 5))
        colors = plt.cm.Paired.colors
        explode = [0.1 if v == max(products_sales.values) else 0 for v in products_sales.values]
        plt.pie(products_sales.values, labels=products_sales.index, autopct='%1.1f%%',
                startangle=90, colors=colors, explode=explode,
                wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
        plt.title('Product Sales Distribution')
        plt.savefig(r"C:\Users\Maryam\Desktop\charts\boxplot_sales.png")

    def plt_boxplot_sales(self):
        products_sales = self.analysis.sales_by_products()

        if products_sales.empty:
            print("⚠ No data to plot for boxplot!")
            return

        plt.figure(figsize=(10, 5))
        plt.boxplot(products_sales.values)
        plt.title('Product Sales Boxplot')
        plt.savefig(r"C:\Users\Maryam\Desktop\charts\boxplot_sales.png")

    def plt_boxplot_price(self):
        plt.figure(figsize=(10, 5))
        plt.boxplot(self.analysis.df['Price'])
        plt.title('Product Price Boxplot')
        plt.savefig(r"C:\Users\Maryam\Desktop\charts\boxplot_price.png")

    def plt_scatter(self):
        book_sales = self.analysis.df[self.analysis.df['Products'] == 'book']

        if book_sales.empty:
            print("⚠ No data for scatter plot (No sales for 'book')")
            return

        plt.figure(figsize=(10, 5))
        sns.regplot(x='Price', y='Quantity', data=book_sales, scatter_kws={'s': 10}, line_kws={'color': 'red'})
        plt.xlabel('Price')
        plt.ylabel('Sales Quantity for book')
        plt.title('Product Sales Scatter')
        plt.savefig(r"C:\Users\Maryam\Desktop\charts\scatter.png")


