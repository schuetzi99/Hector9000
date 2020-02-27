#!/usr/bin/env python3
# -*- coding: utf8 -*-
##
#   HectorAPI.py       API interface class for Hector9000 hardware
#

import abc


def debugOut(name, value):
    print("=> %s: %d" % (name, value))


class HectorAPI(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, cfg):
        pass

    @abc.abstractmethod
    def light_on(self):
        pass

    @abc.abstractmethod
    def light_off(self):
        pass

    @abc.abstractmethod
    def arm_out(self, cback=debugOut):
        pass

    @abc.abstractmethod
    def arm_in(self, cback=debugOut):
        pass

    @abc.abstractmethod
    def arm_isInOutPos(self):
        return false

    @abc.abstractmethod
    def scale_readout(self):
        return 0

    @abc.abstractmethod
    def scale_tare(self):
        pass

    @abc.abstractmethod
    def pump_start(self):
        pass

    @abc.abstractmethod
    def pump_stop(self):
        pass

    @abc.abstractmethod
    def valve_open(self, index, open=1):
        pass

    @abc.abstractmethod
    def valve_close(self, index):
        pass

    @abc.abstractmethod
    def valve_dose(self, index, amount, timeout=30, cback=debugOut, progress=(0,100), topic=""):
        return 0

    @abc.abstractmethod
    def finger(self, pos=0):
        pass

    @abc.abstractmethod
    def ping(self, num, retract=True, cback=None):
        pass

    @abc.abstractmethod
    def cleanAndExit(self):
        pass
