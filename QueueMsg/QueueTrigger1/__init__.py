import logging
import os
import azure.functions as func
import utils.storage_helpers as storage_helpers


def main(msg: func.QueueMessage) -> None:
    file_name = msg.get_body().decode('utf-8')
    logging.info(f"Processing queue item: {file_name}…")
    # Getting settings
    STORAGE_CONNECTION_STRING = os.getenv("AzureWebJobsStorage")
    CONTAINER_NAME = os.getenv("STORAGE_CONTAINER_NAME")
    # Getting file from storage
    file_path = storage_helpers.download_blob(CONTAINER_NAME, file_name, STORAGE_CONNECTION_STRING)
