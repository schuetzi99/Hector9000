# hardware configuration
# all pin numbers are corresponding to physical P1 connector!

config = {
    "hx711": {
        "CLK": 29,
        "DAT": 31,
        #"ref":  869.6761904761905 # calibration yields 100 g <-> readout 214500
        "ref":  450 # calibration yields 100 g <-> readout 214500
    },
    "pca9685": {
        "freq": 60,
        "valvechannels": range(12),  # 0..11
        "valvepositions": [  # (open, closed)
            (375, 535),  # ch 0
            (375, 560),  # ch 1
            (375, 545),  # ch 2
            (375, 575),  # ch 3
            (375, 580),  # ch 4
            (375, 550),  # ch 5
            (375, 545),  # ch 6
            (375, 555),  # ch 7
            (375, 535),  # ch 8
            (375, 555),  # ch 9
            (375, 550),  # ch 10
            (375, 560)  # ch 11
        ],
        "fingerchannel": 12,
        "fingerpositions": (280, 380, 430),  # retracted, above bell, bell
        "lightpin": 22,
        "lightpwmchannel": 13,
        "lightpositions": (0, 500)
    },
    "a4988": {
        "ENABLE": 11,
        "MS0": 13,
        "MS1": 15,
        "CONFIG": 19,
        "VREF": 21,
        "SLEEP": 23,
        "STEP": 35,
        "DIR": 33,
        "numSteps": 2600			# number of steps between IN and OUT positions
    },
    "arm": {
        "SENSE": 16
    },
    "pump": {
        "MOTOR": 18
    },
    "ws2812": {
        # D18
        "DIN": 12
    },
    "mqtt": {
        "SERVER": "localhost",
        "TOPICPREFIX": "Hector9000/Main/"
    }
}
