import orjson


def dump_value_orjson(value: dict) -> bytes:
    return orjson.dumps(value)
