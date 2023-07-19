import sys
import os
import re
import matplotlib.pyplot as plt

pattern_1 = r"(^Trace\b)(\s+)(\*+)(\w+)(\*+\|\*+)(\w+\s\w+)(\*+\|\*+)(\w+)(\*+)"
pattern_2 = r"(^../\w+/\d+\.)(\w+)(\S+)(\s+)(\w+\:\s)(\d+\.\d+)(\s\w+\:\s)(\d+\.\d+)(\s+\|\s)(\w+\:\s)(\d+\.\d+)(\s+\w+\:\s)(\d+\.\d+)(\s+\|\s)(\w+\s\w+\:\s)(\d+\.\d+)"
#dictry = os.listdir(sys.argv[1])
k = []
fl = sys.argv[1]

def plt_grp(fl_name):
    with open(fl_name,'r') as fl_h:
        for each in fl_h.readlines():
            pat1 = re.search(pattern_1,each)
            pat2 = re.search(pattern_2,each)
            if pat1:
                k.append(pat1.group(4))
                k.append(pat1.group(6))
                k.append(pat1.group(8))
                k[0] = []
                k[1] = []
                k[2] = []
                spec = []
            if pat2:
                spec.append(pat2.group(2))
                ipc_lru = float(pat2.group(8))
                k[0].append(ipc_lru)
                ipc_pol = float(pat2.group(13))
                k[1].append(ipc_pol)
                spd_up = float(pat2.group(16))
                k[2].append(spd_up)
        print(k[0])
        print(k[1])
        print(k[2])
        print(spec)
        plt.plot(spec,k[0], label = 'LRU')
        plt.plot(spec,k[1], label = 'CUSTOM POLICY')
        plt.plot(spec,k[2], label = 'SPEEDUP')
        plt.title("THE GRAPH")
        plt.xlabel('SPEC')
        plt.ylabel('IPC')
        plt.legend()
        print("WE ARE AT THIS POINT")
        plt.show()
        print("We ARE NOW AT THE END")



plt_grp(fl)

