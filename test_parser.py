import sys
import subprocess
import os


file_name = "ad_hoc_coverage_results.txt"
PATH = os.path.join(os.getcwd(), file_name)


def test_hit(line_id, function_name, expected_total):
    with open(PATH, "a+") as result_file:
        result_file.write("{}:{}/{}\n".format(function_name, line_id, expected_total))


def report_results():
    with open(PATH, "r") as result_file:
        results = list(set([r.strip() for r in result_file.readlines()]))
        sys.stdout = open(PATH, 'w')
        print("The following lines where hit running the pytest command")
        for r in sorted(results):
            print(str(r))


if __name__ == '__main__':
    open(PATH, 'w')
    process = subprocess.Popen("pytest", shell=True, stdout=subprocess.PIPE)
    process.wait()
    report_results()
