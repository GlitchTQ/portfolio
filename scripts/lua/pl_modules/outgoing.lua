package.path = package.path..';' .. '/etc/asterisk/lua.d/'..'?.lua'
require 'macro'
require 'trunk'

outgoing = {}

-- Outbound Call
function outgoing.call(context, exten)
  local cid = channel['CALLERID(num)']:get()
  channel['CALLERID(all)']:set(N_MTT)
  macro.record(cid, exten)
  app.dial(T_SPACETEL..'/'..exten, 45, 'T')
end

return outgoing
