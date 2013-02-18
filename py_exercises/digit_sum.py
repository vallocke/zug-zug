def digit_sum(n, total):
    if n > 9:
        total += n % 10
        n //= 10
        return digit_sum(n, total)
    else:
        return n + total
        
print digit_sum(1234, 0)

def digit_sum2(n):
    if n > 9:
        return n % 10 + digit_sum2(n // 10)
    else:
        return n

print digit_sum2(1234)
    
