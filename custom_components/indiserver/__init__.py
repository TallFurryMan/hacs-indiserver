from homeassistant.core import HomeAssistant

DOMAIN = "indiserver"

async def async_setup(hass: HomeAssistant, config: dict):
    # ...existing code...
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    # This function sets up the integration based on the configuration entry.
    # Initialize components, add entities, and handle configuration data here.
    # ...existing code...
    return True

async def async_unload_entry(hass: HomeAssistant, entry):
    # ...existing code...
    return True
