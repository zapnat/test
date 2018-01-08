
import sys
import os


for x in sys.path:
  print(x)
  
def print_path():
  "function to print path"
  print(os.environ['PATH'])
  
print_path()
