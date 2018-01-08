
import sys
import os

for x in sys.path:
  print(x)
  
print()

for x in os.environ['PATH'].split(';'):
  print(x)
