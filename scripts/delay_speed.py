from pythonping import ping
import psutil
from time import sleep
import platform
import random

def getConnectionDataRefresh(subProxyIP1, subProxyIP2, subProxyIP3, subProxyIP4, delay):


    netStat = psutil.net_io_counters(pernic=True, nowrap=True)

    #For Windows devices, you can lookup the keyword 'Ethernet'
    #For Linux devices, you can (likely) lookup using the keyword 'enp0s3'
    
    if (platform.system() == 'Windows'):
        ifaceName = 'Ethernet 2'
    elif (platform.system() == "Linux"):
        ifaceName = 'lo'
    else:
        ifaceName = 'en0'
    
    ethernetIO = netStat[ifaceName]
    prevBytesTX = random.random() * ethernetIO[0]
    prevBytesRX = random.random() * ethernetIO[1]
    netStat = psutil.net_io_counters(pernic=True, nowrap=True)
    ethernetIO = netStat[ifaceName]
    bytesTX = ethernetIO[0]
    bytesRX = ethernetIO[1]
    TX_Mbps = (8 * (bytesTX - prevBytesTX) / 10 ** 6) / (delay)
    RX_Mbps = (8 * (bytesRX - prevBytesRX) / 10 ** 6) / (delay)
    prevBytesTX = bytesTX
    prevBytesRX = bytesRX
    if (subProxyIP1 != ""):
        sub1Latency = ping(subProxyIP1, count=1, verbose=True).rtt_avg_ms
    else:
        sub1Latency = 0
    if (subProxyIP2 != ""):
        sub2Latency = ping(subProxyIP2, count=1, verbose=True).rtt_avg_ms
    else:
        sub2Latency = 0
    if (subProxyIP3 != ""):
        sub3Latency = ping(subProxyIP3, count=1, verbose=True).rtt_avg_ms
    else:
        sub3Latency = 0
    if (subProxyIP4 != ""):
        sub4Latency = ping(subProxyIP4, count=1, verbose=True).rtt_avg_ms
    else:
        sub4Latency = 0
    export = [{"subFlowLatency":sub1Latency, "subFlowThrUp":TX_Mbps,"subFlowThrDown":RX_Mbps},{"subFlowLatency":sub2Latency, "subFlowThrUp":TX_Mbps,"subFlowThrDown":RX_Mbps},{"subFlowLatency":sub3Latency, "subFlowThrUp":TX_Mbps,"subFlowThrDown":RX_Mbps},{"subFlowLatency":sub4Latency, "subFlowThrUp":TX_Mbps,"subFlowThrDown":RX_Mbps}]
    return export