import yfinance as yf
import matplotlib.pyplot as plt

jgb = yf.download("10JGB.BD", start="2024-01-01")
jgb['Yield'].plot(title="日本10年国债收益率爆发")
plt.axhline(1.0, color='red', linestyle='--')
plt.show()
