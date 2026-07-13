import random

def jitter(quantity: float) -> float:
    """
    Equal Jitter algoritmi.
    Berilgan quantity vaqtining yarmini oladi va unga 
    qolgan yarmi oralig'idagi tasodifiy sonni qo'shadi.
    """
    if quantity <= 0:
        return 0.0
        
    base = quantity / 2
    random_component = random.uniform(0, quantity / 2)
    
    return base + random_component