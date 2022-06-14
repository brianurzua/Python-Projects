import webbrowser as wb
import time

with open('amazing.html', 'r+') as a:
	html_template = """<html>\n
	<body>\n
	<h1>\n
	Stay tuned for our amazing summer sale!\n
	</h1>\n
	</body>\n
</html> """

	a.write(html_template)

def OpenBrowser():
	wb.open('amazing.html')

""" This close() will clear the file. """
# open('amazing.html', 'w').close()

if __name__ == '__main__':
	OpenBrowser()




