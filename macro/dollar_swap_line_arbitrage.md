# 🧠 Dollar Swap Line Arbitrage

**逻辑说明：**  
追踪美联储Swap Line使用量 + EUR/USD Cross-Currency Basis，捕捉美元流动性紧张，建立方向性套利。

**适用市场：**  
- G10外汇（EUR/USD）  
- 美债利差合约  
- ETF: $UUP, $FXE  

**核心信号：**  
- Swap Line 使用量 > 3个月均值  
- Cross-Currency Basis < -30bp  
- DXY 反弹

**伪代码实现：**
```python
if swap_line > avg(swap_line, 12wks) and basis < -30:
    signal = "Long USD / Short EUR"
