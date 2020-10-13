from ctypes import *
import ctypes.util
from termcolor import colored

import unittest

so_file = "./libft.so"
functions = CDLL(so_file)
path_libc = ctypes.util.find_library("c")
libc = CDLL(path_libc)

class TestStrlen(unittest.TestCase):

	def setUp(self):
		functions.ft_strlen.argtypes = [c_char_p]
		self.strlen = functions.ft_strlen
		self.long_string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
							Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\
							when an unknown printer took a galley of type and scrambled it to make a type\
							specimen book. It has survived not only five centuries, but also the leap into\
							electronic typesetting, remaining essentially unchanged. It was popularised in\
							the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,\
							and more recently with desktop publishing software like Aldus PageMaker including\
							versions of Lorem Ipsum"

	def test_basic(self):
		self.assertEqual(self.strlen(b"Hey"), libc.strlen(b"Hey"), colored("Basic test one ('Hey'): KO", 'red'))
		self.assertEqual(self.strlen(b"String de test"), libc.strlen(b"String de test"), colored("Basic test two ('String de test'): KO", 'red'))
		self.assertEqual(self.strlen(self.long_string.encode("utf-8")), libc.strlen(self.long_string.encode("utf-8")), colored("Basic test three (Long string): KO", "red"))

	def test_null(self):
		self.assertEqual(self.strlen(b""), libc.strlen(b""), colored("Empty string test: KO", 'red'))


class TestIsalpha(unittest.TestCase):
	# On Mac, the built-in function returns 1, on linux (e.g. Ubuntu 18.04), it returns the size of the variable type in bits (1024 in this case).
	def setUp(self):
		self.isalpha = functions.ft_isalpha
		self.isalpha.argtypes = [c_int]

	def test_alpha(self):
		self.assertEqual(self.isalpha(ord('a')), libc.isalpha(ord('a')), colored("Character a: KO", 'red'))
		self.assertEqual(self.isalpha(ord('z')), libc.isalpha(ord('z')), colored("Character z: KO", 'red'))
		self.assertEqual(self.isalpha(ord('A')), libc.isalpha(ord('A')), colored("Character A: KO", 'red'))
		self.assertEqual(self.isalpha(ord('Z')), libc.isalpha(ord('Z')), colored("Character Z: KO", 'red'))

	def test_not_alpha(self):
		self.assertEqual(self.isalpha(ord('6')), libc.isalpha(ord('6')), colored('Character 6: KO', 'red'))

	def test_EOF(self):
		self.assertEqual(self.isalpha(-1), libc.isalpha(-1), colored('Character EOF: KO', 'red'))

class TestIsdigit(unittest.TestCase):
	# On Mac, the built-in function returns 1, on linux (e.g. Ubuntu 18.04), it returns the size of the variable type in bits (2048 in this case).
	def setUp(self):
		self.isdigit = functions.ft_isdigit
		self.isdigit.argtypes = [c_int]

	def test_digit(self):
		self.assertEqual(self.isdigit(ord('5')), libc.isdigit(ord('5')), colored("Number 5: KO", 'red'))
		self.assertEqual(self.isdigit(ord('0')), libc.isdigit(ord('0')), colored("Number 0: KO", 'red'))
		self.assertEqual(self.isdigit(ord('9')), libc.isdigit(ord('9')), colored("Number 9: KO", 'red'))
		self.assertEqual(self.isdigit(ord('2')), libc.isdigit(ord('2')), colored("Number 2: KO", 'red'))

	def test_not_digit(self):
		self.assertEqual(self.isdigit(ord('a')), libc.isdigit(ord('a')), colored('Not digit (a): KO', 'red'))
		self.assertEqual(self.isdigit(ord('z')), libc.isdigit(ord('z')), colored('Not digit (z): KO', 'red'))
		self.assertEqual(self.isdigit(ord('A')), libc.isdigit(ord('A')), colored('Not digit (A): KO', 'red'))
		self.assertEqual(self.isdigit(ord('Z')), libc.isdigit(ord('Z')), colored('Not digit (Z): KO', 'red'))

	def test_EOF(self):
		self.assertEqual(self.isdigit(-1), libc.isdigit(-1), colored('Character EOF: KO', 'red'))

