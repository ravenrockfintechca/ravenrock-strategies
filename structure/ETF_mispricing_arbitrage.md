# 🧠 ETF Mispricing Arbitrage

**策略概述：**  
当ETF价格偏离其基础资产 NAV（净值）超过历史常态，捕捉价格回归。

**使用场景：**  
- $GLD vs 黄金期货  
- $HYG vs 高收益债券篮子

**信号逻辑：**
- ETF/NAV 偏离 > 1.5%
- 高成交量异动

**伪代码：**
```python
if abs(etf_price - nav_price) / nav_price > 0.015:
    open_pair_trade()
