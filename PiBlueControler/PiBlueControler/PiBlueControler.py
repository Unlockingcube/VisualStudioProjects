import optparse
import argparse
import os
import glob

print(os.listdir())
print(glob.glob)
print("Enter the Exact directory of the file you want to open.")
directory = input()
print(glob.glob(directory))
filename = input()
print(filename)
