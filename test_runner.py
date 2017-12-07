#!/usr/bin/env python3

import unittest
import test_parser

parserTestSuite = unittest.TestSuite()
parserTestSuite.addTest(unittest.makeSuite(test_parser.ParserTest))
print("Count of tests: " + str(parserTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(parserTestSuite)
