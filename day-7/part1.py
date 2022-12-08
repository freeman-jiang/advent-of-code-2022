# Creating node class
class Directory:
    def __init__(self, name: str, parent=None):
        self.total_size = 0
        self.children: list[Directory] = []

        if parent is not None:
            parent.children.append(self)
            self.parent = parent
        else:
            self.parent = None
        self.name = name

    def prettyprint(self, spacing: int = 2):
        print(self.name, self.total_size)
        for child in self.children:
            result = " " * spacing
            print(result, end="")
            child.prettyprint(spacing + 2)

    def cd(self, dirname: str):
        for child in self.children:
            if child.name == dirname:
                return child
        raise Exception(f"{self.name} does not have a child directory of {dirname}")

    def add_to_size(self, n: int):
        self.total_size += n
        if self.parent is None:
            return
        self.parent.add_to_size(n)


def sum_of_all(dir: Directory) -> int:
    sum_children = sum(sum_of_all(child) for child in dir.children)
    return dir.total_size + sum_children


def sum_of_small(dir: Directory) -> int:
    sum_children = sum(sum_of_small(child) for child in dir.children)
    if dir.total_size < 100000:
        return dir.total_size + sum_children
    else:
        return sum_children


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

        answer = sum_of_small(root)
        print(answer)


if __name__ == "__main__":
    main()
