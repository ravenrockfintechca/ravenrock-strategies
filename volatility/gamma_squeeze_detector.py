import pandas as pd

def detect_gamma_squeeze(df):
    if df['IV'].pct_change().iloc[-1] > 0.3 and df['volume'].iloc[-1] > 2 * df['avg_volume']:
        return "⚠️ Gamma Squeeze 可能触发"
