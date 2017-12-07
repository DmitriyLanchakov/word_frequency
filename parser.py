#!/usr/bin/env python3

from collections import Counter
import re


class Parser():
    _words = []
    _reg = re.compile('[^a-zA-Zа-яА-Я ]')
    _input_file_name = 'input.txt'
    _output_file_name = 'output.txt'

    def _set_words(self, words):
        self._words = words

    def _get_words(self):
        return self._words

    def _set_reg(self, reg):
        self._reg = reg

    def _get_reg(self):
        return self._reg

    def _set_input_file_name(self, input_file_name):
        self._input_file_name = input_file_name

    def _get_input_file_name(self):
        return self._input_file_name

    def _set_output_file_name(self, output_file_name):
        self._output_file_name=output_file_name

    def _get_output_file_name(self):
        return self._output_file_name

    def read_file(self):
        with open(self._get_input_file_name()) as input_file:
            words = []
            for line in input_file:
                filtered_line = self._get_reg().sub('', line)
                for word in re.findall(r'\w+', filtered_line.casefold()):
                    words.append(word)

            self._set_words(words)
        input_file.close()

    def write_file(self):
        with open(self._get_output_file_name(), "w") as output_file:
            for word, count in Counter(self._get_words()).most_common():
                print('%-70s %d' % (word, count), file=output_file)
        output_file.close()

parser = Parser()
parser.read_file()
parser.write_file()









