import logging
import voluptuous as vol

from homeassistant.components.media_player.const import MediaType
from homeassistant.helpers import config_validation as cv, entity_registry as er
from homeassistant.const import ATTR_ENTITY_ID, ATTR_DEVICE_ID
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import *
from .media_player import WiiMData, WiiMDevice

_LOGGER = logging.getLogger(__name__)

# List the platforms that your integration supports.
PLATFORMS = ["media_player"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the WiiM integration from a config entry."""
    # Create integration-level data storage if it doesn't exist.
    hass.data.setdefault(DOMAIN, {})

    # (Optional) Store a shared instance of your global data object.
    hass.data[DOMAIN]["data"] = WiiMData()
       
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    return unload_ok


