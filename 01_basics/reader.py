""" 
Read the `data.json` file and print the file contents in console
Keyword to search: python read text file
"""

with open('data.json') as f:
  f = open('child/data.json')
  file_content = f.read()
  print(file_content)