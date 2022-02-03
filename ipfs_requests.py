#!/usr/bin/python3

import requests
import dumper

# post should look like:
# Abspath: /absolute/path/to/file.txt
# Content-Disposition: form-data; name="file"; filename="folderName%2Ffile.txt"
# Content-Type: application/octet-stream
# 
# ...contents...

files = {'file': open('README.md', 'rb')}
params = { "arg": "/README", "create" : "1"}
r = requests.post('http://localhost:5001/api/v0/files/write', params=params,
        files=files)

dumper.dump(r)

