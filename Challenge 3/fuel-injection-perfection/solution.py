def solution(n):
    int_n = int(n)

    c=0
    while True:
        if (int_n ==1):
            return c
        elif(int_n%2==0):
            int_n /= 2
        else:
            left = int(int_n-1)
            right = int(int_n+1)
            leftb = bin(left).count('1')                                
            rightb = bin(right).count('1')                              # Count of Ones in the binary
            if(leftb==rightb):                                          # If number of ones matches, check their length, smaller will be better
                if(len(bin(left))<len(bin(right))):                    
                    int_n = left
                else:
                    int_n = right                                       # If length matches it will take the bigger number, because the bigger number divide to be even
            elif (leftb<rightb):        
                int_n = left                                            # Execute if less number of one
            elif(leftb>rightb):
                int_n = right                                           # Execute if more number of one
        c += 1
        