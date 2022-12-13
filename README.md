# advent-of-code-2022

a fun way to learn python!


## Comments:
Day 1: Python is incredibly terse and list comprehensions are cool, although I'm more used to using callbacks from my JavaScript background
Day 3: Must admit that `ord` is much more ergonomic than `charCodeAt(0)` for converting characters to Unicode number
Day 5: The hard part of this question is parsing the initial state of the stacks. Key is to look backwards after you find the index of the numbers themselves.
Day 6: Classic sliding window algorithm
Day 7: Very cool problem, came up with an object-oriented recursive solution using general trees. Interestingly, most of the recursion is upwards (ie. from a folder to its parent)
Day 8: Relatively straightforward once you figure out how to do it for one tree position.
Day 9: Key is defining a function that will take a head and a tail to return the new tail
Day 11: Spent a lot of time thinking about how to solve part 2 because the numbers were getting huuuge. The key realization is that the monkeys only care if they can divide the number. We can thus apply modular arithmetic: if we take the item mod the product of all the monkeys' divisors, the resulting operations should continue the same way as if we didn't.
