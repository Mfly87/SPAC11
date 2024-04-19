from multiprocessing.pool import ThreadPool, Pool
from multiprocessing import cpu_count

from typing import Callable, TypeVar
import tqdm

T = TypeVar("T")

class ThreadPoolHandler():

    def map_unordered(self, func: Callable[[T], None], list_of_args: list[T]):
        _len = len(list_of_args)
        '''
        _cpu_count = max(1, cpu_count() - 1)

        with Pool(processes=_cpu_count) as pool:
            _map = pool.imap_unordered(func, list_of_args)
            for _ in tqdm.tqdm(_map, total=_len):
                pass
        '''
        
        with ThreadPool() as pool:
            _map = pool.imap_unordered(func, list_of_args)

            for _ in tqdm.tqdm(_map, total=_len):
                pass