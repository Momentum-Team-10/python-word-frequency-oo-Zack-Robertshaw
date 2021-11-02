STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename
        # pass

    def read_contents(self):
        with open(self.filename) as text:
            text = text.read()
            # print(text)
            return(text)

        """
        This should read all the contents of the file
        and return them as one string.
        """
        # raise NotImplementedError("FileReader.read_contents")


class WordList:
    def __init__(self, text):
        self.text = text

    def extract_words(self):
        self.text = self.text.replace(",", " ")
        self.text = self.text.replace(".", " ")
        self.text = self.text.replace("_", " ")
        self.text = self.text.replace("?", " ")
        self.text = self.text.replace(":", " ")
        self.text = self.text.replace("’", "")
        self.text = self.text.replace("-", " ")
        self.text = self.text.replace("\n", " ")
        self.text = self.text.lower()
        self.text = self.text.split(' ')
        # print(self.text)


        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        # raise NotImplementedError("WordList.extract_words")

    def remove_stop_words(self):
        while 'a' in self.text:
            self.text.remove('a')
        while 'an' in self.text:
            self.text.remove('an')
        while 'and' in self.text:
            self.text.remove('and')
        while 'are' in self.text:
            self.text.remove('are')
        while 'as' in self.text:
            self.text.remove('as')
        while 'at' in self.text:
            self.text.remove('at')
        while 'be' in self.text:
            self.text.remove('be')
        while 'by' in self.text:
            self.text.remove('by')
        while 'for' in self.text:
            self.text.remove('for')
        while 'from' in self.text:
            self.text.remove('from')
        while 'has' in self.text:
            self.text.remove('has')
        while 'he' in self.text:
            self.text.remove('he')
        while 'i' in self.text:
            self.text.remove('i')
        while 'in' in self.text:
            self.text.remove('in')
        while 'is' in self.text:
            self.text.remove('is')
        while 'it' in self.text:
            self.text.remove('it')
        while 'its' in self.text:
            self.text.remove('its')
        while 'of' in self.text:
            self.text.remove('of')
        while 'on' in self.text:
            self.text.remove('on')
        while 'that' in self.text:
            self.text.remove('that')
        while 'the' in self.text:
            self.text.remove('the')
        while 'to' in self.text:
            self.text.remove('to')
        while 'were' in self.text:
            self.text.remove('were')
        while 'will' in self.text:
            self.text.remove('will')
        while 'with' in self.text:
            self.text.remove('with')
        while '' in self.text:
            self.text.remove('')
        # print(self.text)
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        # raise NotImplementedError("WordList.remove_stop_words")

    def get_freqs(self):
        lines = sorted(self.text, key=self.text.count, reverse=True) 

        dict = {}

        for word in self.text:
            dict[word] = self.text.count(word)

        print(dict)
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        # raise NotImplementedError("WordList.get_freqs")


class FreqPrinter:
    def __init__(self, freqs):
        pass

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        raise NotImplementedError("FreqPrinter.print_freqs")


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    # breakpoint()
    if file.is_file():
        reader =FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)

# Pbd  $ n
#      $ word_list
#      $ word_list.__dict__