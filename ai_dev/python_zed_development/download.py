# 2 download_file_from_google_drive('0B7eQasUpbyfZb04zZ3hJa09yRVk', 'z2.zip')
# 3 download_file_from_google_drive('0B7eQasUpbyfZRENtaE9HeEVzVUE', 'z3.zip')
# 4 download_file_from_google_drive('0B7eQasUpbyfZaFYxUXpzanJOQkU', 'z4.zip')
# 5 download_file_from_google_drive('0B7eQasUpbyfZTExzX1BvVkRlczA', 'z5.zip')
# 6 download_file_from_google_drive('0B7eQasUpbyfZT1ExVXY3bFlKWWs', 'z6.zip')
# source /home/cs231n/myVE35/bin/activate

import requests

def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    


download_file_from_google_drive('0B7eQasUpbyfZb04zZ3hJa09yRVk', 'z2.zip')
download_file_from_google_drive('0B7eQasUpbyfZRENtaE9HeEVzVUE', 'z3.zip')
download_file_from_google_drive('0B7eQasUpbyfZaFYxUXpzanJOQkU', 'z4.zip')
download_file_from_google_drive('0B7eQasUpbyfZTExzX1BvVkRlczA', 'z5.zip')
download_file_from_google_drive('0B7eQasUpbyfZT1ExVXY3bFlKWWs', 'z6.zip')

import os
directory='unzipped'
if not os.path.exists(directory):
    os.makedirs(directory)

import zipfile
for i in range(2,7):
    print('unzipping file z{}.zip'.format(i))
    zip_ref = zipfile.ZipFile('z{}.zip'.format(i), 'r')
    zip_ref.extractall(directory)
    zip_ref.close()

# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) is not 3:
#         print "Usage: python google_drive.py drive_file_id destination_file_path"
#     else:
#         # TAKE ID FROM SHAREABLE LINK
#         file_id = sys.argv[1]
#         # DESTINATION FILE ON YOUR DISK
#         destination = sys.argv[2]
#         download_file_from_google_drive(file_id, destination)