import numpy as np

def without_brackets(function):
  return function()
   
@without_brackets
def HelloWorld():
  return 'Hello World!'
  
print(HelloWorld)
