import numpy as np

# input
F=list(map(float,input().split()))
a=list(map(float,input().split()))
print()

# consts
g=9.8

# your code

# 3. & 4.
# We use polyfit to find the linear trend of 'a' vs 'F'.
p, pcov = np.polyfit(F, a, 1, cov=True)

# From the equation: a = (1/m)*F - mu*g
# The intercept p[1] is equal to -mu*g
mu_raw = -p[1] / g

# The variance of the intercept is pcov[1, 1].
DELTA_mu_raw = np.sqrt(pcov[1, 1]) / g

# 5.
# Rounding DELTA_mu to 1 significant figure.
power = -int(np.floor(np.log10(np.abs(DELTA_mu_raw))))
DELTA_mu = round(DELTA_mu_raw, power)

# Rounding mu to the same decimal place as DELTA_mu.
mu = round(mu_raw, power)


## output
print(f'{mu}\n{DELTA_mu}')