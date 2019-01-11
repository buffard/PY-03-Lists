planet_list = ["Mercury", "Mars"]
# 1. Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")
# 2. Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
last_planets = ("Uranus", "Neptune")
planet_list.extend(last_planets)
# 3. Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
# 4. Use append() again to add Pluto to the end of the list.
planet_list.insert(len(planet_list), "Pluto")
# 5. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets
rocky_finder = slice(0, 4)
rocky_planets = planet_list[rocky_finder]
# 6. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[8]


print(planet_list)
print(rocky_planets)
