import sys
import webbrowser
import os

WEB_SOURCE = sys.argv[1]
WEB_TEMPLATE = sys.argv[2]
WEB_OUTPUT = sys.argv[3]

script = open(WEB_SOURCE).read()
tpl = open(WEB_TEMPLATE).read()
out_text = tpl.format(script=script)

output_directory = os.path.join('.', 'output')
web_directory = os.path.join(output_directory, 'web')

os.makedirs(output_directory, exist_ok=True)

os.makedirs(web_directory, exist_ok=True)

web_path = web_directory + WEB_OUTPUT
open(web_path, 'w').write(out_text)
webbrowser.open(web_path)
