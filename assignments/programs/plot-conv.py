import pprint
import numpy as np
import scipy.linalg as la
import matplotlib.pylab as plt

r_laplace50 = [50,
               173.205,
               91.0492,
               75.0106,
               68.1489,
               62.5463,
               60.7533,
               58.6344,
               57.9244,
               56.5346,
               56.2508,
               55.2048,
               55.1348,
               54.2765,
               54.3253,
               53.5791,
               53.6986,
               53.0239,
               53.1877,
               52.5609,
               52.7534,
               52.1603,
               52.3719,
               51.8032,
               52.0279,
               51.4777,
               51.7113,
               51.1754,
               51.4153,
               50.8908,
               51.1351,
               50.6199,
               50.8672,
               50.3599,
               50.6093,
               50.1086,
               50.3594,
               49.8645,
               50.1162,
               49.6264,
               49.8786,
               49.3935,
               49.6459,
               49.165,
               49.4173,
               48.9404,
               49.1925,
               48.7192,
               48.971,
               48.5011]

r_laplace100 = [100,
                494.975,
                254.361,
                197.204,
                175.707,
                159.099,
                148.655,
                144.674,
                138.599,
                136.78,
                132.471,
                131.734,
                128.395,
                128.275,
                125.523,
                125.783,
                123.411,
                123.917,
                121.803,
                122.474,
                120.541,
                121.328,
                119.527,
                120.395,
                118.692,
                119.62,
                117.992,
                118.964,
                117.394,
                118.399,
                116.875,
                117.905,
                116.417,
                117.467,
                116.009,
                117.073,
                115.639,
                116.715,
                115.302,
                116.386,
                114.991,
                116.082,
                114.702,
                115.798,
                114.43,
                115.531,
                114.174,
                115.277,
                113.93,
                115.036]

x=np.array(range(1,51))
y=150./x
plt.loglog(x,r_laplace50,'b', label='n=50, 2D Laplace')
plt.loglog(x,r_laplace100,'r', label='n=100, 2D Laplace')
plt.loglog(x,y,'g', label='linear convergence')
plt.legend()
plt.title("Steepest decent convergence of residual")
plt.xlabel("iterations")
plt.ylabel("residual")
plt.show()


