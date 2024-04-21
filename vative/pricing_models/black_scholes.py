import numpy as np
import scipy.stats as si


def black_scholes(S: float, K: float, T: float, r: float, sigma: float, option_type: str = "call") -> float:
    """
    Calculate the price of a European call or put option using the Black-Scholes model.

    S: float - initial stock price
    K: float - strike price
    T: float - time to maturity (in years)
    r: float - risk-free interest rate (annualized)
    sigma: float - volatility of the underlying stock (annualized)
    option_type: str - "call" for a call option or "put" for a put option
    """

    # Calculate d1 and d2
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        # Calculate the call option price
        call_price = S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0)
        return call_price
    elif option_type == "put":
        # Calculate the put option price
        put_price = K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0)
        return put_price
    else:
        raise ValueError("Option type must be 'call' or 'put'.")
