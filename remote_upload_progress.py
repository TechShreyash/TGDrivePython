# a simple demo showing how to access tg drive api and add remote upload tasks
# this also shows how to get download and upload progress

tgdrive_url = "http://tgdrive.37.44.244.56.sslip.io"
admin_password = "admin"
file_info_api = tgdrive_url + "/api/getFileInfoFromUrl"
start_remote_upload_api = tgdrive_url + "/api/startFileDownloadFromUrl"
download_progress_api = tgdrive_url + "/api/getFileDownloadProgress"
upload_progress_api = tgdrive_url + "/api/getUploadProgress"

file_download_url = "https://vadapav.mov/f/e38a65d9-414b-4009-8f1c-f136dad07b76/"

import requests, time

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

id = json["id"]

time.sleep(3)  # wait for download to start

# get download progress
print("Download started")

while True:

    r = requests.post(
        download_progress_api,
        json={
            "id": id,
            "password": admin_password,
        },
    )
    json = r.json()
    data = json["data"]
    # print(data)

    if data[0] == "completed":
        break
    elif data[0] == "error":
        raise Exception("Download failed")
    else:
        status = data[0]
        done = data[1]
        total = data[2] or 1
        print(f"{status}: {done}/{total} ({done/total*100:.2f}%)")

    time.sleep(1)

print("Download completed")
time.sleep(3)  # wait for upload to start

# get upload progress
print("Upload started")

while True:

    r = requests.post(
        upload_progress_api,
        json={
            "id": id,
            "password": admin_password,
        },
    )
    json = r.json()
    data = json["data"]
    # print(data)

    if data[0] == "completed":
        break
    else:
        status = data[0]
        done = data[1]
        total = data[2] or 1
        print(f"Uploading: {done}/{total} ({done/total*100:.2f}%)")

    time.sleep(1)

print("Upload completed")
