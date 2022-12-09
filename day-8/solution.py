def main():
    with open("input.txt") as file:
        grid = [list(row) for row in file.read().splitlines()]
        max_cols = len(grid)
        max_rows = len(grid[0])

        def is_visible(tree_coordinates: (int, int)) -> bool:
            tree_row, tree_col = tree_coordinates
            tree_height = grid[tree_row][tree_col]

            heights_north = [grid[row][tree_col] for row in range(0, tree_row)]
            if all([tree_height > height for height in heights_north]):
                return True

            heights_east = [grid[tree_row][col] for col in range(tree_col + 1, max_cols)]
            if all([tree_height > height for height in heights_east]):
                return True

            heights_south = [grid[row][tree_col] for row in range(tree_row + 1, max_rows)]
            if all([tree_height > height for height in heights_south]):
                return True

            heights_west = [grid[tree_row][col] for col in range(0, tree_col)]
            if all([tree_height > height for height in heights_west]):
                return True

            return False

        num_perimeter_trees = 2 * len(grid) + 2 * len(grid[0]) - 4
        visible_trees = num_perimeter_trees

        # Check the inner trees
        for row in range(1, max_rows - 1):
            for col in range(1, max_cols - 1):
                if is_visible((row, col)):
                    visible_trees += 1

        print(f"Part 1: {visible_trees}")

        def calculate_scenic_score(tree_coordinates: (int, int)) -> int:
            tree_row, tree_col = tree_coordinates
            house_height = grid[tree_row][tree_col]

            heights_north = [grid[row][tree_col] for row in reversed(range(0, tree_row))]
            heights_east = [grid[tree_row][col] for col in range(tree_col + 1, max_cols)]
            heights_south = [grid[row][tree_col] for row in range(tree_row + 1, max_rows)]
            heights_west = [grid[tree_row][col] for col in reversed(range(0, tree_col))]

            all_heights = [heights_north, heights_east, heights_south, heights_west]

            scenic_score = 1

            for direction in all_heights:
                direction_scenic_score = 0
                for height in direction:
                    direction_scenic_score += 1
                    if house_height <= height:
                        break

                scenic_score *= direction_scenic_score

            return scenic_score

        max_score = 0

        for row in range(max_rows):
            for col in range(max_cols):
                score = calculate_scenic_score((row, col))
                if score > max_score:
                    max_score = score

        print(f"Part 2: {max_score}")


if __name__ == "__main__":
    main()
