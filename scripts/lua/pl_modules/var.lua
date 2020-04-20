var = {}

-- Secondary functions --
--
-- Check for the presence of a value in a table.
function var.check(table, target)
  for key, val in pairs(table) do
    if val == target then
      return true
    end
  end
  return false
end

function var.formatting(exten)
-- Formating caller id for provider
  if #exten == 11 then
    if string.sub(exten, 1, 1) == '8' then
      exten = '7'..string.sub(exten, 2)
    elseif string.sub(exten, 1, 1) == '7' then
      exten = exten -- DO NOT ASK ME!!!
    end
  elseif #exten == 12 then
    if string.sub(exten, 1, 2) == '98' then
      exten = '7'..string.sub(exten, 3)
    elseif string.sub(exten, 1, 2) == '97' then
      exten = string.sub(exten, 2)
    end
  end
  return exten
end

return var
