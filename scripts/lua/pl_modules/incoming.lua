package.path = package.path..';' .. '/etc/asterisk/lua.d/'..'?.lua'
require 'macro'
require 'trunk'

incoming = {}

-- Incoming Call
function incoming.call(context, exten)
  local cid = channel['CALLERID(num)']:get()
  app.noop(cid)
  macro.record(cid, exten)
  app.dial('SIP/101', 45, 'T')
end

return incoming
