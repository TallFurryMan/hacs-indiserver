from homeassistant.helpers.entity import Entity

async def async_setup_entry(hass, entry, async_add_entities):
    # ...existing code...
    async_add_entities([INDIServerSensor(entry)])

class INDIServerSensor(Entity):
    def __init__(self, entry):
        self._host = entry.data.get("host")
        self._port = entry.data.get("port")

    @property
    def name(self):
        return "INDI Server Sensor"

    @property
    def state(self):
        # ...existing code...
        return "unknown"

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port
