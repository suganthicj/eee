def multiplyFactors(n) : 
    prod = 1
      
    i = 1
    while i * i <= n : 
        if (n % i == 0) : 
              
            # If factors are equal, 
            # multiply only once 
            if (n / i == i) : 
                prod = (prod * i) % M 
                  
            #Otherwise multiply both 
            else : 
                prod = (prod * i) % M 
                prod = (prod * n / i) % M 
        i = i + 1
  
    return prod 
  
# Driver Code 
  
n = 12
print (multiplyFactors(n)) 
  
