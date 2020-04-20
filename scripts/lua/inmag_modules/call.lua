package.path = package.path..';' .. '/etc/asterisk/lua.d/'..'?.lua'
require 'macro'
require 'var'

call ={}

-- Incoming logic.
function call.incoming(context, exten)
-- Some incoming call
  local cid = channel['CALLERID(num)']:get()
  macro.record(cid, exten)
  app.dial('SIP/1003', 45, 'T')
  app.Hangup()
end

function call.ivr(exten)
--IVR for XXX.RU shop
  local cid = channel['CALLERID(num)']:get()
  app.BackGround('you-sound-cute')
  app.WaitExten(3)
  app.Hangup()
  return
end


-- Outgoing logic
function call.outgoingXXX(context, exten)
-- Outgoing city calls for XXX.
  var.formatting(exten)
  local cid = channel['CALLERID(num)']:get()
  channel['CHANNEL(accountcode)']:set(cid)
  channel['CALLERID(all)']:set(RN_SPACETEL)
  macro.record(cid, exten)
  app.dial(T_SPACETEL..'/'..exten, 45, 'T')
end

function call.outgoingXXXXX(context, exten)
-- Outgoing city calls for XXXXX.
  var.formatting(exten)
  local cid = channel['CALLERID(num)']:get()
  channel['CHANNEL(accountcode)']:set(cid)
  channel['CALLERID(all)']:set(LN_SPACETEL)
  macro.record(cid, exten)
  app.dial(T_SPACETEL..'/'..exten, 45, 'T')
end

function call.local_call(context, exten)
-- Internal unit calls.
  local cid = channel['CALLERID(num)']:get()
  local state = channel[string.format('DEVICE_STATE(SIP/%s)', exten)]:get()
  macro.dev_state(exten, state)
  macro.record(cid, exten)
  app.dial('SIP/'..exten, 60, 'tT')
  app.hangup()
end

function call.dundi(context, exten)
-- Internal call to another unit in the Company.
  local DUNDi = channel[string.format('DUNDILOOKUP(%s,priv)', exten)]:get()
  local cid = channel['CALLERID(num)']:get()
  macro.record(cid, exten)
  app.dial(string.format(DUNDi, 60, 'tT'))
end

function call.company(context, exten)
-- Internal Company call.
  local peer = channel[string.format('SIPPEER(%s,status)', exten)]:get()
  if peer ~= nill then
    call.local_call(context, exten)
  else
    call.dundi(context, exten)
  end
end


-- Queue call logic.
function call.queueXXX(context, exten)
-- Call processing for XXX.RU shop.
  channel['CDR(did)']:set('3000')
  app.Queue('operator','nt','','','30')
  channel['CDR(did)']:set('3253')
  app.Queue('salesman2','nt','','','20')
  channel['CDR(did)']:set('3254')
  app.Queue('salesman3','nt','','','10')
  channel['CDR(did)']:set('3251')
  app.Queue('admin','nt','','','15')
  call.queueXXX(context, exten)
  app.Hangup()
end

function call.queueXXXXX(context, exten)
-- Call processing for XXXXX shop
  channel['CDR(did)']:set('3000')
  app.Queue('operator_leran','nt','','','30')
  channel['CDR(did)']:set('3253')
  app.Queue('salesman2_leran','nt','','','20')
  channel['CDR(did)']:set('3254')
  app.Queue('salesman3_leran','nt','','','10')
  channel['CDR(did)']:set('3251')
  app.Queue('admin_leran','nt','','','15')
  call.queueXXX(context, exten)
  app.Hangup()
end

return call
