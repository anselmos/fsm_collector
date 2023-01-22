from os import walk, path
from kafka import KafkaProducer
from constants import KAFKA_TOPIC, INIT_PATH

def get_producer():
    return KafkaProducer(bootstrap_servers=['localhost:9092'])

def produce_new_file(kafka_producer, path):
    kafka_producer.send(KAFKA_TOPIC, bytes(path, 'utf-8'))
    kafka_producer.flush()


def enumerate_files(init_path=None):

    if not init_path:
        raise ValueError("No init_path provided - or not available at .env")
    for (root, dirnames, filenames) in walk(init_path):
        print(root)
        for filename in filenames:
            yield path.join(root, filename)

def main():
    kafka_producer = get_producer()
    for path in enumerate_files(INIT_PATH):
        produce_new_file(kafka_producer, path)

if __name__ == '__main__':
    main()
