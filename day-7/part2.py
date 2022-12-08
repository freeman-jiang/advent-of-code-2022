from part1 import *


def find_directory(dir: Directory, target: int):
    suitable_directories = []

    if dir.total_size >= target:
        suitable_directories.append(dir)

    for child in dir.children:
        smallest = find_directory(child, target)
        if smallest:
            suitable_directories.append(smallest)

    if suitable_directories:
        return min(suitable_directories, key=lambda x: x.total_size)

    return None


def main():
    with open("input.txt") as file:
        root = Directory("root")
        current_dir = None
        # Build model of directory
        for line in file:
            if "$ cd" in line:
                dirname = line.split()[-1]
                if dirname == "/":
                    current_dir = root
                elif dirname == "..":
                    if current_dir.parent is not None:
                        current_dir = current_dir.parent
                else:
                    Directory(name=dirname, parent=current_dir)
                    current_dir = current_dir.cd(dirname)
            elif "$" not in line and "dir" not in line:  # We are looking at a file
                file_size, file_name = line.split()
                current_dir.add_to_size(int(file_size))

        # Traverse directory and find those with size at most 100000
        # root.prettyprint()

        TOTAL_SPACE = 70000000
        REQUIRED_SPACE = 30000000

        current_unused = TOTAL_SPACE - root.total_size
        target = REQUIRED_SPACE - current_unused

        answer = find_directory(root, target).total_size
        print(answer)


if __name__ == "__main__":
    main()
