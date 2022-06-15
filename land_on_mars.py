print('''
                      <>
        .-"""-.       ||::::::==========
       /=      \      ||::::::==========
      |- /~~~\  |     ||::::::==========
      |=( '.' ) |     ||================
      \__\_=_/__/     ||================
       {_______}      ||================
     /` *       `'--._||
    /= .     [] .     { >
   /  /|ooo     |`'--'||
  (   )\_______/      ||
   \``\/       \      ||
    `-| ==    \_|     ||
      /         |     ||
     |=   >\  __/     ||
     \   \ |- --|     ||
      \ __| \___/     ||
 jgs  _{__} _{__}     ||
     (    )(    )     ||
 ^^~  `"""  `"""  ~^^^~^^~~~^^^~^^^~^^^~^^~^


''')

print("Welcome to SpaceX space ship.")
print("Your mission is to sucseffuly land on Mars. Let's get started!")

space_ship = input("What's the space ship are you going to use? 'Falcon 9' or 'Falcon Heavy'? ")
space_ship.lower()

if space_ship == "falcon heavy":
    print("Space ship exploided during the launch. GAME OVER.")
else:
    fly = input("Great! You launch was sucsseful! You in the space. Will you use 'Autopilot' or 'Manual fly? ")
    fly.lower()
    if fly == "autopilot":
        print("Autopilot wasn't good enougth. You ship crashed by asteroids. GAME OVER.")
    else:
        landing = input("We arrived! Let's find a spot for landing. Will you land on the 'field', 'vulcano' or 'mount'? ")
        landing.lower()
        if landing == "field":
            print("Great job! You on Mars. YOU WON.")
        elif landing == "mount":
            print("Yor ship is crashed. GAME OVER")
        elif landing == "vulcano":
            print("Vulcano was active. Explosion heppend. GAME OVER.")
        else:
            print("GAME OVER.")
