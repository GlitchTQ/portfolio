var = {}

function var.check(table, target)
  for key, val in pairs(table) do
    if val == target then
      return true
    end
  end
  return false
end

var.T_01 = 'SIP/2393901'
var.T_02 = 'SIP/2393902'
var.T_03 = 'SIP/2393903'
var.T_04 = 'SIP/2393904'
var.T_05 = 'SIP/2393905'

return var
