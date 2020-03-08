#!/usr/bin/env python3

import sys, time
from conf.HectorConfig import config
from HectorHardware import HectorHardware

hardware = True

if hardware:
    h = HectorHardware(config)

print("REINIGUNG")
print("")

if hardware:
    h.light_on()
    time.sleep(1)
    #h.arm_out()

if True:
    vlist = range(12)
    valves = []
    print("Die folgenden Kanäle werden jetzt gereinigt:")
    for v in vlist:
        if v == "":
            continue
        i = int(v)
        print("  %d" % i)
        valves.append(i)
if hardware:
    h.pump_start()
    for i in range(1):
        print("STEP: " + str(i))
        for vnum in valves:
            print("Ventil %d wird geöffnet, Ende mit <Return>" % (vnum,))
            h.valve_open(vnum)
            time.sleep(180)
            h.valve_close(vnum)
    h.pump_stop()



