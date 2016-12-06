"""
A python module for demonstrating head orientation tracking for binaural
synthesis

Usage: python opti_ssr_demo.py [SSR_IP] [SSR_port] [optitrack ip] [multicast address] [optitrack port] [end_message]
"""

import sys

import opti_network
import ssr_network
import opti_ssr

def demo(ssr_ip='139.30.207.123', ssr_port=4711, opti_ip=None, multicast_address='239.255.42.99', opti_port=1511, end_message='\0'):
    """ #todo

    Parameters
    ----------
    IP : str, optional
        IP of the server running thr SSR.
    port : int, optional
        Port of SSR Network Interface. By default, p
    end_message : str, optional
        Symbol to terminate the XML messages send to SSR. By default, a binary zero.

    """
    # setting arguments if executed in command line
    if sys.argv[1:]:
        ssr_ip = str(sys.argv[1])
    if sys.argv[2:]:
        ssr_port = int(sys.argv[2])
    if sys.argv[3:]:
        opti_ip = str(sys.argv[3])
    if sys.argv[4:]:
        multicast_address = str(sys.argv[4])
    if sys.argv[5:]:
        opti_port = str(sys.argv[5])
    if sys.argv[6:]:
        end_message = str(sys.argv[6])

    # instantiation of the necessary class objects
    optitrack = opti_network.opti_network(opti_ip, multicast_address, opti_port)
    ssr = ssr_network.ssr_network(ssr_ip, ssr_port, end_message)
    localwfs = opti_ssr.HeadTracker(optitrack, ssr)

    # creating sources once and continuously tracking position
    localwfs.start()

if __name__ == "__main__":
    demo()