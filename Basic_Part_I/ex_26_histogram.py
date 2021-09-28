import matplotlib.pyplot as plt
import numpy as np

def histogram():
    randomowe = np.random.normal(170,10,250)
    plt.hist(randomowe)
    return plt.show()



histogram()
