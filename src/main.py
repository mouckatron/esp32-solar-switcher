import relays
import time
import webserver

relayservice = relays.RelayService()
relayservice.switch_all(1)

webserver = webserver.Webserver({
    '/': webserver.HTMLPage('html/dashboard.html'),
    '/api/status': webserver.JSONAPI(relayservice.status),
    '/api/panel1/on':  webserver.Empty(lambda: str(relayservice.switch('panel1', 0))),
    '/api/panel1/off': webserver.Empty(lambda: str(relayservice.switch('panel1', 1))),
    '/api/panel2/on':  webserver.Empty(lambda: str(relayservice.switch('panel2', 0))),
    '/api/panel2/off': webserver.Empty(lambda: str(relayservice.switch('panel2', 1))),
    '/api/panel3/on':  webserver.Empty(lambda: str(relayservice.switch('panel3', 0))),
    '/api/panel3/off': webserver.Empty(lambda: str(relayservice.switch('panel3', 1))),
    '/api/panel4/on':  webserver.Empty(lambda: str(relayservice.switch('panel4', 0))),
    '/api/panel4/off': webserver.Empty(lambda: str(relayservice.switch('panel4', 1)))
})
print("Starting webserver")
webserver.start()
