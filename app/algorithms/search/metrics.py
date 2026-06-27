import time
import tracemalloc


class Metrics:

    @staticmethod
    def evaluate(search_function):

        tracemalloc.start()

        start_time = time.time()

        result = search_function()

        end_time = time.time()

        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        return {
            "result": result,
            "time_seconds": end_time - start_time,
            "memory_bytes": peak
        }