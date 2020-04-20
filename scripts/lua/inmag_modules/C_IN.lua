package.path = package.path..';' .. '/etc/asterisk/lua.d/'..'?.lua'
require 'var'

C_IN = {}

C_IN['sipp']  = function(context, exten)
  local timestamp = os.time(os.date("!*t"))
  local unit = 'rbt'
  channel['UNIT']:set(unit)
  local cid = channel['CALLERID(num)']:get()
  channel['CALLERID(name)']:set('RBT-'..cid)
  macro.HExtensions(exten)
  macro.blacklist(exten)
  app.noop(channel['CHANNEL(state)']:get())
  call.ivr(exten)
end

C_IN['1599']  = function(context, exten)
  local timestamp = os.time(os.date("!*t"))
  local unit = 'rbt'
  channel['MARK']:set(timestamp)
  channel['SHARED(MARK)']:set(timestamp)
  channel['CDR(userfield)']:set(channel['MARK']:get())
  channel['UNIT']:set(unit)
  local cid = channel['CALLERID(num)']:get()
  channel['CALLERID(name)']:set('RBT-'..cid)
  macro.HExtensions(exten)
  macro.blacklist(exten)
  app.noop(channel['CHANNEL(state)']:get())
  call.ivr(exten)
end

C_IN['i'] = function(context, exten)
  local cid = channel['CALLERID(num)']:get()
  channel['CDR(userfield)']:set(channel['MARK']:get())
  if channel['UNIT']:get() == 'rbt' then
    call.queueRBT(context, exten)
  else
    call.queueLeran(context, exten)
  end
end

C_IN['t'] = function(context, exten)
  local cid = channel['CALLERID(num)']:get()
  channel['CDR(userfield)']:set(channel['MARK']:get())
  if channel['UNIT']:get() == 'rbt' then
    call.queueRBT(context, exten)
  else
    call.queueLeran(context, exten)
  end
end

C_IN['1'] = function(context, exten)
  local cid = channel['CALLERID(num)']:get()
  channel['CDR(userfield)']:set(channel['MARK']:get())
  if channel['UNIT']:get() == 'rbt' then
    channel['CDR(did)']:set('3250')
    app.Queue('salesman','nt','','','10')
    call.queueRBT(context, exten)
  else
    channel['CDR(did)']:set('3250')
    app.Queue('salesman_leran','nt','','','10')
    call.queueLeran(context, exten)
  end
end

return C_IN
