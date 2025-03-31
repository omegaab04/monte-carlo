# Monte Carlo Pricing of European Options

This simple project simulates the pricing of European call and put options using the Monte Carlo method.

## Files:
- `option.py` – Defines option parameters
- `simulator.py` – Runs Monte Carlo simulations
- `main.py` – Runs the simulation and prints the price
- `plotter.py` – (Optional) Visualizes simulated data

## How to Run
```bash
python main.py
```
In the main file, you can change between a call option simulation
```
my_option = EuropeanOption(S0=100, K=105, T=1, r=0.05, sigma=0.2, option_type='call')
```
or a put option simulation

```
my_option = EuropeanOption(S0=100, K=105, T=1, r=0.05, sigma=0.2, option_type='put')
```
If you still can't see what to change, it's the ```option_type = 'call'``` part. 
