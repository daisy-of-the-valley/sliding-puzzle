def main(tiles):
    moves = 0
    draw_grid(tiles)
    input_list = tiles
    while is_complete(input_list) != True:
        input_list = is_valid(input_list)
        draw_grid(input_list)
        moves += 1
    return print(f"You won in {moves} moves. Congratulations!")


def draw_grid(tiles):
    size_n = get_size(tiles)
    tile_labels = draw_row(tiles)
    #top
    print("┌────", end="")
    for i in range(size_n - 1):
        print("┬────", end="")
    print("┐")
    #rows
    for i in range(size_n):
        row_tile = tile_labels[i * size_n :(i + 1) * size_n]
        row_list = []
        for element in row_tile:
            row_list.append(element)
        row = "│".join(row_list)
        print("│" + row + "│")
        #divider 
        if i < (size_n - 1):
            print("├────", end="")
            for i in range(size_n - 1):
                print("┼────", end="")
            print("┤")
    #end
    print("└────", end="")
    for i in range(size_n - 1):
        print("┴────", end="")
    print("┘")


def get_size(string_of_values):
    import math
    list_of_values = string_of_values.split(",")
    square_number = int(len(list_of_values))
    sqaure_root = math.sqrt(square_number)
    return round(sqaure_root)


def draw_row(data_string):
    data_list = data_string.split(",")
    output_list = []
    for i in data_list:
        if len(i) == 0:
            output_list.append("    ")
        elif len(i) == 1:
            output_list.append("  " + i + " ")
        elif len(i) == 2:
            output_list.append(" " + i + " ")
    return output_list


def is_valid(list_of_choices):
    valid_choices = is_orthagonally_adjacent(list_of_choices)
    prompt = input("Your move: ")
    entered_value = prompt
    if entered_value in valid_choices:
        modified_list = swap_tile(list_of_choices, entered_value)
        return modified_list
    elif entered_value == "quit":
        return (f"{entered_value} is valid.")
    else:
        while entered_value not in valid_choices:
            print(f"{entered_value} is not valid. Try again.")
            prompt = input("Your move: ")
            entered_value = prompt
            if entered_value == "quit":
                return print(f"{entered_value} is valid.")
        modified_list = swap_tile(list_of_choices, entered_value)
        return modified_list


def is_orthagonally_adjacent(input_tiles):
    tiles_list = input_tiles.split(",")
    blank_tile = tiles_list.index("")
    n = get_size(input_tiles)
    valid_inputs = []
    for i in tiles_list:
        if is_vertically_adjacent(n, blank_tile, tiles_list.index(i)):
            valid_inputs.append(i)
        if is_horizontally_adjacent(n, blank_tile, tiles_list.index(i)):
            valid_inputs.append(i)
    return valid_inputs 


def is_vertically_adjacent(n, first, second):
    if second - n == first or first - n == second:
        return True
    else:
        return False


def is_horizontally_adjacent(n, first, second):
    row_first = first // n
    row_second = second // n
    if row_first != row_second:
        return False
    first_mod = first % n
    second_mod = second % n
    if first_mod - second_mod == 1 or first_mod - second_mod == -1:
        return True
    else:
        return False

def swap_tile(list_of_tiles, tile_choice):
    tiles = list_of_tiles.split(",")
    tile_index = tiles.index(tile_choice)
    blank_index = tiles.index("")
    tiles[tile_index], tiles[blank_index] = tiles[blank_index], tiles[tile_index]
    updated_tiles = ",".join(tiles)
    return updated_tiles


def is_complete(string_of_tiles):
    list_of_tiles = string_of_tiles.split(",")
    blank_index = list_of_tiles.index("")
    popped_element = list_of_tiles.pop(blank_index)
    int_list = [int(element) for element in list_of_tiles]
    sorted_list = sorted(int_list)
    sorted_list_string = [str(element) for element in sorted_list]
    list_of_tiles.insert(blank_index, popped_element)
    sorted_list_string.append(popped_element)
    if list_of_tiles == sorted_list_string:
        return True
    else:
        return False

main("1,3,6,4,5,2,,15,8,9,13,12,10,14,11,7")


