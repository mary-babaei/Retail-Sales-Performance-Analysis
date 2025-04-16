from charts import *
from Statistic import *
from model import *
from Analysis import *


if __name__ == '__main__':
    # تولید داده
    data_generator = GenerateData()
    df = data_generator.generate_random_data()

    # تحلیل داده
    analysis = AnalysisSalesPerformance(df)
    print("✅ Total Sales:", analysis.total_sales())
    print("✅ Max Sales:", analysis.max_sales())
    print("✅ Min Sales:", analysis.min_sales())
    print("✅ Mean Sales:", analysis.mean_sales())
    print("✅ Popular Product:", analysis.popular_products())
    print("✅ Sales by Customer:\n", analysis.sales_by_customer())
    print("✅ Sales by Order:\n", analysis.sales_by_order())
    print("✅ Sales by Products:\n", analysis.sales_by_products())

    # رسم نمودارها
    charts = Charts(df)
    print(charts.plt_products_sales())
    print(charts.plt_pie_product_sales())
    print(charts.plt_products_sales())
    print(charts.plt_filtered_date('2020-01-01', '2025-03-10'))
    print(charts.plt_filtered_product_sales('book', '2023-01-01', '2024-12-31'))
    print(charts.plt_pie_product_sales())
    print(charts.plt_boxplot_sales())
    print(charts.plt_boxplot_price())
    print(charts.plt_scatter())

    #تحلیل آماری
    stats = StatisticAnalysis(df)
    print(stats.describe_data())
    stats.plot_histogram('Price')
    stats.plot_histogram('Quantity')
    stats.plot_heatmap()

    # پیش بینی و مدلسازی
    print("🌟 شروع مدلسازی...")
    model_instance = SalesPredictionModel(df)  # ← ساختن شیء از کلاس با دیتافریم
    X_train, X_test, y_train, y_test = model_instance.preprocess_data()
    model = model_instance.train_and_evaluate()
    predictions = model.predict(X_test)
    print("🔍 مدل ما این مقدار فروش‌ها رو پیش‌بینی کرده:")
    print(predictions[:10])  # ۱۰ پیش‌بینی اول
    print("🎯 مقادیر واقعی:")
    print(y_test[:10])  # ۱۰ مقدار واقعی




    print("🌟 پایان برنامه.")
