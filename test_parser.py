import sys
import subprocess
import os

class TestCoverageHandler:

    """
    To run this coverage tool:
        1. Import this class into the class you will test
        2. Initialize it at the top of the class with the name of the function you will test
           and the expected number of branches to test.
           EXAMPLE : tch = TestCoverageHandler(<name_of_function_you_will_test>, 22)
        3. In the function you want to test call tch.test_hit(id_of_test)
           at the branch that you want to check
        4. Run this python script by writing the following in the command line:
           python test_parser.py <name_of_function_you_will_test>
                                  make sure its the same as in step 2
    """
    def __init__(self, function_name, expected_lines=20):
        self.function_name = function_name
        file_name = function_name + "_results.txt"
        self.path = os.path.join(os.getcwd(), file_name)
        print(self.path)
        self.expected_lines = expected_lines

    def test_hit(self, line_id):
        with open(self.path, "a+") as result_file:
            result_file.write(str(line_id) + '\n')

    def report_results(self):
        with open(self.path, "r") as result_file:
            results = [r.strip() for r in result_file.readlines()]
            results = list(set(results))
            print("Results from function: " + self.function_name)
            print("The following lines where hit running the pytest command")
            for r in sorted(results):
                print(str(r))
            print("Total lines hit: {}\nExpected lines: {}".format(len(results), self.expected_lines))
            print("Total coverage is {}/1.0".format(len(results) / self.expected_lines))


if __name__ == '__main__':
    tch = TestCoverageHandler(sys.argv[1])
    process = subprocess.Popen("pytest", shell=True, stdout=subprocess.PIPE)
    process.wait()
    tch.report_results()
