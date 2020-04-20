package.path = package.path..';' .. '/etc/asterisk/lua.d/'..'?.lua'
require 'macro'
require 'trunk'
in_call = {}

-- Internal call on the PBX
function in_call.local_call(context, exten)
  local cid = channel['CALLERID(num)']:get()
  local state = channel[string.format('DEVICE_STATE(SIP/%s)', exten)]:get()
  macro.dev_state(exten, state)
  macro.record(cid, exten)
  app.dial('SIP/'..exten, 60, 'tT')
  app.hangup()
end

-- Internal call to another unit in the Company.
function in_call.dundi(context, exten)
  local DUNDi = channel[string.format('DUNDILOOKUP(%s,priv)', exten)]:get()
  local cid = channel['CALLERID(num)']:get()
  macro.record(cid, exten)
  app.dial(string.format(DUNDi, 60, 'tT'))
end

-- Internal Company call.
function in_call.company(context, exten)
  local peer = channel[string.format('SIPPEER(%s,status)', exten)]:get()
  if peer ~= nill then
    in_call.local_call(context, exten)
  else
    in_call.dundi(context, exten)
  end
end

return in_call