class TestIsalnum(unittest.TestCase):
	# The built-in function returns 8 on Ubuntu 18.04
	def setUp(self):
		self.isalnum = functions.ft_isalnum
		self.isalnum.argtypes = [c_int]

	def test_alnum(self):
		self.assertEqual(self.isalnum(ord('5')), libc.isalnum(ord('5')), colored("Alnum 5: KO", 'red'))
		self.assertEqual(self.isalnum(ord('0')), libc.isalnum(ord('0')), colored("Alnum 0: KO", 'red'))
		self.assertEqual(self.isalnum(ord('9')), libc.isalnum(ord('9')), colored("Alnum 9: KO", 'red'))
		self.assertEqual(self.isalnum(ord('2')), libc.isalnum(ord('2')), colored("Alnum 2: KO", 'red'))
		self.assertEqual(self.isalnum(ord('a')), libc.isalnum(ord('a')), colored("Alnum a: KO", 'red'))
		self.assertEqual(self.isalnum(ord('z')), libc.isalnum(ord('z')), colored("Alnum z: KO", 'red'))
		self.assertEqual(self.isalnum(ord('A')), libc.isalnum(ord('A')), colored("Alnum A: KO", 'red'))
		self.assertEqual(self.isalnum(ord('Z')), libc.isalnum(ord('Z')), colored("Alnum Z: KO", 'red'))

	def test_not_alnum(self):
		self.assertEqual(self.isalnum(ord('-')), libc.isalnum(ord('-')), colored('Not alnum (-): KO', 'red'))
		self.assertEqual(self.isalnum(ord('_')), libc.isalnum(ord('_')), colored('Not alnum (_): KO', 'red'))
		self.assertEqual(self.isalnum(ord('.')), libc.isalnum(ord('.')), colored('Not alnum (.): KO', 'red'))
		self.assertEqual(self.isalnum(ord('!')), libc.isalnum(ord('!')), colored('Not alnum (!): KO', 'red'))
		self.assertEqual(self.isalnum(ord('#')), libc.isalnum(ord('#')), colored('Not alnum #: KO', 'red'))
		self.assertEqual(self.isalnum(130), libc.isalnum(130), colored('Not alnum (unsigned char 130): KO', 'red'))

	def test_EOF(self):
		self.assertEqual(self.isalnum(-1), libc.isalnum(-1), colored('Character EOF: KO', 'red'))

class TestIsascii(unittest.TestCase):

	def setUp(self):
		self.isascii = functions.ft_isascii
		self.isascii.argtypes = [c_int]

	def test_ascii(self):
		self.assertEqual(self.isascii(0), libc.isascii(0), colored("Ascii 0: KO", 'red'))
		self.assertEqual(self.isascii(127), libc.isascii(127), colored("Ascii 127: KO", 'red'))
		self.assertEqual(self.isascii(120), libc.isascii(120), colored("Ascii 120: KO", 'red'))
		self.assertEqual(self.isascii(25), libc.isascii(25), colored("Ascii 25: KO", 'red'))
		self.assertEqual(self.isascii(12), libc.isascii(12), colored("Ascii 0: KO", 'red'))

	def test_not_ascii(self):
		self.assertEqual(self.isascii(-20), libc.isascii(-20), colored("Ascii -20: KO", 'red'))
		self.assertEqual(self.isascii(255), libc.isascii(255), colored("Ascii 255: KO", 'red'))
		self.assertEqual(self.isascii(130), libc.isascii(130), colored("Ascii 130: KO", 'red'))

	def test_EOF(self):
		self.assertEqual(self.isascii(-1), libc.isascii(-1), colored('Character EOF: KO', 'red'))


class TestIsprint(unittest.TestCase):
	# For some reason, the built-in function returns 16384 on Ubuntu 18.04
	def setUp(self):
		self.isprint = functions.ft_isprint
		self.isprint.argtypes = [c_int]

	def test_print(self):
		self.assertEqual(self.isprint(ord('c')), libc.isprint(ord('c')), colored("Printable ('c'): KO", 'red'))
		self.assertEqual(self.isprint(ord('4')), libc.isprint(ord('4')), colored("Printable ('4'): KO", 'red'))
		self.assertEqual(self.isprint(ord('~')), libc.isprint(ord('~')), colored("Printable ('~'): KO", 'red'))
		self.assertEqual(self.isprint(32), libc.isprint(32), colored("Printable (' '): KO", 'red'))
		self.assertEqual(self.isprint(126), libc.isprint(126), colored("Printable (126): KO", 'red'))

	def test_not_print(self):
		self.assertEqual(self.isprint(0), libc.isprint(0), colored("Printable (0): KO", 'red'))
		self.assertEqual(self.isprint(127), libc.isprint(127), colored("Printable (127): KO", 'red'))
		self.assertEqual(self.isprint(255), libc.isprint(255), colored("Printable (255): KO", 'red'))
		self.assertEqual(self.isprint(31), libc.isprint(31), colored("Printable (31): KO", 'red'))
		self.assertEqual(self.isprint(-20), libc.isprint(-20), colored("Printable (-20): KO", 'red'))

	def test_EOF(self):
		self.assertEqual(self.isprint(-1), libc.isprint(-1), colored("Character EOF: KO", 'red'))


