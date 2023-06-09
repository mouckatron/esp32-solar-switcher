from machine import Pin

class RelayService():

    def __init__(self):
        self._relays = {
            'panel1': Pin(16, Pin.OUT),
            'panel2': Pin(17, Pin.OUT),
            'panel3': Pin(18, Pin.OUT),
            'panel4': Pin(19, Pin.OUT)
            }

    def switch(self, relay, state):
        try:
            r = self._relays[relay]
        except KeyError:
            return False
        else:
            if state > 0:
                r.on()
            else:
                r.off()

    def switch_all(self, state):
        for r in self._relays:
            if state > 0:
                self._relays[r].on()
            else:
                self._relays[r].off()

    def status(self):
        return {
            'panel1': self._relays['panel1'].value(),
            'panel2': self._relays['panel2'].value(),
            'panel3': self._relays['panel3'].value(),
            'panel4': self._relays['panel4'].value()
            }
