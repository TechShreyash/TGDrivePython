# a simple demo showing how to access tg drive api and add remote upload tasks
# this shows how to add multiple remote upload tasks, you can later view the files in the website

tgdrive_url = "http://tgdrive.37.44.244.56.sslip.io"
admin_password = "admin"
file_info_api = tgdrive_url + "/api/getFileInfoFromUrl"
start_remote_upload_api = tgdrive_url + "/api/startFileDownloadFromUrl"
download_progress_api = tgdrive_url + "/api/getFileDownloadProgress"
upload_progress_api = tgdrive_url + "/api/getUploadProgress"

file_download_url_list = []

with open("links.txt", "r") as f:
    file_download_url_list = f.readlines()

import requests


for file_download_url in file_download_url_list:
    file_download_url = file_download_url.strip()
    print('Processing:', file_download_url)
    # get file info
    print("Getting file info")

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
    print("Starting remote upload")

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
    json = r.json()
    print(json)
