run_kafka:
	docker-compose -f docker/kafka-compose.yml up -d

run_collector:
	pipenv run python main.py
