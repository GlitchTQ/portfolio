C_OUT = {}

M_COMPANY     = '_XXXX'
RM_OUT        = '_918[3489]XXXXXXXXX'
RM_OUT_MTT    = '_938[3489]XXXXXXXXX'
LM_OUT        = '_928[3489]XXXXXXXXX'
M_OUT_RESERVE = '_948[3489]XXXXXXXXX'

C_OUT[M_COMPANY] = function(context, exten)
  call.company(context, exten)
end

C_OUT[RM_OUT] = function(context, exten)
  call.outgoingRBT(context, exten)
end

C_OUT[LM_OUT] = function(context, exten)
  call.outgoingLeran(context, exten)
end

return C_OUT
