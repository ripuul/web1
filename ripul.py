#!python
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
else:
    pageId = 'Welcome'
print('''<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <body>
      <h1><a href="ripul.py">This is ripul_s tap</a></h1>
      <ol>
        <li><a href="ripul.py?id=1">Tap 1</a></li>
        <li><a href="ripul.py?id=2">Tap 2</a></li>
        <li><a href="ripul.py?id=3">Tap 3</a></li>
        <h2>{prepare}</h2>
        <p> hello~~~</p>
      </ol>
    </body>
  </head>
</html>
'''.format(prepare=pageId))
