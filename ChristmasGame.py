print("Welcome to Prep for Christmas! To see commands type help")
christmas_lights = 0
ornaments = 0
presents = 0
christmas_trees = 0

more_colors = False
brighter_colors = False
longer_strands = False
ornament_box = False

paint = False
plastic_to_glass = False
glass_to_metal = False
wrapping_paper = False

ribbon = False
fancy_bows = False
bigger_boxes = False
more_space = False

taller_trees = False
sturdy_branches = False
long_branches = False
december_25th = False

while True:
    command = input("> ").lower()
    if command == "help":
        print("""
        get christmas lights = l
        get ornaments = o
        get presents = p
        get christmas trees = t
        check house = c
        upgrades = u
        (buy upgrades by typing "buy upgrade name" """)
    elif command == "c":
        print(f"{christmas_lights} lights, {ornaments} ornaments, {presents} presents, {christmas_trees} trees")
    elif command == "u":
        print("""
        more colors, 10 lights - increases lights per to 2
        brighter colors, 50 lights - increases lights per to 4
        longer strands, 100 lights - increases lights per to 8
        ornament box, 500 lights - allows the collection of ornaments
        
        paint, 10 ornaments - increases ornaments per to 2
        plastic to glass, 50 ornaments - increases ornaments per to 4
        glass to metal, 100 ornaments - increases ornaments per to 8
        wrapping paper, 500 ornaments - allows the collection of presents
        
        ribbon, 10 presents - increases presents per to 2
        fancy bows, 50 presents - increases presents per to 4
        bigger boxes, 100 presents - increases presents per to 8
        more space, 500 presents - allows the collection of trees
        
        taller trees, 10 trees - increases trees per to 2
        sturdy branches, 50 trees - increases trees per to 4
        long branches, 100 trees - increases trees per to 8
        december 25th, 500 trees - you are prepared for christmas
        
        (each upgrade can only be bought once)
        """)
    if command == "l":
        if longer_strands == True:
            christmas_lights += 8
        elif brighter_colors == True:
            christmas_lights += 4
        elif more_colors == True:
            christmas_lights += 2
        else:
            christmas_lights += 1
    elif command == "o" and ornament_box == True:
        if glass_to_metal == True:
            ornaments += 8
        elif plastic_to_glass == True:
            ornaments += 4
        elif paint == True:
            ornaments += 2
        else:
            ornaments += 1
    elif command == "p" and wrapping_paper == True:
        if bigger_boxes == True:
            presents += 8
        elif fancy_bows == True:
            presents += 4
        elif ribbon == True:
            presents += 2
        else:
            presents += 1
    elif command == "t" and more_space == True:
        if long_branches == True:
            christmas_trees += 8
        elif sturdy_branches == True:
            christmas_trees += 4
        elif taller_trees == True:
            christmas_trees += 2
        else:
            christmas_trees += 1
    if command == "buy more colors" and christmas_lights >= 10:
        christmas_lights -= 10
        more_colors = True
        print("the lights are hard to look away from with the magnificent colors")
    elif command == "buy brighter colors" and christmas_lights >= 50:
        christmas_lights -= 50
        brighter_colors = True
        print("the lights illuminate the entire house")
    elif command == "buy longer strands" and christmas_lights >= 100:
        christmas_lights -= 100
        longer_strands = True
        print("each strand can reach across the whole house")
    elif command == "buy ornament box" and christmas_lights >= 500:
        christmas_lights -= 500
        ornament_box = True
        print("you grab your boxes of ornaments")
    if command == "buy paint" and ornaments >= 10:
        ornaments -= 10
        paint = True
        print("the ornaments are more unique and colorful")
    elif command == "buy plastic to glass" and ornaments >= 50:
        ornaments -= 50
        plastic_to_glass = True
        print("the ornaments feel fancier")
    elif command == "buy glass to metal" and ornaments >= 100:
        ornaments -= 100
        glass_to_metal = True
        print("the ornaments don't break if they fall")
    elif command == "buy wrapping paper" and ornaments >= 500:
        ornaments -= 500
        wrapping_paper = True
        print("you buy all the wrapping paper you can find")
    if command == "buy ribbon" and presents >= 10:
        presents -= 10
        paint = True
        print("the presents are tied instead of taped")
    elif command == "buy fancy bows" and presents >= 50:
        presents -= 50
        fancy_bows = True
        print("the presents look much fancier")
    elif command == "buy bigger boxes" and presents >= 100:
        presents -= 100
        bigger_boxes = True
        print("the boxes nearly can't fit through the door")
    elif command == "buy more space" and presents >= 500:
        presents -= 500
        more_space = True
        print("you rent a mall to fill with christmas spirit")
    if command == "buy taller trees" and christmas_trees >= 10:
        christmas_trees -= 10
        taller_trees = True
        print("the trees touch the ceiling")
    elif command == "buy sturdy branches" and christmas_trees >= 50:
        christmas_trees -= 50
        sturdy_branches = True
        print("the branches don't get weighed down by ornaments")
    elif command == "buy long branches" and christmas_trees >= 100:
        christmas_trees -= 100
        long_branches = True
        print("the branches are nearly 3X longer")
    elif command == "buy december 25th" and christmas_trees >= 500:
        christmas_trees -= 500
        december_25th = True
        print("YOU ARE PREPARED FOR CHRISTMAS!")
        print("Thank you for playing and merry christmas!")