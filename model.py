from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from generat_data import *

class SalesPredictionModel:
    def __init__(self, df):
        self.df = df

    def preprocess_data(self):
        # ساخت ستون فروش
        self.df['Sales'] = self.df['Price'] * self.df['Quantity']
        print(self.df.head())
        # تبدیل تاریخ به ویژگی‌های عددی
        self.df['Year'] = self.df['OrderDate'].dt.year
        self.df['Month'] = self.df['OrderDate'].dt.month
        self.df['Day'] = self.df['OrderDate'].dt.day

        # تبدیل Product به ستون‌های عددی (one-hot encoding)
        if 'Products' in self.df.columns:
            self.df = pd.get_dummies(self.df, columns=['Products'])
        # تعریف ورودی‌ها و خروجی مدل
        X = self.df[['Price', 'Quantity', 'Year', 'Month', 'Day'] +
                    [col for col in self.df.columns if col.startswith('Products_')]]
        y = self.df['Sales']

        print("🚨 داده‌های ورودی X:")
        print(X.head())  # بررسی اولین چند ردیف از داده‌ها

        print("🚨 داده‌های خروجی y:")
        print(y.head())  # بررسی اولین چند ردیف از داده‌های خروجی

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # پرینت کردن داده‌های تقسیم‌شده
        print("🚨 داده‌های تقسیم‌شده:")
        print(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")
        print(f"y_train shape: {y_train.shape}, y_test shape: {y_test.shape}")

        return X_train, X_test, y_train, y_test

    def train_and_evaluate(self):
        print("🔵 شروع آموزش مدل...")

        X_train, X_test, y_train, y_test = self.preprocess_data()

        print("🔵 آموزش مدل...")
        model = LinearRegression()
        model.fit(X_train, y_train)

        # پیش‌بینی‌ها
        y_pred = model.predict(X_test)

        # بررسی مقادیر
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # پرینت نتایج
        print("🔢 Mean Squared Error:", mse)
        print("📈 R-squared Score:", r2)

        return model

#
# if __name__ == '__main__':
#     from generat_data import GenerateData
#
#     data_generator = GenerateData()
#     df = data_generator.generate_random_data()
#
#     print("📦 دیتافریم ساخته شد:", df.shape)
#
#     model_instance = SalesPredictionModel(df)
#     model = model_instance.train_and_evaluate()