class TestToupper(unittest.TestCase):

	def setUp(self):
		self.toupper = functions.ft_toupper
		self.toupper.argtypes = [c_int]

	def test_upper(self):
		self.assertEqual(self.toupper(ord('c')), libc.toupper(ord('c')), colored("To upper ('c'): KO", 'red'))
		self.assertEqual(self.toupper(ord('a')), libc.toupper(ord('a')), colored("To upper ('a'): KO", 'red'))
		self.assertEqual(self.toupper(ord('z')), libc.toupper(ord('z')), colored("To upper ('z'): KO", 'red'))
		self.assertEqual(self.toupper(ord('f')), libc.toupper(ord('f')), colored("To upper ('f'): KO", 'red'))

	def test_not_upper(self):
		self.assertEqual(self.toupper(ord('C')), libc.toupper(ord('C')), colored("To upper ('C'): KO", 'red'))
		self.assertEqual(self.toupper(ord('A')), libc.toupper(ord('A')), colored("To upper ('A'): KO", 'red'))
		self.assertEqual(self.toupper(ord('~')), libc.toupper(ord('~')), colored("To upper ('~'): KO", 'red'))
		self.assertEqual(self.toupper(ord('!')), libc.toupper(ord('!')), colored("To upper ('!'): KO", 'red'))
		self.assertEqual(self.toupper(ord('\t')), libc.toupper(ord('\t')), colored("To upper ('\t'): KO", 'red'))
		self.assertEqual(self.toupper(ord('\n')), libc.toupper(ord('\n')), colored("To upper ('\n'): KO", 'red'))
		self.assertEqual(self.toupper(127), libc.toupper(127), colored("To upper (127): KO", 'red'))
		self.assertEqual(self.toupper(31), libc.toupper(31), colored("To upper (31): KO", 'red'))

	def test_EOF(self):
		self.assertEqual(self.toupper(-1), libc.toupper(-1), colored("Character EOF: KO", 'red'))

class TestTolower(unittest.TestCase):

	def setUp(self):
		self.tolower = functions.ft_tolower
		self.tolower.argtypes = [c_int]

	def test_lower(self):
		self.assertEqual(self.tolower(ord('C')), libc.tolower(ord('C')), colored("To lower ('C'): KO", 'red'))
		self.assertEqual(self.tolower(ord('A')), libc.tolower(ord('A')), colored("To lower ('A'): KO", 'red'))
		self.assertEqual(self.tolower(ord('Z')), libc.tolower(ord('Z')), colored("To lower ('Z'): KO", 'red'))
		self.assertEqual(self.tolower(ord('F')), libc.tolower(ord('F')), colored("To lower ('F'): KO", 'red'))

	def test_not_lower(self):
		self.assertEqual(self.tolower(ord('c')), libc.tolower(ord('c')), colored("To lower ('c'): KO", 'red'))
		self.assertEqual(self.tolower(ord('a')), libc.tolower(ord('a')), colored("To lower ('a'): KO", 'red'))
		self.assertEqual(self.tolower(ord('~')), libc.tolower(ord('~')), colored("To lower ('~'): KO", 'red'))
		self.assertEqual(self.tolower(ord('!')), libc.tolower(ord('!')), colored("To lower ('!'): KO", 'red'))
		self.assertEqual(self.tolower(ord('\t')), libc.tolower(ord('\t')), colored("To lower ('\t'): KO", 'red'))
		self.assertEqual(self.tolower(ord('\n')), libc.tolower(ord('\n')), colored("To lower ('\n'): KO", 'red'))
		self.assertEqual(self.tolower(127), libc.tolower(127), colored("To lower (127): KO", 'red'))
		self.assertEqual(self.tolower(31), libc.tolower(31), colored("To lower (31): KO", 'red'))

	def test_EOF(self):
		self.assertEqual(self.tolower(-1), libc.tolower(-1), colored("Character EOF: KO", 'red'))