digits = [1,2,3]

class soulution:
  def plusOne(self,digits):
    
    for i in range(len(digits)-1,-1,-1):
      if i == 0 and digits[i] == 9:
        digits[i] = 1
        digits.append(0)
      elif i > 0 and digits[i] == 9:
        digits[i] = 0
      else:
        digits[i] += 1
        break
    
    return digits
  
s = soulution()
result = s.plusOne(digits)
print(result)