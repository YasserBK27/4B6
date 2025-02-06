import time

# Initialisation d'une variable pour alterner
toggle = True

# Boucle infinie
while True:
    if toggle:
        print("bonsoir")
    else:
        print("bonjour")
    
    # Alterner la valeur de toggle
    toggle = not toggle
    
    # Pause d'une seconde
    time.sleep(1)
