from mininet.topo import Topo
from mininet.net import Mininet
net=Mininet()
#Creating nodes in the network
c0=net.addController()
h0=net.addHost('h0')
s0=net.addSwitch('s0')
h1=net.addHost('h1')
#
net.addLink(h0,s0)
net.addLink(h1,s0)
#
net.start()
net.pingAll()
net.stop()
