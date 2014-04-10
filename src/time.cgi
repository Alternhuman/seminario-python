#!/usr/bin/env python3

import time
print("Content-Type: text/html\n\n")

tiempo = time.strftime("%c")

htmlFormat = """
<html>
	<Title>The time is a-changin'</Title>
<body>
	<p>La hora actual es: {tiempo}</p>
</body>
</html> """

print(htmlFormat.format(**locals()))

