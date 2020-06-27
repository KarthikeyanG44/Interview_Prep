import numpy as np
x = [1,-1,3,4,5]
h = [2,3]

idx = 0

kerenel_len = len(h)
signal_len = len(x)

total_length = kerenel_len + signal_len - 1

y = np.zeros(total_length)

for i in range(signal_len):
    sum_local = 0
    for k in range(kerenel_len):
        sum_local += x[i+k]*h[kerenel_len-k]

    y[idx] = sum_local
