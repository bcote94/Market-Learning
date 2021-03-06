from datetime import datetime, timedelta

EQUITY_LOOKBACK = 10
ETF_LOOKBACK = 180
PREDICTION_WINDOW = 20
YEARS_LOOKBACK = 10

CURRENT_MONTH = datetime.now().month
CURRENT_DAY = datetime.now().day
CURRENT_YEAR = datetime.now().year
CURRENT_DATETIME = datetime(CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY)
START_DATETIME = CURRENT_DATETIME - timedelta(YEARS_LOOKBACK * 365)

SCORING = 'average_precision'
MODEL_PATH = '/Users/brian/PycharmProjects/Market-Learning/models/'
MODEL_VARIABLES = ['slow_stochastic_%K', 'fast_stochastic_%D', 'williams_%R', 'price_difference', 'price_ROC',
                   'RSI', 'ATR', 'average_price_volatility', 'disparity_index', 'MACD', 'on_balance_volume', 'label']

MULT12 = 2 / 13
MULT26 = 2 / 27

CV_PARAMS = {'cv': 5,
             'scoring': 'precision',
             'n_iter': 100}
