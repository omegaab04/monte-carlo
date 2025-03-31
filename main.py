from option import EuropeanOption
from simulator import monte_carlo_price

# Create an instance of EuropeanOption
my_option = EuropeanOption(S0=100, K=105, T=1, r=0.05, sigma=0.2, option_type='call')
# Simulate the option price using Monte Carlo simulation
price = monte_carlo_price(my_option, n_simulations=100000)

print(f"Estimated Monte Carlo price of the {my_option.type} option: {price:.2f}")