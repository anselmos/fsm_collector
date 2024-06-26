from os import walk, path
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from constants import KAFKA_TOPIC, INIT_PATH, BATCH_LIMIT
import json

def get_producer():
    return KafkaProducer(bootstrap_servers=['localhost:9092'])

def produce_new_file(kafka_producer, batch_paths, partition_id):
    data = {
        "batch": batch_paths,
    }
    kafka_producer.send(KAFKA_TOPIC, bytes(json.dumps(data), 'utf-8'), partition=partition_id)
    kafka_producer.flush()


def enumerate_files(init_path=None):

    if not init_path:
        raise ValueError("No init_path provided - or not available at .env")
    for (root, dirnames, filenames) in walk(init_path):
        for filename in filenames:
            yield path.join(root, filename)

def main():
    kafka_producer = get_producer()
    counter = 0
    batch_counter = 0
    batch_paths = []
    for path in enumerate_files(INIT_PATH):
        batch_paths.append(path)
        if batch_counter == BATCH_LIMIT:
            # TODO make more then 2 partition in future
            partition_id = 1 if bool(counter%2) else 0
            print(f"PART: {partition_id}, BATCH: {batch_counter}")
            produce_new_file(kafka_producer, batch_paths, partition_id)
            counter += 1
            batch_counter = 0
            batch_paths = []

        batch_counter +=1

if __name__ == '__main__':
    main()
