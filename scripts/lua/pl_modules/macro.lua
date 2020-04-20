package.path = package.path..';' .. '/etc/asterisk/lua.d/'..'?.lua'
require 'var'
macro ={}

-- to H extensions
function macro.HExtensions(exten)
  if exten == 'h' then
    app.NoCDR()
    app.hangup()
  end
end

--Blacklist
function macro.blacklist(exten)
  local black = channel['BLACKLIST()']:get()
  if black == '1' then
    app.hangup(1)
  end
end

-- Recording call.
function macro.record(cid, exten)
  app.noop(string.format('Start recoding from %s to %s', cid, exten))
  local timestamp = string.format('%s.%s.%s.%s:%s:%s',
                                   os.date("*t")['year'], os.date("*t")['month'],
                                   os.date("*t")['day'], os.date("*t")['hour'],
                                   os.date("*t")['min'], os.date("*t")['sec'])
  local fname = string.format('%s-%s-%s-%s', channel['UNIQUEID']:get(),
                               timestamp, cid, exten)
  local year, month, day = os.date("%Y"), os.date("*t")['month'], os.date("%d")
  local row = string.format('%s/%s/%s/%s/%s', RDIR, year, month, day, fname)
  channel['CDR(filename)']:set(row)
  channel['CDR(realdst)']:set(exten)
  channel['CHANNEL(accountcode)']:set(exten)
  app.mixmonitor(string.format('%s.wav,b', row))
end

-- The phone state checkup.
function macro.dev_state(exten, state)
  if var.check(UDEV, state) then
    app.wait(1)
    app.playback('ru/followme/sorry')
    app.wait(1)
    app.hangup()
  elseif check(BUSY, state) then
    app.wait(1)
    app.playback('ru/all-circuits-busy-now')
    app.playback('ru/pls-try-call-later')
    app.wait(1)
    app.hangup()
  end
end

return macro
