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
    r_central = net.addHost('r_central', cls=Node, ip='0.0.0.0')
    r_central.cmd('sysctl -w net.ipv4.ip_forward=1')
    s_w_dep1 = net.addSwitch('s_w_dep1', cls=OVSKernelSwitch, failMode='standalone')
    s_w_dep2 = net.addSwitch('s_w_dep2', cls=OVSKernelSwitch, failMode='standalone')
    s_w_dep3 = net.addSwitch('s_w_dep3', cls=OVSKernelSwitch, failMode='standalone')
    s_w_dep4 = net.addSwitch('s_w_dep4', cls=OVSKernelSwitch, failMode='standalone')
    s_w_dep5 = net.addSwitch('s_w_dep5', cls=OVSKernelSwitch, failMode='standalone')
    r_dep1 = net.addHost('r_dep1', cls=Node, ip='0.0.0.0')
    r_dep1.cmd('sysctl -w net.ipv4.ip_forward=1')
    r_dep2 = net.addHost('r_dep2', cls=Node, ip='0.0.0.0')
    r_dep2.cmd('sysctl -w net.ipv4.ip_forward=1')
    r_dep3 = net.addHost('r_dep3', cls=Node, ip='0.0.0.0')
    r_dep3.cmd('sysctl -w net.ipv4.ip_forward=1')
    r_dep4 = net.addHost('r_dep4', cls=Node, ip='0.0.0.0')
    r_dep4.cmd('sysctl -w net.ipv4.ip_forward=1')
    r_dep5 = net.addHost('r_dep5', cls=Node, ip='0.0.0.0')
    r_dep5.cmd('sysctl -w net.ipv4.ip_forward=1')
    s_l_dep1 = net.addSwitch('s_l_dep1', cls=OVSKernelSwitch, failMode='standalone')
    s_l_dep2 = net.addSwitch('s_l_dep2', cls=OVSKernelSwitch, failMode='standalone')
    s_l_dep3 = net.addSwitch('s_l_dep3', cls=OVSKernelSwitch, failMode='standalone')
    s_l_dep4 = net.addSwitch('s_l_dep4', cls=OVSKernelSwitch, failMode='standalone')
    s_l_dep5 = net.addSwitch('s_l_dep5', cls=OVSKernelSwitch, failMode='standalone')
    r_dep1_esc1 = net.addHost('r_dep1_esc1', cls=Node, ip='0.0.0.0')
    r_dep1_esc1.cmd('sysctl -w net.ipv4.ip_forward=1')
    r_dep1_esc2 = net.addHost('r_dep1_esc2', cls=Node, ip='0.0.0.0')
    r_dep1_esc2.cmd('sysctl -w net.ipv4.ip_forward=1')
    r_dep1_esc3 = net.addHost('r_dep1_esc3', cls=Node, ip='0.0.0.0')
    r_dep1_esc3.cmd('sysctl -w net.ipv4.ip_forward=1')

    info( '*** Add hosts\n')
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)

    info( '*** Add links\n')

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s_w_dep1').start([])
    net.get('s_w_dep2').start([])
    net.get('s_w_dep3').start([])
    net.get('s_w_dep4').start([])
    net.get('s_w_dep5').start([])
    net.get('s_l_dep1').start([])
    net.get('s_l_dep2').start([])
    net.get('s_l_dep3').start([])
    net.get('s_l_dep4').start([])
    net.get('s_l_dep5').start([])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

