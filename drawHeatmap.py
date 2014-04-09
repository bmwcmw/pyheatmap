# -*- coding: utf-8 -*-

import urllib
from pyheatmap.heatmap import HeatMap

def main(srcUrl, clkMap, heatMap, width, height):

    # url = "https://raw.github.com/oldj/pyheatmap/master/examples/test_data.txt"
    # sdata = urllib.urlopen(url).read().split("\n")
    # url = "D:/DEV/GitHub/Sokaris_View3D/Sokaris_View3D/IntersectionsHN.ini"
    sdata = open(srcUrl, 'r').read().split('\n')

    data = []
    for ln in sdata:
        a = ln.split(" ")
        if len(a) != 2:
            continue
        a = [int(i) for i in a]
        data.append(a)

    hm = HeatMap(data=data,width=width,height=height)
    hm.clickmap(save_as=clkMap)
    hm.heatmap(save_as=heatMap)

if __name__ == "__main__":
    print(" ************************************************* \n")
    print(" ************************************************* \n")
    print(" ****    Sokaris - HeatMap Generator 0.0.2    **** \n")
    print(" ************************************************* \n")
    print(" ************************************************* \n\n")
    print(" Je suis en train de travailler... \n\n")
    #while True :
    main(srcUrl="D:/DEV/GitHub/Sokaris_View3D/Debug/IntersectionsHN.ini", clkMap="hitHN.png", heatMap="D:/DEV/GitHub/Sokaris_View3D/Debug/texture/heatHN.png", width=613, height=300)
    main(srcUrl="D:/DEV/GitHub/Sokaris_View3D/Debug/IntersectionsHW.ini", clkMap="hitHW.png", heatMap="D:/DEV/GitHub/Sokaris_View3D/Debug/texture/heatHW.png", width=790, height=300)
    main(srcUrl="D:/DEV/GitHub/Sokaris_View3D/Debug/IntersectionsHS.ini", clkMap="hitHS.png", heatMap="D:/DEV/GitHub/Sokaris_View3D/Debug/texture/heatHS.png", width=613, height=300)
    main(srcUrl="D:/DEV/GitHub/Sokaris_View3D/Debug/IntersectionsHE.ini", clkMap="hitHE.png", heatMap="D:/DEV/GitHub/Sokaris_View3D/Debug/texture/heatHE.png", width=790, height=300)