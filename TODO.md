# Crossword
- [x] yield important words placements
- [x] if the user doesn't like the board they're given, they can ask for the next one
- [x] return (or print) "this isn't possible! please try other words." instead of an empty board
- [ ] prompting words in a different order yield different results?? ("dogs cats" vs "cats dogs")

# Board
- [x] initialize Board with rows and columns
- [x] implement valid_board
- [x] is_valid: let it input row and column indices to not go over the ENTIRE board
- [x] insert word(row, col, direction)
- [x] implement fill_board method, ignoring #s for now
- [ ] randomize as you go through common_words is fill_board
- [x] DONT CHECK USER WORDS AS INVALID IN IS_VALID
- [ ] remove copies of words au fur-a-mesure while filling board (remove word from common_words after use?)