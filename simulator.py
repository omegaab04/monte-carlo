import numpy as np

def monte_carlo_price(option, n_simulations=100000):
    Z = np.random.standard_normal(n_simulations)
    ST = option.S0 * np.exp((option.r - 0.5 * option.sigma**2) * option.T +
                            option.sigma * np.sqrt(option.T) * Z)

    if option.type == 'call':
        payoffs = np.maximum(ST - option.K, 0)
    else:
        payoffs = np.maximum(option.K - ST, 0)

    price = np.exp(-option.r * option.T) * np.mean(payoffs)
    return price