#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "not specified")
text2 = form.getfirst("TEXT_2", "not specified")
text1 = html.escape(text1)
text2 = html.escape(text2)

print("Content-type: text/html\n")
print("""<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
		<title>Forms Data Processing</title>
	</head>
	<body>""")

print("<h1>Forms Data Processing</h1")
print("<p>TEXT_1: {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))

print("""</body>
	</html>""")
