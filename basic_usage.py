# a simple demo showing how to access tg drive api and add remote upload tasks

tgdrive_url = "http://tgdrive.37.44.244.56.sslip.io"
admin_password = "admin"
file_info_api = tgdrive_url + "/api/getFileInfoFromUrl"
start_remote_upload_api = tgdrive_url + "/api/startFileDownloadFromUrl"

file_download_url = "https://vadapav.mov/f/e38a65d9-414b-4009-8f1c-f136dad07b76/"

import requests

# get file info

r = requests.post(
    file_info_api,
    json={
        "url": file_download_url,
        "password": admin_password,
    },
)
json = r.json()
print(json)

file_name = json["data"]["file_name"]
file_size = json["data"]["file_size"]


# start remote upload

r = requests.post(
    start_remote_upload_api,
    json={
        "filename": file_name,
        "password": admin_password,
        "path": "/",
        "singleThreaded": True,
        "url": file_download_url,
    },
)
