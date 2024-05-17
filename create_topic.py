from constants import KAFKA_TOPIC
from kafka.admin import KafkaAdminClient, NewTopic


admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id='test'
)

topic_list = []
# TODO make more then 2 partition in future
topic_list.append(NewTopic(name=KAFKA_TOPIC, num_partitions=2, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)
