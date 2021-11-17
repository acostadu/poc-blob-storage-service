import os

from azure.storage.blob import BlockBlobService
from dotenv import load_dotenv

load_dotenv(os.getenv('CURRENT_ENV_DIR'))


def run_sample():
    try:
        block_blob_service = BlockBlobService(
            account_name=os.getenv('AZURE_STORAGE_ACOUNT'),
            account_key=os.getenv('AZURE_STORAGE_KEY')
        )

        container_name = os.getenv('AZURE_STORAGE_CONTAINER')
        local_path = os.path.abspath(os.path.curdir)
        local_file_name = 'CDN_26062021_RE_761349465.dat'

        full_path_to_file2 = os.path.join(f'{local_path}/data', local_file_name)
        block_blob_service.get_blob_to_path(container_name, local_file_name, full_path_to_file2)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    run_sample()
