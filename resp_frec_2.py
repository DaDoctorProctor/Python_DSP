#Frequency response 03日11月20年

import plotly.graph_objects as go
from dft_lib_correct import *
from palitos2 import stem_plot
from numpy import *


n = arange(64)
xn = sin(2*pi*2*n/64)
hn = [1/5]*5 #Filter coefficiets.

#Move the signal to the frequency domain X(M).
N = 64
vec_zeros = zeros(N - len(hn))
hn_zeros = array(hn + list(vec_zeros)) #Fill H(N) with zeros for the 64 points.
n_zeros = arange(N)

rx,ix,mx,ax = mi_dft(xn)
e_xn = rx + ix * 1j

rh,ih,mh,ah = mi_dft(hn_zeros)
e_hn = rh + ih * 1j

e_yn = e_xn * e_hn

yn_r, yn_i = mi_idft(e_yn)

fig = go.Figure()
fig.add_traces(go.Scatter(x = n_zeros, y = xn))
fig.add_traces(go.Scatter(x = n_zeros, y = yn_r))
fig.show()

#fig = go.Figure()
#fig.add_traces(go.Scatter(x = n_zeros, y = xn))
#fig.add_traces(go.Scatter(x = n_zeros, y = yn_r))
#fig.show()

#Using convolution function

yn = convolve(xn, hn)

fig = go.Figure()
fig.add_traces(go.Scatter(x = n_zeros, y = xn))
fig.add_traces(go.Scatter(x = n_zeros, y = yn_r, color = 'firebrick'))
fig.show()

fig = go.Figure()
fig.add_traces(go.Scatter(x = n_zeros, y = xn))
fig.add_traces(go.Scatter(x = arange(len(yn)), y = yn, color = 'firebrick'))
fig.show()

#Using convolution DFT is better because it fixes de original error the signal
#brings to the table.









