import os
from pathlib import Path
from typing import Optional

import typer
from azure.storage.blob import BlockBlobService
from dotenv import load_dotenv

load_dotenv(os.getenv('CURRENT_ENV_DIR'), '.env')

app = typer.Typer()


@app.command("read")
def cli_read_from(file_name: str):
    """
    To read from Azure Blob Storage any file name passed by parameter.
    """
    try:
        block_blob_service = BlockBlobService(
            account_name=os.getenv('AZURE_STORAGE_ACOUNT'),
            account_key=os.getenv('AZURE_STORAGE_KEY')
        )

        container_name = os.getenv('AZURE_STORAGE_CONTAINER')
        local_path = os.path.abspath(os.path.curdir)

        full_path_to_file2 = os.path.join(f'{local_path}/data', file_name)
        block_blob_service.get_blob_to_path(container_name, file_name, full_path_to_file2)

    except Exception as ex:
        print(ex)


@app.command("write")
def cli_write_to(file_path: Optional[Path] = typer.Option(None)):
    """
    To write to an Azure Blob storage any file path passed by parameter
    """
    pass


if __name__ == "__main__":
    app()
