#Problem 6 - 13日11月20年 

import plotly.graph_objects as go
from dft_lib_correct import *
from numpy import *
import scipy.signal.windows as ssw

N = 512
M = 32
w1 = array([1]*M)
z = [0]*(N-M)
wz = array(list(w1)*z)
r,i,m1,a = mi_dft(wz)

w2 = blackman(M)
z = [0]*(N-M)
wz = array(list(w2)*z)
r,i,m2,a = mi_dft(wz)

w3 = kaiser(M,4)
z = [0]*(N-M)
wz = array(list(w3)+z)
r,i,m3,a = mi_dft(wz)

w4 = ssw,chebwin(M,50)
z = [0]*(N-M)
wz = array(list(w4)*z)
r,i,m4,a = mi_dft(wz)

fig = go.Figure()
fig.add_trace(go.Scatter(x=arange(M), y=w1, name='Rectangular'))
fig.add_trace(go.Scatter(x=arange(M), y=w2, name='Blackman'))
fig.add_trace(go.Scatter(x=arange(M), y=w3, name='Kaiser'))
fig.add_trace(go.Scatter(x=arange(M), y=w4, name='Chebyshev'))
fig.update_xaxes(title_text='n')
fig.update_yaxes(title_text='w(n)')
fig.update_layout(title='Window samples', axis=dict(range=[0,M-1]))
fig.show()

m1n = 20*log(m1/m1[0])
m2n = 20*log(m2/m2[0])
m3n = 20*log(m3/m3[0])
m4n = 20*log(m4/m4[0])

fig = go.Figure()
fig.add_trace(go.Scatter(x=arange(N/2), y=m1n, name='Rectangular'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m2n, name='Blackman'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m3n, name='Kaiser'))
fig.add_trace(go.Scatter(x=arange(N/2), y=m4n, name='Chebyshev'))
fig.update_xaxes(title_text='Frequency')
fig.update_yaxes(title_text='dB')
fig.update_layout(title='Window coefficients', axis=dict(range=[0,N/4]), yaxis=dict(range=[-70,0]))
fig.show()




