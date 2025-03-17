from datetime import timedelta

DOMAIN = 'wiim_custom_ng'

ICON_DEFAULT = 'mdi:speaker'
ICON_PLAYING = 'mdi:speaker-wireless'
ICON_MUTED = 'mdi:speaker-off'
ICON_BLUETOOTH = 'mdi:speaker-bluetooth'
ICON_PUSHSTREAM = 'mdi:cast-audio'

ATTR_FWVER = 'firmware'
ATTR_DEVMODEL = 'device_model'
ATTR_PL_TRACKS = 'pl_tracks'
ATTR_PL_TRCRT = 'pl_track_current'
ATTR_TRCRT = 'track_current'
ATTR_STURI = 'stream_uri'
ATTR_UUID = 'uuid'
ATTR_DEBUG = 'debug_info'
ATTR_BITRATE = 'bit_rate'
ATTR_SAMPLERATE = 'sample_rate'
ATTR_DEPTH = 'bit_depth'
ATTR_FIXED_VOL = 'fixed_vol'
ATTR_SLAVE = 'slave'
ATTR_MASTER_UUID = 'master_uuid'
ATTR_ART_URL = 'art_url'
ATTR_SOUND_MODE = 'sound_mode'
ATTR_SOUND_MODE_LIST = 'sound_mode_list'


ATTR_CMD = 'command'
ATTR_NOTIFY = 'notify'
ATTR_URL = 'url'
ATTR_PRESET = 'preset'
ATTR_ALARM_NUMBER = 'alarm_number'
ATTR_ALARM_TRIGGER = 'alarm_trigger'
ATTR_ALARM_ACTION = 'alarm_action'
ATTR_ALARM_TIME = 'alarm_time'
ATTR_ALARM_DATE = 'alarm_date'
ATTR_ALARM_WEEKDAY = 'alarm_weekday'
ATTR_ALARM_MONTHDAY = 'alarm_monthday'
ATTR_ALARM_URL = 'alarm_url'
ATTR_AUDIO_OUTPUT_MODE = 'audio_output_mode'
ATTR_AUDIO_INPUT_MODE = 'audio_input_mode'



CONF_NAME = 'name'
CONF_HOST = 'host'
CONF_VOLUME_STEP = 'volume_step'
CONF_UUID = 'uuid'

DEFAULT_VOLUME_STEP = 5


DEBUGSTR_ATTR = True
MAX_VOL = 100

UPNP_TIMEOUT = 2
API_TIMEOUT = 2

UNA_THROTTLE = timedelta(seconds=20)
CONNECT_PAUSED_TIMEOUT = timedelta(seconds=300)
AUTOIDLE_STATE_TIMEOUT = timedelta(seconds=1)

MODEL_MAP = {'Muzo_Mini': 'WiiM Mini',
             'WiiM_Pro_with_gc4a': 'WiiM Pro',
             'WiiM_Pro_Plus': 'WiiM Pro Plus',
             'WiiM_AMP': 'WiiM Amp'}

SOURCES = {'line-in': 'Analog',
            'bluetooth': 'Bluetooth',
            'optical': 'Toslink',
            'udisk': 'USB',
            'network': 'Network',
            'third-dlna': 'DLNA',
            'squeezelite': 'Squeezelite',
            'airplay': 'Airplay',
            'roon': 'Roon',
            'HDMI': 'HDMI'}

SOURCES_MAP = {'-1': 'Idle', 
               '0': 'Idle', 
               '1': 'Airplay', 
               '2': 'DLNA',
               '3': 'Amazon',
               '4': '???',
               '5': 'Chromecast',
               '10': 'Network',
               '11': 'USB',
               '20': 'Network',			   
               '31': 'Spotify',
               '32': 'TIDAL',
               '33': 'Roon',
               '34': 'Squeezelite',
               '40': 'Analog',
               '41': 'Bluetooth',
               '43': 'Toslink',	
               '49': 'HDMI',			   
               '99': 'Idle'}

SOURCES_IDLE = ['-1', '0', '99']
SOURCES_LIVEIN = ['40', '41', '43', '49']
SOURCES_STREAM = ['1', '2', '3', '4', '5', '10', '20', '33', '34']
SOURCES_CONNECT = ['31', '32']

SERVICE_CMD = 'command'
SERVICE_PLAY_URL = 'play_url'
SERVICE_PRESET = 'preset'
SERVICE_ALARMCLOCK_SET  = 'alarmclock_set'
SERVICE_AUDIO_OUTPUT_MODE  = 'audio_output_set'
SERVICE_AUDIO_INPUT_MODE  = 'audio_input_set'

DEFAULT_SOUND_MODES = ["Flat", "Acoustic", "Bass Booster", "Bass Reducer", "Classical", "Dance", "Deep", "Electronic", 
"Hip-Hop", "Jazz", "Latin", "Loudness", "Lounge", "Piano", "Pop", "R&B", "Rock", "Small Speakers", "Spoken Word", "Treble Booster", "Treble Reducer", "Vocal Booster"] 

