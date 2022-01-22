![build](https://img.shields.io/pypi/v/english-words)
# PyWordleFinder
Python Class to Find the Wordle of the day.

## Usage/Examples
```python
>> word = WordleFinder()
>> word.set_must_have_letters('y')
>> print(word.get_word())
#{'Wendy', 'beady', 'diety', 'heady', 'edify', 'Ryder', 'Teddy', 'reedy', 'deity', 'ready', 'decry', 'decay', 'Clyde', 'decoy', 'yield', 'seedy', 'yodel', 'derby', 'deify', 'delay', 'weedy', 'needy'}

>> word.set_letter_position('w', 1)
>> print(word.get_word())
#{'washy', 'worry', 'wishy', 'woody', 'warty', 'witty', 'wordy', 'weary', 'weedy', 'withy', 'wacky', 'wally', 'windy', 'wispy', 'wormy'}

>> word.set_letter_position('l', 3)
>> print(word.get_word())
#{'wally'}
```

## Dependencies
Python >= 3.6<br>
english-words >=1.0.4

## Author
[@mobig](https://github.com/mobig)


## License
[MIT](https://choosealicense.com/licenses/mit/)