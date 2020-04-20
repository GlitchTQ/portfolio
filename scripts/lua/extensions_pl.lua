package.path = package.path..';' .. '/etc/asterisk/lua.d/'..'?.lua'
require 'in_call'
require 'macro'
require 'incoming'
require 'outgoing'
require 'var'
require 'trunk'

-- Variables
RDIR        = '/monitor'

UDEV        = {'UNKNOWN', 'UNAVAILABLE', 'INVALID'}
BUSY        = {"INUSE", "BUSY", "RINGING", "RINGINUSE", "ONHOLD"}

M_COMPANY   = '_XXXX'
M_CITY      = '_[27]XXXXXX'
M_CITY_9    = '_9[27]XXXXXX'
M_COUNTRY   = '_8[3489]XXXXXXXXX'
M_COUNTRY_9 = '_98[3489]XXXXXXXXX'


-- Assign Contexts --
--
extensions.TEST[M_COMPANY] = function(context, exten)
  company(context, exten)
end

extensions.TEST[M_COUNTRY] = function(context, exten)
  city_call(context, exten)
end
extensions.TEST[M_COUNTRY_9] = function(context, exten)
  city_call(context, exten)
end
extensions.TEST[M_CITY_9] = function(context, exten)
  city_call(context, exten)
end
extensions.TEST[M_CITY] = function(context, exten)
  city_call(context, exten)
end
