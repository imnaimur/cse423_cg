import random

def generate_positions(minwidth, maxwidth):
   
    start = random.randint(minwidth, maxwidth)

 
    max_positive_diff = (maxwidth - start) // 200
    max_negative_diff = (start - minwidth) // 200

 
    if max_positive_diff <20 and max_negative_diff <20:
        return generate_positions(minwidth, maxwidth)  
    while True:
        difference = random.randint(-max_negative_diff, max_positive_diff)
        if difference != 0 :  
            break

    positions = [start + i * difference for i in range(200)]
    return positions

