import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('alphabet_stock_data.csv')
plt.title("Trading Volume of Alphabet Inc. Stock (2020-04-15 to 2020-05-15)", loc= 'center')
plt.xlabel('Date')
plt.ylabel('Trading Volume')
