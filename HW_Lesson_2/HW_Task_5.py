vip_seats = {1: "Messi", 2: "Ronaldo", 3: "Zidane", 4: "Totti", 5: "Pele"}
common_room = {6: "Cafu", 7: "Shevchenko", 8: "Henry", 9: None, 10: None}

print(vip_seats)
print(common_room)

vip_seats.update(common_room)

print(vip_seats)
