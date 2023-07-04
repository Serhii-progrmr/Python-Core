def custom_range(start, stop=None):
    counter = start if stop else 0
    
    stop = start if not stop else stop
        
    while counter < stop:
        yield counter
        counter += 1


range_gen = custom_range(10)

for i in range(11):
    next(range_gen)