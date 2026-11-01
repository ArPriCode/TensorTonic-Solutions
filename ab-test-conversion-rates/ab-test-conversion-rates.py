import math
from statistics import NormalDist

def ab_test_conversion(control_conversions: int, control_n: int, treatment_conversions: int, treatment_n: int, alpha: float = 0.05) -> dict:
    p_c = control_conversions / control_n
    p_t = treatment_conversions / treatment_n
    lift = p_t - p_c
    
    p_pooled = (control_conversions + treatment_conversions) / (control_n + treatment_n)
    se_pooled = math.sqrt(p_pooled * (1 - p_pooled) * (1 / control_n + 1 / treatment_n))
    
    if se_pooled == 0:
        z = 0.0
        p_val = 1.0
    else:
        z = lift / se_pooled
        p_val = math.erfc(abs(z) / math.sqrt(2))
        
    se_unpooled = math.sqrt((p_c * (1 - p_c) / control_n) + (p_t * (1 - p_t) / treatment_n))
    z_crit = NormalDist().inv_cdf(1 - alpha / 2)
    
    ci_low = lift - z_crit * se_unpooled
    ci_high = lift + z_crit * se_unpooled
    
    return {
        "lift": lift,
        "z": z,
        "p_value": p_val,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "significant": p_val < alpha
    }