![build](https://img.shields.io/pypi/v/english-words)
# PyWordleFinder
Python Class to Find the Wordle of the day.

## Usage/Examples
```python
>> word = WordleFinder()
>> word.set_value('e', 2)
>> word.set_value('a', 3)
>> word.set_value('r', 4)
>> word.get_word()

{'yearn', 'weary', 'pearl', 'learn', 'heart', 'beard', 'heard'}

>> word.set_value('e')
>> word.remove_letters_position('a', 1)
>> word.remove_letters_position('e', 4)
>> word.remove_letters_position('e', 5)
>> word.remove_letters('d', 'i', 'u', 'n', 'l')
>> word.get_word()

{'weary', 'heart'}
```

## Dependencies
Python >= 3.6<br>
english-words >=1.0.4

## Author
[@mobig](https://github.com/mobig)


## License
[MIT](https://choosealicense.com/licenses/mit/)