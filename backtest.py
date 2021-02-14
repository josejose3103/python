import datetime
import pandas as pd
from backtesting import Strategy
from backtesting import Backtest
 
class myCustomStrategy(Strategy):
    def init(self):
        pass
 
    def next(self): 
        self.buy if self.data.Close[-1]> self.data.Open[-1] else self.sell()
 
df = pd.read_csv("6701_2020.csv", skiprows=2000, names=("Datetime", "Open", "High", "Low", "Close", "Volume"), index_col='Datetime')
# 欠損値を埋める
df = df.interpolate()
df.index = pd.to_datetime(df.index)
bt = Backtest(df, myCustomStrategy, cash=1000000, commission=.001)
bt.run()
# bt.plot()
