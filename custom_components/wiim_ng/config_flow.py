"""ConfigFlow for WiiM integration."""
from __future__ import annotations

import logging

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.config_entries import ConfigFlow, OptionsFlow
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import selector

from .const import *

_LOGGER = logging.getLogger(__name__)

CONFIG_FLOW_SCHEMA = vol.Schema({
    vol.Required(CONF_HOST): selector.TextSelector(),
    vol.Required(CONF_NAME): str,
    vol.Optional(CONF_UUID, default=""): str,
})
CONFIG_OPTIONS_SCHEMA = vol.Schema({
    vol.Optional(CONF_VOLUME_STEP, default=5): vol.All(int, vol.Range(min=1, max=25)),
})

@config_entries.HANDLERS.register(DOMAIN)
class WiiMConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=CONFIG_FLOW_SCHEMA, errors=errors
        )
        
    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Create the options flow."""
        return WiiMOptionsFlowHandler(config_entry)        

class WiiMOptionsFlowHandler(OptionsFlow):
    def __init__(self, config_entry) -> None:
        """Initialize options flow."""

    async def async_step_init(
        self, user_input: dict | None = None
    ) -> FlowResult:
        """Manage the options."""
        errors = {}
        if user_input is None:
            return self.async_show_form(
                step_id="init",
                data_schema=CONFIG_OPTIONS_SCHEMA,
                errors=errors
            ) 
            
        _LOGGER.debug(f"UserInputs Options Init: {user_input}")
        return self.async_create_entry(title="", data=user_input)   