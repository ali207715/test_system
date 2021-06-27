#!/usr/bin/env python

"""
A prototype of an automated test system.

Two test cases present:
File list test: Lists out the files present in the home directory every 2 seconds
Random file test: Creates and deletes a file of size 1 MB with random content if the host's current RAM usage
                  drops below 1 GB.

External libraries utilized: psutil (for checking status of the system).
NOTE: You may use the search feature in IDE's to look for tags given below for better inspection:
      [O] - categorises lines that are optional and may be omitted for a faster/clutter-free execution.
      [C] - categorises lines that you may change based on your needs.

P.S As the programs were fairly simple, there was no need for any exception handling.
"""

import psutil
import time
import sys
import pathlib
import os
import datetime


# TestCase 1 ----------------------------------------------------------------------------------------------------


class FileList:

    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

        sys.stdout.write("TestCase named " + name + " with id:" + str(tc_id) + " active \n")

    def prep(self):
        current_time = time.time()  # returns time in epoch format.
        if int(current_time) % 2 == 0:

            sys.stdout.write("Current system time since Unix Epoch is divisible by 2, interrupting test case \n")
            return True

    def run(self):
        home_dir = str(pathlib.Path.home())  # lists both the files and folders present in the home directory
        files = [f for f in os.listdir(home_dir) if os.path.isfile(os.path.join(home_dir, f))]
        # [C] Line above can commented out if the folders present in the home directory need to listed as well.

        sys.stdout.write("Listing the files from the home directory upon interrupt: \n")
        print(*files, sep="\n")

    def clean_up(self):
        input("Please press enter to continue..")
        # [O] The line can be omitted for complete automation

    def execute(self):
        sys.stdout.write("File list test execution\n")
        now = datetime.datetime.now()

        sys.stdout.write("Start time: " + now.strftime("%H : %M : %S") + "\n")

        while True:
            sys.stdout.write("Current epoch time since Epoch Unix: " + str(time.time()) + "\n")
            # [O] The line above can be commented out for clutter-free execution.

            if FileList.prep(self):
                FileList.run(self)
                FileList.clean_up(self)

            sys.stdout.write("To exit the test, please press CTRL + C \n")
            # [O] The line above can be commented out for a clutter-free execution.


# TestCase 2 ----------------------------------------------------------------------------------------------------

class RandomFile:

    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

        sys.stdout.write("TestCase named " + name + " with id:" + str(tc_id) + " active" + "\n")

    def prep(self):
        current_available_memory = psutil.virtual_memory()[1] / 1e+9
        if current_available_memory < 5:
            sys.stdout.write("Current available RAM below 1 GB, interrupting test case \n")
            return True

    def run(self):
        with open("test.txt", "w") as test:
            test.write(str(os.urandom(1024000)))  # size exceeds 1024 KB by a bit due to the str method.

        sys.stdout.write("File of size " + str((os.path.getsize("test.txt")) / 1000000) + " MB created successfully." + "\n")

    def clean_up(self):
        os.remove("test.txt")  # As the file was created in the same directory, no need to specify a path

        sys.stdout.write("File named test.txt removed successfully.\n")
        input("Please press Enter to continue..")
        # [0] The line above can be omitted for complete automation.

    def execute(self):
        sys.stdout.write("Random file test execution\n")
        now = datetime.datetime.now()

        sys.stdout.write("Start time: " + now.strftime("%H : %M : %S") + "\n")

        while True:

            sys.stdout.write("Current available RAM: " + str(int(psutil.virtual_memory()[1] / 1e+9)) + " GB" + "\n")
            # [0] The line above can be commented out for clutter-free execution.

            if RandomFile.prep(self):
                RandomFile.run(self)
                RandomFile.clean_up(self)

            sys.stdout.write("To exit the test, please press CTRL + C \n")
            # [O] The line above can be commented out for a clutter-free execution.


# Main execution -----------------------------------------------------------------------------------------------

if __name__ == "__main__":

    Test1 = FileList(1, "test1")
    #Test1.execute()

    Test2 = RandomFile(2, "test2")
    Test2.execute()
