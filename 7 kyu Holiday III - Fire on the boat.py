def fire_fight(s):
    lst = []

    for i in s.split():
        if i == 'Fire':
            lst.append('~~')
        else:
            lst.append(i)

    return ' '.join(lst)


print(fire_fight("Boat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast"),
      "Boat Rudder Mast Boat Hull Water ~~ Boat Deck Hull ~~ Propeller Deck ~~ Deck Boat Mast")
print(fire_fight("Mast Deck Engine Water Fire"),
      "Mast Deck Engine Water ~~")
print(fire_fight("Fire Deck Engine Sail Deck Fire Fire Fire Rudder Fire Boat Fire Fire Captain"),
      "~~ Deck Engine Sail Deck ~~ ~~ ~~ Rudder ~~ Boat ~~ ~~ Captain")
