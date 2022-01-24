from english_words import english_words_set


class WordleFinder:
    def __init__(self):
        self.all_words = self._get_all_words_with_length()

    @staticmethod
    def _get_all_words_with_length(length=5) -> set:
        """
        Gets all the english words with the specified length
        :param length:
        :return: set
        """
        _temp = set()
        for word in english_words_set:
            if len(word) == length:
                _temp.add(word)
        return _temp

    def get_word(self):
        """
        Used to return all the words based on criteria
        :return:
        """
        print(self.all_words)
        return self.all_words

    def set_value(self, letter, position=None) -> None:
        """
        Used to set known letters and their positions. A position can be passed or not
        :param letter: a known included letter
        :param position: (optional) a known position of the letter
        :return: None
        """
        _temp = self.all_words.copy()
        for word in _temp:
            if position:
                if word[position - 1] != letter:
                    if word in self.all_words:
                        self.all_words.remove(word)
            else:
                if letter not in word:
                    self.all_words.remove(word)

    def remove_letters(self, *args) -> None:
        """
        Used to remove letters from possible words
        :param args: letters you want to remove as str
        :return: None
        """
        _temp = self.all_words.copy()
        for word in _temp:
            for letter in args:
                if letter in word:
                    if word in self.all_words:
                        self.all_words.remove(word)

    def remove_letters_position(self, letter, position) -> None:
        """
        Used to remove a letter from a position but not if the letter is somewhere else in the word
        :param letter: Letter to remove from position
        :param position: Position to remove the letter from
        :return: None
        """
        _temp = self.all_words.copy()
        for word in _temp:
            if letter in word[position - 1]:
                if word in self.all_words:
                    self.all_words.remove(word)


###########
word = WordleFinder()
word.set_value('e', 2)
word.set_value('a', 3)
word.set_value('r', 4)
word.get_word()
{'yearn', 'weary', 'pearl', 'learn', 'heart', 'beard', 'heard'}
word.set_value('e')
word.remove_letters_position('a', 1)
word.remove_letters_position('e', 4)
word.remove_letters_position('e', 5)
word.remove_letters('d', 'i', 'u', 'n', 'l')
word.get_word()
{'weary', 'heart'}
