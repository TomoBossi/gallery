import os
os.chdir(os.path.dirname(__file__))
path = "./images/display/"
images = [path+img for img in sorted(os.listdir(path))][::-1]
for i, path in enumerate(images):
    if i > 0:
        title = path.split(" ")[-1][:-4]
        if title == images[i-1].split(" ")[-1][:-7]:
            images.insert(i-1, images.pop(i))

for path in images:
    domstring = f"<img class=\"display\" src=\"{path}\">"
    title = path.split(" ")[-1][:-4]
    date = path.split(" ")[-2][-12:-4]
    date = date[:4] + "/" + date[4:6] + "/" + date[6:]
    print(f"<div class=\"tile\" id=\"{title}\">")
    print("  " + domstring)
    print("  " + f"<p class=\"date\">{date}</p>")
    print("  " + "<p class=\"tools\"> </p>")
    print("  " + "<p class=\"comment\"> </p>")
    print("  " + "<p class=\"resources\"> </p>")
    print("</div>")