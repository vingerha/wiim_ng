![GitHub release (with filter)](https://img.shields.io/github/v/release/vingerha/wiim_ng)

This is a improved / extended integration for WiiM devices, based on the latest work in [the fork of m-stefanski](https://github.com/m-stefanski/home-assistant-custom-components-wiim-ng)

**Important** Home Assistant has a native integration [LinkPlay](https://www.home-assistant.io/integrations/linkplay) which will also work for WiiM devices to create a media_player. It however wil lliely (unclear) not comver WiiM specifics as this integration aims to achieve.

This integration allows you to control the WiiM Mini, Pro, Pro Plus and Amp devices from your [Home Assistant](http://www.home-assistant.io) smart home system. 

## Installation on Home Assistant (awaiting HACS acceptance)

- add this URL as a 'Custom Repository' to HACS (3-dots top right), then
- HACS > Integrations > WiiM ...download
- restart HA
- add your setup via Settings > Devices & Services, new integration; WiiM

### Configuration Settings

**host:**  
  *(string)* *(Required)* The IP address of the WiiM unit. Make sure it gets the same IP via static lease.

**name:**  
  *(string)* *(Required)* Name that Home Assistant will generate the `entity_id` based on. It is also the base of the friendly name seen in the dashboard, but will be overriden by the device name set in the smartphone WiiM app.

**uuid:**  
  *(string)* *(Optional)* Hardware UUID of the player. Can be read out from the attibutes of the entity. Set it manually to that value to handle double-added entity cases when Home Assistant starts up without the WiiM device being on the network at that moment.

### Configuration Options
Available after the device has been created 
**volume_step:**  
  *(integer)* *(Optional)* Step size in percent to change volume when calling `volume_up` or `volume_down` service against the media player. Defaults to `5`, can be a number between `1` and `25`.

## Gratitude goes out to the following authors/contributors
Parts of the integration were originally developed for LinkPlay devices by the following people
    "@nicjo814",
    "@limych",
    "@nagyrobi",
    "@onlyoneme",
    "@m-stefanski"
