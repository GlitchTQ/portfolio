-- Variables
package.path = package.path..';' .. '/etc/asterisk/lua.d/'..'?.lua'
require 'call'
require 'macro'
require 'var'
require 'C_QR'
require 'C_QL'
require 'C_OUT'
require 'C_IN'

RDIR          = '/monitor'

UDEV          = {'UNKNOWN', 'UNAVAILABLE', 'INVALID', 'NO ANSWER', 'CANCEL'}
BUSY          = {"INUSE", "BUSY", "RINGING", "RINGINUSE", "ONHOLD"}

M_COMPANY     = '_XXXX'
RM_OUT        = '_918[3489]XXXXXXXXX'
RM_OUT_MTT    = '_938[3489]XXXXXXXXX'
LM_OUT        = '_928[3489]XXXXXXXXX'
M_OUT_RESERVE = '_948[3489]XXXXXXXXX'

RN_SPACETEL   = '78006003900'
RN_MTT        = '78003333617'
LN_SPACETEL   = '78006002848'
LN_TTK        = '0007553755'

T_SPACETEL    = 'SIP/spacetel'
T_MTT         = 'SIP/mtt'
T_DOMRU       = 'SIP/domru'
-- Exten start. --
--
extensions            = {}
extensions.outgoing   = C_OUT
extensions.incoming   = C_IN
extensions.fromqueueR = C_QR
extensions.fromqueueL = C_QL
