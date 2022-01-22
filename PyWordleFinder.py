from english_words import english_words_set


class WordleFinder:
    def __init__(self, word_length=5):
        self.starting_letter = ''
        self.containing_letters = {i: None for i in range(5)}
        self.words_for_each_position = {i: [] for i in range(5)}
        self.possible_words = set()
        self.word_length = word_length
        self.bad_characters = []
        self.must_have_letters = []
        self.words_for_must_have_letters = set()

    def set_letter_position(self, letter: str, position: int) -> None:
        """
        Used to set a known letter position.
        :param letter: the letter
        :param position: the position of the letter in the work
        :return: None
        """
        rtn_lst = []
        position -= 1
        for word in english_words_set:
            if len(word) == self.word_length:
                if letter == word[position]:
                    rtn_lst.append(word)
        self.words_for_each_position[position] = rtn_lst

    def get_word(self) -> set:
        """
        Returns the possible wordle based on known letters with position, known letters without position
        and known excluded letters.
        :return: Set of possible Wordles
        """
        self.get_must_have_letters_words()
        self._get_possible_words_from_position()
        if not self._check_position_list_empty():
            self.possible_words = self.words_for_must_have_letters.intersection(self.possible_words)
        else:
            self.possible_words = self.words_for_must_have_letters
        self.remove_characters()
        return self.possible_words

    def _get_possible_words_from_position(self):
        """
        Finds all words that match the positional instances attributes in self.words_for_each_position
        :return: Set of possible Wordles
        """
        self.possible_words = set(list(self.words_for_each_position.values())[0])
        for s in list(self.words_for_each_position.values())[1:]:
            if s:
                self.possible_words.intersection_update(s)
        return self.possible_words

    def _check_position_list_empty(self):
        """
        Returns True if the position list is empty.
        :return: None
        """
        for i in self.words_for_each_position.values():
            if i:
                return False
            else:
                return True

    def remove_characters(self):
        """
        Used to eliminate words that include known unused characters.
        :return:
        """
        _temp = self.possible_words.copy()
        for character in self.bad_characters:
            for word in self.possible_words:
                if character in word:
                    _temp.remove(word)
        self.possible_words = _temp

    def get_must_have_letters_words(self):
        for word in english_words_set:
            if all([letter in word and len(word) == self.word_length for letter in self.must_have_letters]):
                self.words_for_must_have_letters.add(word)

    def set_remove_characters(self, *args):
        self.bad_characters = args

    def set_must_have_letters(self, *args):
        self.must_have_letters = args
