import os
os.chdir(os.path.dirname(__file__))
path = "./images/display/"
images = [path+img for img in sorted(os.listdir(path))][::-1]
domstrings = [f"<img class=\"display\" src=\"{img}\">" for img in images]
for string in domstrings:
  print(string)