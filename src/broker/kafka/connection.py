from aiokafka import AIOKafkaProducer

from src.core import KafkaSettings


def get_producer(settings: KafkaSettings) -> AIOKafkaProducer:
    return AIOKafkaProducer(
        bootstrap_servers=settings.get_url
    )