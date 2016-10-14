


a = float (input ("Please enter  a: "))
b = float (input ("Please enter  b: "))
c = float (input ("Please enter  c: "))
largest = max(a, b, c)
minimum = min(a, b, c)



if a!= largest and a!= minimum:
     middle= a 



elif b!= largest and b!= minimum:
     middle= b 

else: middle = c



if (largest<=0) or (middle<=0) or (minimum<=0):
    print -1

    


elif(largest>middle+minimum): 

     print -1 


elif (largest) ** 2 < ((minimum) ** 2 + (middle) ** 2):
       print 1
     
elif (largest) ** 2 > ((minimum) ** 2 + (middle) ** 2):
        print 2

elif largest ** 2 == (minimum ** 2 + middle ** 2):
        print 3











   
    
    
         
