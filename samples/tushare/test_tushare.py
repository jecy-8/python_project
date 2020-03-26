import tushare


if __name__ == '__main__':
    print('tushare info:\n author: %s\n version: %s' % (tushare.__author__, tushare.__version__))
    # print('History data of 600848 :\n%s' % tushare.get_hist_data('600848'))
    # print('All current stock trend:\n%s' % tushare.get_today_all())
    # print(tushare.get_today_all())

    df = tushare.get_tick_data('600036',date='2020-01-21',src='tt')
    print(df.head(10))

    df = tushare.get_index()
    print('大盘指数行情列表top20:\n%s' % df.head(20))