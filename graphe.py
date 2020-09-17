import networkx as nx 
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv
import time

G = nx.DiGraph()

G.add_node("a")
G.add_node("b")
G.add_node("c")
G.add_node("d")
G.add_node("e")





print(G.nodes())

# here for GEXF format, we will have to change attribute etc 
c = 30
u = 0
for node in G.nodes():
    u += 1
    c+= int(50)
    G.nodes[node]["viz"] = {"size":200} 
    G.nodes[node]["viz"]["color"] = {"r": 200, "v": 0, "b" : 0}
    G.nodes[node]["viz"]["position"] = {"x": c+6*u , "y": c + 20*u, "z" : 0}

#G.nodes[0] = {"size":54}nodes[0][“viz”] = {“size”: 54} 
"""
f = plt.figure()
f.subplots_adjust(top=0.8)
ax1 = plt.axes([0, 0, 1, 1])
ax1 = f.add_subplot(211)
ax1.set_ylabel('volts')
ax1.set_title('a sine wave')
t = np.arange(0,10,1)
s = np.arange(0,10,1)
line, = ax1.plot(t, s, lw=2)
#pos = nx.spring_layout(G, pos = )
nx.draw_networkx_nodes(G,node_size=[x*100 for x in range(5)],pos = {"a" : (0,10), "b" : (10,200), "c" : (20,300), "d" : (30,400), "e" : (40,500)}, ax = ax1)
limits=plt.axis('on')
ax1.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

f.savefig('graph.png',bbox_inches='tight')"""
nx.write_gexf(G, "test.gexf")
