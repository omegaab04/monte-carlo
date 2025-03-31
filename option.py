class EuropeanOption:
    def __init__(self, S0, K, T, r, sigma, option_type='call'):
        self.S0 = S0          # Initial stock price
        self.K = K            # Strike price
        self.T = T            # Time to maturity
        self.r = r            # Risk-free rate
        self.sigma = sigma    # Volatility
        self.type = option_type  # 'call' or 'put'