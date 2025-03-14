from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from .const import DOMAIN, DEFAULT_PORT
import re

HOST_REGEX = re.compile(
    r"^(?:(?:[a-zA-Z0-9-]{1,63}\.)+(?:[a-zA-Z]{2,63})|"
    r"(?:(?:[0-9]{1,3}\.){3}[0-9]{1,3}))$"
)

class INDIServerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            host = user_input.get("host")
            port = user_input.get("port")

            if not HOST_REGEX.match(host):
                errors["host"] = "invalid_host"
            elif not (1024 <= port <= 65535):
                errors["port"] = "invalid_port"
            else:
                return self.async_create_entry(title="INDI Server", data=user_input)

        data_schema = vol.Schema({
            vol.Required("host"): str,
            vol.Optional("port", default=DEFAULT_PORT): int,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
