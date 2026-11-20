import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    p = math.exp(-lam)
    cdf = p
    for i in range(1, k + 1):
        p *= lam / i
        cdf += p
    return {"pmf": float(p), "cdf": float(cdf)}