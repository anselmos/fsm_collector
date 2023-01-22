import os
from dotenv import load_dotenv
load_dotenv()

KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'fsm_file_path')
INIT_PATH = os.getenv('INIT_PATH')
