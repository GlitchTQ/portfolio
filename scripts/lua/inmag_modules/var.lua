var = {}

-- Secondary functions --
--
function var.check(table, target)
-- Check for the presence of a value in a table.
  for key, val in pairs(table) do
    if val == target then
      return true
    end
  end
  return false
end

function var.formatting(exten)
-- Formating caller id for provider
  exten = string.sub(exten, 3)
    if string.sub(exten, 1, 1) == '8' then
      exten = '7'..string.sub(exten, 2)
    elseif string.sub(exten, 1, 1) == '7' then
      exten = exten -- DON`T ASK ME WHY!!!
    end
  return exten
end


return var
