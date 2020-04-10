import unittest
from unittest.mock import patch
import io
import sys

from inputs import *

class TestOfMainInputs(unittest.TestCase):
    def testInputOptionsOk(self):
        user_input = ['R',"r"]
        with patch('builtins.input', side_effect=user_input):
            option = Input('Opción R/S', ('R', 'S'))
        self.assertEqual(option, 'R')

    def testInputOptionsMoreThanOne(self):
        user_input = ['N',"s"]
        with patch('builtins.input', side_effect=user_input):
            option = Input('Opción R/S', ('R', 'S'))
        self.assertEqual(option, 'S')

    def testInputMsgError(self):
        user_input = ["N", "s"]
        capturedOutput = io.StringIO()           # Create StringIO object
        sys.stdout = capturedOutput             
                           # Reset redirect.
        with patch('builtins.input', side_effect=user_input):
            option = Input('Opción R/S', ('R', 'S'))
        self.assertEqual(option, 'S')
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Opción incorrecta\n") 

    def testValidaNumberOk(self):
        self.assertTrue(valida_number('.0'))
        self.assertTrue(valida_number('0'))
        self.assertTrue(valida_number('0.'))
        self.assertTrue(valida_number('-.0'))
        self.assertTrue(valida_number('-0.0'))

    def testValidaNumberWrong(self):
        self.assertFalse(valida_number('.'))
        self.assertFalse(valida_number('-0.0-'))
        self.assertFalse(valida_number('-0.w'))

    def testInputNumberOk(self):
        user_input = ['923.0']
        with patch('builtins.input', side_effect=user_input):
            option = input_number('Numero')
        self.assertEqual(option, '923.0')

    def testInputNumberMoreThanOne(self):
        user_input = ['',"923.1"]
        with patch('builtins.input', side_effect=user_input):
            option = input_number('Numero')
        self.assertEqual(option, '923.1')

    def testInputNumberMsgError(self):
        user_input = ['',"923.1"]
        capturedOutput = io.StringIO()           # Create StringIO object
        sys.stdout = capturedOutput             
                           # Reset redirect.
        with patch('builtins.input', side_effect=user_input):
            option = input_number('Numero')
        self.assertEqual(option, '923.1')
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "No es un número\n") 
        



if __name__ == '__main__':
    unittest.main()
