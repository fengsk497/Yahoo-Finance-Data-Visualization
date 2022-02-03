
def Get_Stock_Price(ticker, start=None, end=None):
    import yfinance as yf
    target=yf.Ticker(ticker)
    if start==None and end== None:
        return target.history(period='max')
    else:
        return target.history(start=start,end=end)

def Get_Option_Price(ticker, c_p, strike, expiration,start=None, end=None):
    import yfinance as yf
    target=yf.Ticker(ticker)
    if expiration not in target.options:
        return None
    if c_p=='call':
        df=target.option_chain(expiration)[0]
        option_symbol=list(df.loc[df['strike']==strike]['contractSymbol'])[0]
    elif c_p=='put':
        df=target.option_chain(expiration)[1]
        option_symbol=list(df.loc[df['strike']==strike]['contractSymbol'])[0]
    return(Get_Stock_Price(option_symbol))

