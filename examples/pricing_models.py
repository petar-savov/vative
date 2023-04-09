from vative.pricing_models.black_scholes import black_scholes


call_price = black_scholes(S=100, K=110, T=1, r=0.05, sigma=0.25, option_type="call")
print("Call option price:", call_price)

put_price = black_scholes(S=100, K=110, T=1, r=0.05, sigma=0.25, option_type="put")
print("Put option price:", put_price)
