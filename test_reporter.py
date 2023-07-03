from reporter.sk_report_generator import ReportGenerator
from sk_calculator import Calculator
import unittest
class TestGetValues(unittest.TestCase):

    def setUp(self):
        self.reporter =ReportGenerator()



    def test_get_values(self):

        data = {'$x': '3', '$y': '3', '$var': '460', '$var2': '6', '$xy': '12', '$yx': '18'}
        template  = '''{{$x+$y}}+{{$var+$var2}}+$xy+$yx'''
        report = self.reporter.generate_report(template,data)
        expected_report  = '3+3+460+6+$xy+$yx'
        self.assertEqual(report,expected_report)

    def test_get_values_with_expression(self):
        # Test when there is an expression in the variable declaration

        data = {'$x': '3', '$y': '3', '$z': '12'}
        template  = '''$x+$y+$z'''
        report = self.reporter.generate_report(template,data)
        expected_report  = '$x+$y+$z'
        self.assertEqual(report,expected_report)

    def test_get_values_with_multiple_expressions(self):
        # Test when there are multiple expressions in the variable declaration

        data = {'$x': '3', '$y': '3', '$z': '12', '$w': '4.5'}
        template  = '''{{$x+$y+$z+$w}}'''
        expected_report  = '3+3+12+4.5'
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_get_values_with_nested_expressions(self):
        # Test when there are nested expressions in the variable declaration
        data = "$x = 1 + 2; $y = 2 + 1; $z = $x + $y * ($x + $y); $w = $x + $y / ($x + $y);"
        data = {'$x': '3', '$y': '3', '$z': '21', '$w': '3.5'}
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_get_values(self):
        data = {'$x': '3', '$y': '3', '$var': '460', '$var2': '6', '$xy': '12', '$yx': '18'}
        template = '''{{$x+$y}}+{{$var+$var2}}+$xy+$yx'''
        report = self.reporter.generate_report(template, data)
        expected_report = '3+3+460+6+$xy+$yx'
        self.assertEqual(report, expected_report)

    def test_get_values_with_expression(self):
        data = {'$x': '3', '$y': '3', '$z': '12'}
        template = '''{{$x+$y+$z}}'''
        report = self.reporter.generate_report(template, data)
        expected_report = '3+3+12'
        self.assertEqual(report, expected_report)

    def test_get_values_with_multiple_expressions(self):
        data = {'$x': '3', '$y': '3', '$z': '12', '$w': '4.5'}
        template = '''{{$x+$y+$z+$w}}'''
        expected_report = '3+3+12+4.5'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

    def test_get_values_with_nested_expressions(self):
        data = {'$x': '3', '$y': '3', '$z': '21', '$w': '3.5'}
        template = '''{{$x + $y * ($x + $y)}} {{$x + $y / ($x + $y)}}'''
        expected_report = '3 + 3 * (3 + 3) 3 + 3 / (3 + 3)'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

    def test_get_values_with_multiple_variable_assignment(self):
        # Test when there are multiple variable assignments in the expression
        data = {'$matrix1': [1.0,2.0,3.0,4.0]}
        template = '''{{$matrix1.avg()}}'''
        expected_report = '2.5'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

    def test_get_values_with_list_variable(self):
        data = {'$list': [1, 2, 3, 4]}
        template = '''{{$list[0]}}+{{$list[1]}}+{{$list[2]}}+{{$list[3]}}'''
        report = self.reporter.generate_report(template, data)
        expected_report = '1+2+3+4'
        self.assertEqual(report, expected_report)

    def test_get_values_with_dictionary_variable(self):
        data = {'$dict': {'key1': 1, 'key2': 2, 'key3': 3}}
        template = '''{{$dict.key1}}+{{$dict.key2}}+{{$dict.key3}}'''
        report = self.reporter.generate_report(template, data)
        expected_report = '1+2+3'
        self.assertEqual(report, expected_report)

    def test_get_values_with_nested_variables(self):
        data = {'$x': '3', '$y': 3, '$z': '$x + $y'}
        template = '''{{$x}}+{{$y}}+{{$z}}'''
        report = self.reporter.generate_report(template, data)
        expected_report = '3+3+$x + $y'
        self.assertEqual(report, expected_report)


    def test_get_values_with_empty_variable(self):
        data = {'$x': '', '$y': ''}
        template = '''{{$x}}+{{$y}}'''
        report = self.reporter.generate_report(template, data)
        expected_report = '+'
        self.assertEqual(report, expected_report)


    def test_get_values_with_multiple_complex_expressions(self):
        # Test when there are multiple complex expressions in the variable declaration

        data = {'$table': [{'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'department': 'Sales', 'salary': 50000.0, 'hire_date': '2020-01-15'}, {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'age': 35, 'department': 'HR', 'salary': 60000.0, 'hire_date': '2019-05-20'}, {'id': 3, 'first_name': 'Michael', 'last_name': 'Johnson', 'age': 28, 'department': 'IT', 'salary': 55000.0, 'hire_date': '2021-03-10'}, {'id': 4, 'first_name': 'Sarah', 'last_name': 'Williams', 'age': 32, 'department': 'Marketing', 'salary': 58000.0, 'hire_date': '2018-09-01'}, {'id': 5, 'first_name': 'David', 'last_name': 'Brown', 'age': 29, 'department': 'Finance', 'salary': 52000.0, 'hire_date': '2022-02-28'}]}
        template = '''{{$table[0].id}}'''
        expected_report = '''1'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$table[0].id}}'''
        expected_report = '''1'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)



    def test_get_values_with_no_variables(self):
        # Test when there are no variable declarations

        data = {'$x': [1,2,3,4,5,6,7]}
        template = '''{{$x}}'''
        expected_report='''[1, 2, 3, 4, 5, 6, 7]'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)


        template = '''{{$x.avg()}}'''
        expected_report='''4.0'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.avg((x)=>x>1)}}'''
        expected_report='''4.5'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.sum()}}'''
        expected_report='''28'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.sum((x)=>x>1)}}'''
        expected_report='''27'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.min()}}'''
        expected_report='''1'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.min((x)=>x>1)}}'''
        expected_report='''2'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.count(1)}}'''
        expected_report='''1'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.count(0)}}'''
        expected_report='''0'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.len()}}'''
        expected_report='''7'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_scripts(self):
        data = {'$table': [{'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'department': 'Sales', 'salary': 50000.0, 'hire_date': '2020-01-15'}, {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'age': 35, 'department': 'HR', 'salary': 60000.0, 'hire_date': '2019-05-20'}, {'id': 3, 'first_name': 'Michael', 'last_name': 'Johnson', 'age': 28, 'department': 'IT', 'salary': 55000.0, 'hire_date': '2021-03-10'}, {'id': 4, 'first_name': 'Sarah', 'last_name': 'Williams', 'age': 32, 'department': 'Marketing', 'salary': 58000.0, 'hire_date': '2018-09-01'}, {'id': 5, 'first_name': 'David', 'last_name': 'Brown', 'age': 29, 'department': 'Finance', 'salary': 52000.0, 'hire_date': '2022-02-28'}]}
        template = '''<><<{{$table[0].id}}>> </>'''
        expected_report = '''1'''
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''<><<{{$table[0].first_name}}>></>'''
        expected_report = '''John'''
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''<>
for item in {{$table}}:
    <<{item.id}>>
        </>'''
        expected_report ='1\n2\n3\n4\n5'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data  ={'$x': {'sanjakate': [{'allonomous': [[3]]}], 'adjectivitis': [[{'uneconomizing': [0.8498277974832624]}]], 'Galbulinae': [[{'caramba': [0.04015297797329953]}]]}}
        template = '''{{$x.sanjakate[0].allonomous[0][0]}}'''
        expected_report ='3'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_alignment(self):
        data = {'$x' : 1}
        template = '''{{$x :b}}'''
        expected_report ='1'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : 1}
        template = '''{{$x :>5}}'''
        expected_report ='    1'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : 1}
        template = '''{{$x :^5}}'''
        expected_report ='  1  '
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : 1}
        template = '''{{$x :<5}}'''
        expected_report ='1    '
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)
        # Test case 1: Left alignment with width of 10
        data = {'$x': 123}
        template = '''{{$x :<10}}'''
        expected_report = '123       '
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

        # Test case 2: Right alignment with width of 8 and fill character '0'
        data = {'$x': 123}
        template = '''{{$x :0>8}}'''
        expected_report = '00000123'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

        # Test case 3: Center alignment with width of 6 and fill character '-'
        data = {'$x': 12}
        template = '''{{$x :-^6}}'''
        expected_report = '--12--'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

        # Test case 4: Left alignment with width of 7 and fill character '#'
        data = {'$x': 12345}
        template = '''{{$x :#<7}}'''
        expected_report = '12345##'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

if __name__ == '__main__':
    unittest.main()