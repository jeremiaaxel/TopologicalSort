from os.path import join
import os

class FileParser:

    def file_to_list_of_courses(filename, test_dir=None) -> list:
        '''
        Takes test directory path (test_dir) and name of the file (filename)
        Return a list of strings.

        if test_dir is not declared, automatically switch to current directory
        '''
        try:
            if (test_dir is None):
                test_dir = os.getcwd()

            f = open(join(test_dir, filename), 'r')
            lines = f.read().splitlines()
            f.close()
            print("File read success")

            list_of_soals = []
            for line in lines:
                line = line.replace(" ", "").replace(".", "").split(",")
                list_of_soals.append(line)

            return list_of_soals

        except FileNotFoundError:
            print("File not found")
            exit(1)

        except TypeError:
            print("Input error")
            exit(1)
