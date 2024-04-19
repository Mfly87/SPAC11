from multiprocessing.pool import ThreadPool, Pool
from multiprocessing import cpu_count

from typing import Callable, TypeVar
import tqdm

T = TypeVar("T")

class ThreadPoolHandler():

    def map_unordered(self, func: Callable[[T], None], list_of_args: list[T]):
        _len = len(list_of_args)
        
        with ThreadPool() as pool:
            _map = pool.imap_unordered(func, list_of_args)

            for _ in tqdm.tqdm(_map, total=_len):
                pass