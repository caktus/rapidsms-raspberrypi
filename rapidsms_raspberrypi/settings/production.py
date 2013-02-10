from rapidsms_raspberrypi.settings.staging import *

# There should be only minor differences from staging

DATABASES['default']['NAME'] = 'rapidsms_raspberrypi_production'

EMAIL_SUBJECT_PREFIX = '[Rapidsms_Raspberrypi Prod] '

