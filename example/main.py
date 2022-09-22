import logging
from example.add import pipeline
from sematic import CloudResolver

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    future = pipeline(1, 2, 3).set(
        name="Basic add example pipeline", tags=["example", "basic", "final"]
    )

    resolver = None
    resolver = CloudResolver()
    result = future.resolve(resolver)

    logging.info(result)
