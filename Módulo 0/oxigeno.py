

import numpy as np
import matplotlib.pyplot as plt


#data = np.random.default_rng(12345)
#oxy_nums = data.integers(low=0, high=100, size=100)


endVelocity = 11200
startVelocity = 0
acceleration = 9.8

time = (endVelocity - startVelocity) / acceleration
print("Tiempo para alcanzar la velocidad deseada = ", time)
#plt.bar(range((startVelocity)), endVelocity)
plt.plot(startVelocity,endVelocity )
plt.show()

