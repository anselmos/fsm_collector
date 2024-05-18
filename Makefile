run_kafka:
	docker compose -f docker/kafka-compose.yml up -d

run_collector:
	pipenv run python main.py

create_topic:
	pipenv run python create_topic.py
