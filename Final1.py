#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    swd1 = net.addSwitch('swd1', cls=OVSKernelSwitch, failMode='standalone')
    rcentral = net.addHost('rcentral', cls=Node, ip='0.0.0.0')
    rcentral.cmd('sysctl -w net.ipv4.ip_forward=1')
    swd2 = net.addSwitch('swd2', cls=OVSKernelSwitch, failMode='standalone')
    swd3 = net.addSwitch('swd3', cls=OVSKernelSwitch, failMode='standalone')
    swd4 = net.addSwitch('swd4', cls=OVSKernelSwitch, failMode='standalone')
    swd5 = net.addSwitch('swd5', cls=OVSKernelSwitch, failMode='standalone')
    rd1 = net.addHost('rd1', cls=Node, ip='0.0.0.0')
    rd1.cmd('sysctl -w net.ipv4.ip_forward=1')
    rd2 = net.addHost('rd2', cls=Node, ip='0.0.0.0')
    rd2.cmd('sysctl -w net.ipv4.ip_forward=1')
    rd3 = net.addHost('rd3', cls=Node, ip='0.0.0.0')
    rd3.cmd('sysctl -w net.ipv4.ip_forward=1')
    rd4 = net.addHost('rd4', cls=Node, ip='0.0.0.0')
    rd4.cmd('sysctl -w net.ipv4.ip_forward=1')
    rd5 = net.addHost('rd5', cls=Node, ip='0.0.0.0')
    rd5.cmd('sysctl -w net.ipv4.ip_forward=1')
    sld1 = net.addSwitch('sld1', cls=OVSKernelSwitch, failMode='standalone')
    sld2 = net.addSwitch('sld2', cls=OVSKernelSwitch, failMode='standalone')
    sld3 = net.addSwitch('sld3', cls=OVSKernelSwitch, failMode='standalone')
    sld4 = net.addSwitch('sld4', cls=OVSKernelSwitch, failMode='standalone')
    sld5 = net.addSwitch('sld5', cls=OVSKernelSwitch, failMode='standalone')
    rd1_e1 = net.addHost('rd1_e1', cls=Node, ip='0.0.0.0')
    rd1_e1.cmd('sysctl -w net.ipv4.ip_forward=1')
    rd1_e2 = net.addHost('rd1_e2', cls=Node, ip='0.0.0.0')
    rd1_e2.cmd('sysctl -w net.ipv4.ip_forward=1')
    rd1_e3 = net.addHost('rd1_e3', cls=Node, ip='0.0.0.0')
    rd1_e3.cmd('sysctl -w net.ipv4.ip_forward=1')
    sld1_e1 = net.addSwitch('sld1_e1', cls=OVSKernelSwitch, failMode='standalone')
    sld1_e2 = net.addSwitch('sld1_e2', cls=OVSKernelSwitch, failMode='standalone')
    sld1_e3 = net.addSwitch('sld1_e3', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    h1_e3 = net.addHost('h1_e3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h1_d1 = net.addHost('h1_d1', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h1_e2 = net.addHost('h1_e2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h1_e1 = net.addHost('h1_e1', cls=Host, ip='10.0.0.1', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(rcentral, swd1)
    net.addLink(rcentral, swd2)
    net.addLink(rcentral, swd3)
    net.addLink(rcentral, swd4)
    net.addLink(rcentral, swd5)
    net.addLink(swd1, rd1)
    net.addLink(swd2, rd2)
    net.addLink(swd3, rd3)
    net.addLink(swd4, rd4)
    net.addLink(swd5, rd5)
    net.addLink(rd1, sld1)
    net.addLink(rd2, sld2)
    net.addLink(rd3, sld3)
    net.addLink(rd4, sld4)
    net.addLink(rd5, sld5)
    net.addLink(sld1, rd1_e1)
    net.addLink(sld1, rd1_e2)
    net.addLink(sld1, rd1_e3)
    net.addLink(sld1, h1_d1)
    net.addLink(rd1_e1, sld1_e3)
    net.addLink(rd1_e2, sld1_e2)
    net.addLink(rd1_e3, sld1_e1)
    net.addLink(sld1_e3, h1_e1)
    net.addLink(sld1_e2, h1_e2)
    net.addLink(sld1_e1, h1_e3)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('sld2').start([])
    net.get('sld1_e2').start([])
    net.get('sld1').start([])
    net.get('sld4').start([])
    net.get('sld1_e1').start([])
    net.get('swd3').start([])
    net.get('swd2').start([])
    net.get('sld1_e3').start([])
    net.get('swd4').start([])
    net.get('sld5').start([])
    net.get('sld3').start([])
    net.get('swd5').start([])
    net.get('swd1').start([])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

