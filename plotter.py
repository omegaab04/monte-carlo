import matplotlib.pyplot as plt

def plot_terminal_prices(ST):
    plt.hist(ST, bins=50, alpha=0.7)
    plt.title("Distribution of Simulated Final Stock Prices")
    plt.xlabel("Stock Price at Maturity")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()