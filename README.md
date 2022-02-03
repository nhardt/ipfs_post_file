# Playing around with IPFS 

The python client libraries for IPFS that I tried were not compatible with the
0.11 version. IPFS exposes a web API though, so I wanted to see if I could do a
basic to write to IPFS with a python http client.

## Done

* [X] Post the README to the IPFS network, get it from another computer
    * [X] Connect to running IPFS node at localhost:5001
    * [X] Figure out what APIs I need to call
        - https://docs.ipfs.io/reference/http/api/#api-v0-files-write
    * [X] Call them
    * [X] Find the files from another computer or with IPFS web extension

## Code

```python
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
```

## Reference

* https://docs.ipfs.io/reference/cli/#ipfs
* https://docs.python.org/3/library/http.client.html
* https://docs.python-requests.org/en/master/user/quickstart/
