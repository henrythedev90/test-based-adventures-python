def display_map(player, middle_earth):
    """Display the map based on player's current location"""
    current_room = player.current_room
    
    # Check if we're in Bag End to show a detailed map
    if hasattr(current_room, 'is_in_bag_end') and current_room.is_in_bag_end:
        print("\n== Bag End Map ==")
        print("Legend: [X] Current Location, [H] Bedroom (Home), [O] Visited Room")
        print("You are inside Bag End, a cozy hobbit-hole.")
        
        # Get only Bag End rooms
        bag_end_rooms = [room for room in middle_earth.locations if hasattr(room, 'is_in_bag_end') and room.is_in_bag_end]
        
        # Find dimensions for Bag End map
        min_x = min(room.map_position[0] for room in bag_end_rooms)
        max_x = max(room.map_position[0] for room in bag_end_rooms)
        min_y = min(room.map_position[1] for room in bag_end_rooms)
        max_y = max(room.map_position[1] for room in bag_end_rooms)
        
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        
        # Create an empty grid filled with None
        grid = [[None for _ in range(width)] for _ in range(height)]
        
        # Place rooms in the grid
        for room in bag_end_rooms:
            x, y = room.map_position
            grid_x = x - min_x
            grid_y = y - min_y
            grid[grid_y][grid_x] = room
    else:
        print("\n== Middle-earth Map ==")
        print("Legend: [X] Current Location, [H] Home (Bag End), [O] Visited Location, [ ] Unexplored")
        print("         |   North")
        print("         v")
        
        # Get map dimensions
        min_x, min_y, width, height = middle_earth.get_map_dimensions()
        
        # Create an empty grid filled with None
        grid = [[None for _ in range(width)] for _ in range(height)]
        
        # Place rooms in the grid
        for room in middle_earth.locations:
            if room.map_position:
                x, y = room.map_position
                grid_x = x - min_x
                grid_y = y - min_y
                grid[grid_y][grid_x] = room
    
    # Draw the map
    for y in range(height):
        # First line: top borders
        line = ""
        for x in range(width):
            room = grid[y][x]
            if room and (room.visited or room == current_room):
                line += "+---"
            else:
                line += "    "
        line += "+"
        print(line)
        
        # Second line: room symbol and connections
        line = ""
        for x in range(width):
            room = grid[y][x]
            if room and (room.visited or room == current_room):
                # Room symbol
                if room == current_room:
                    line += "| X "
                elif hasattr(room, 'is_starting_room') and room.is_starting_room:
                    line += "| H "
                else:
                    line += "| O "
            else:
                line += "    "
        line += "|"
        print(line)
        
        # Third line: horizontal connections
        line = ""
        for x in range(width):
            room = grid[y][x]
            if room and (room.visited or room == current_room):
                if x < width - 1 and grid[y][x+1] and "east" in room.exits and room.exits["east"] == grid[y][x+1]:
                    line += "+---"
                else:
                    line += "+   "
            else:
                line += "    "
        line += "+"
        print(line)
    
    print() 