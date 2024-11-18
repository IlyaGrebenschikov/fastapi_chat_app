from aiokafka import AIOKafkaProducer, AIOKafkaConsumer


class Manager:
    def __init__(self, client: AIOKafkaProducer | AIOKafkaConsumer):
        self._client = client

    async def __aenter__(self) -> None:
        await self._client.start()

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._client.stop()
