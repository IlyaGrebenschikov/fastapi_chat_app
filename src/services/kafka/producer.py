from aiokafka import AIOKafkaProducer

from src.broker.kafka import Manager
from src.services.common.converters import dump_value_orjson


class ProducerService(Manager):
    def __init__(self, client: AIOKafkaProducer):
        super().__init__(client)

    async def send(self, topic: str, value: dict) -> None:
        await self._client.send(topic, dump_value_orjson(value))
