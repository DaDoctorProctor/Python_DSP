
import plotly.graph_objects as go
from dft_lib_correct import *
from palitos2 import stem_plot
from numpy import *
import matplotlib.pyplot as plt

hn1 = [0.2, 0.2, 0.2, 0.2, 0.2]
hn2 = [0.1, 0.2, 0.2, 0.2, 0.1]
hn3 = [0.04, 0.12, 0.2, 0.12, 0.04]

N = 512
v_zeros = [0]*507
hn1_zeros = array(hn1 + v_zeros)
hn2_zeros = array(hn2 + v_zeros)
hn3_zeros = array(hn3 + v_zeros)

r1,i1,m1,a1 = mi_dft(hn1_zeros)
e1 = r1 + i1*1j
r2,i2,m2,a2 = mi_dft(hn2_zeros)
e2 = r2 + i2*1j
r3,i3,m3,a3 = mi_dft(hn3_zeros)
e3 = r3 + i3*1j

e1 = e1/e1[0]
e2 = e2/e2[0]
e3 = e3/e3[0]

m1 = sqrt(e1.real**2 + e1.imag**2)
m2 = sqrt(e2.real**2 + e2.imag**2)
m3 = sqrt(e3.real**2 + e3.imag**2)

fig = go.Figure()
fig.add_traces(go.Scatter(x=arange(N/2), y=m1, name='[H1(m)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=m2, name='[H2(m)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=m3, name='[H3(m)]'))
#fig.show()

n = arange(N)

plt.figure()
plt.plot(n, m1)
plt.plot(n, m2)
plt.plot(n, m3)
plt.xlim(n[0],n[250])
plt.legend()
plt.show()

xn = [10, 22, 24, 37, 77, 89, 22, 63, 9, 52, 31, 48, 53, 29, 14, 47, 38, 70]
v_zeros = [0]*(512-len(xn))
xn_zeros = array(xn + v_zeros)

r4,i4,m4,a4 = mi_dft(xn_zeros)
e4 = r4 + i4*1j

xn_hn1 = e1*e4
xn_hn2 = e2*e4
xn_hn3 = e3*e4

m5 = sqrt(xn_hn1.real**2 + xn_hn1.imag**2)
m6 = sqrt(xn_hn2.real**2 + xn_hn2.imag**2)
m7 = sqrt(xn_hn3.real**2 + xn_hn3.imag**2)

fig = go.Figure()
fig.add_traces(go.Scatter(x=arange(N/2), y=m4/m4[0], name='[X(m)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=m1, name='[H1(m)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=m5/m5[0], name='[Y1(m)]'))
fig.show()

fig = go.Figure()
fig.add_traces(go.Scatter(x=arange(N/2), y=m4/m4[0], name='[X(m)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=m2, name='[H1(m)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=m6/m6[0], name='[Y2(m)]'))
fig.show()

fig = go.Figure()
fig.add_traces(go.Scatter(x=arange(N/2), y=m4/m4[0], name='[X(m)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=m3, name='[H1(m)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=m7/m7[0], name='[Y3(m)]'))
fig.show()

fig = go.Figure()
fig.add_traces(go.Scatter(x=arange(N/2), y=m5, name='[Y1(m)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=m6, name='[Y2(m)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=m7, name='[Y3(m)]'))
fig.show()

yn1, x = mi_idft(xn_hn1)
yn2, x = mi_idft(xn_hn2)
yn3, x = mi_idft(xn_hn3)

fig = go.Figure()
fig.add_traces(go.Scatter(x=arange(N/2), y=xn, name='[x(n)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=yn1, name='[Y1(n)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=yn2, name='[Y2(n)]'))
fig.add_traces(go.Scatter(x=arange(N/2), y=yn3, name='[Y3(n)]'))
fig.update_layout(xaxis=dict(range=[0,20]))
fig.show()