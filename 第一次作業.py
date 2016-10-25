# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
K=9100
Premium_Call=100
Premium_Put=40
Interval=500
ST=np.arange(K-Interval,K+Interval)

Buy_Call=(np.maximum(ST-K,0)-Premium_Call)
Short_Call=-(np.maximum(ST-K,0)-Premium_Call)
Buy_Put=(np.maximum(K-ST,0)-Premium_Put)
Short_Put=-(np.maximum(K-ST,0)-Premium_Put)

import matplotlib.pyplot as plt

BC=plt.plot(ST,Buy_Call)

SC=plt.plot(ST,Short_Call)

BP=plt.plot(ST,Short_Put)

SP=plt.plot(ST,Buy_Put)

BCSC=plt.plot(ST,Buy_Call+Short_Call)

BPSP=plt.plot(ST,Buy_Put+Short_Put)

BCBP=plt.plot(ST,Buy_Call+Buy_Put)

