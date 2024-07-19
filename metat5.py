import MetaTrader5 as mt
from datetime import datetime

mt.initialize()
login=10000521364
password="nFznbFEP"
server = 'MetaQuotes-Demo'

mt.login(login,password,server)
#rates = mt.copy_rates_from('TSLA.NAS', mt.TIMEFRAME_D1, datetime.now(),100)
ticker='TSLA.NAS'
interval = mt.TIMEFRAME_D1
from_date = datetime.now()
no_of_rows= 100
rates = mt.copy_rates_from(ticker,interval,from_date,no_of_rows)
print(rates)
