import unittest
from Module_functions import m_functions

class Test_M_Functions(unittest.TestCase):



    def setUp(self):
        self.line_list = []
        self.test_one = m_functions(5)
        self.Col1 = []
        self.Col5 = []
        with open('ColCheckMe', 'r') as f:
            # next(f) # skip headings
            fields = []
            for line in f:
                fields = line.split('\t')
                self.line_list.append(fields)
        for line in self.line_list:
            # print "\t".join(line)
            self.Col1.append(line[0])
            self.Col5.extend([1,2,3])
            #self.Col5.append(line[4])

    def test_check_line_length(self):
        self.assertEqual(self.test_one.check_line_length(self.line_list), True)

    def test_allUnique(self):
        self.assertEqual(self.test_one.allUnique(self.Col1), True)

    def test_check_integers(self):
        self.assertEqual(self.test_one.check_integers(self.Col5), True)

    def test_check_num_string(self):
        self.assertEqual(self.test_one.check_num_string(self.line_list,'SpecStr'), 4)

if __name__ == '__main__':
    unittest.main()