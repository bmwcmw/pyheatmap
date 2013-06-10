# -*- coding: utf-8 -*-

import urllib
from pyheatmap.heatmap import HeatMap

def main():

    # url = "https://raw.github.com/oldj/pyheatmap/master/examples/test_data.txt"
    # sdata = urllib.urlopen(url).read().split("\n")
    url = "D:/DEV/GitHub/Sokaris_View3D/Sokaris_View3D/IntersectionsHN.ini"
    sdata = open(url, 'r').read().split('\n')

    data = []
    for ln in sdata:
        a = ln.split(" ")
        if len(a) != 2:
            continue
        a = [int(i) for i in a]
        data.append(a)

    hm = HeatMap(data)
    hm.clickmap(save_as="hit.png")
    hm.heatmap(save_as="heat.png")

if __name__ == "__main__":
    print(" ************************************************* \n")
    print(" ************************************************* \n")
    print(" ****    Sokaris - HeatMap Generator 0.0.1    **** \n")
    print(" ************************************************* \n")
    print(" ************************************************* \n\n")
    print(" Je suis en train de travailler... \n\n")
    while True :
        main()