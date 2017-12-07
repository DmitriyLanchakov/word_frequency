#!/usr/bin/env python3

from parser import Parser
import unittest
import os
import hashlib


class ParserTest(unittest.TestCase, Parser):
    _output_test_file_name = 'test_output.txt'

    def _set_output_test_file_name(self, output_test_file_name):
        self._output_test_file_name=output_test_file_name

    def _get_output_test_file_name(self):
        return self._output_test_file_name

    def get_file_hash(self, file_name):
        blocksize = 65536
        hasher = hashlib.sha1()
        with open(file_name, 'rb') as afile:
            buf = afile.read(blocksize)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(blocksize)
        return(hasher.hexdigest())

    def test_parser(self):
        self._set_input_file_name('test_input_original.txt')
        self._set_output_file_name('test_output_original.txt')

        parser = Parser()
        parser._set_input_file_name(self._get_input_file_name())
        parser._set_output_file_name(self._get_output_test_file_name())
        parser.read_file()
        parser.write_file()

        output_hash = self.get_file_hash(self._get_output_test_file_name())
        output_original_hash = self.get_file_hash(self._get_output_file_name())

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), self._get_output_test_file_name())
        os.remove(path)

        self.assertEqual(output_hash, output_original_hash)
