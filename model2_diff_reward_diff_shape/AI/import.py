import numpy as np

xd = np.load('plot_data/iters{}.npz'.format("1370"))['arr_0']

print(xd.shape)
print(xd[5000-1])
print(sum(xd) % 5000)

