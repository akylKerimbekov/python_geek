from __future__ import annotations

from abc import ABC, abstractmethod


class Searching:

    def __init__(self, strategy: SearchingStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> SearchingStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: SearchingStrategy) -> None:
        self._strategy = strategy

    def process(self, raw_list: list, val: int):
        self._strategy.searching(raw_list, val)


class SearchingStrategy(ABC):
    @abstractmethod
    def searching(self, array: list, val: int) -> list:
        pass


class BinarySearching(SearchingStrategy):
    def searching(self, array: list, val: int):
        n = len(array)
        result_ok = False
        first = 0
        last = n - 1
        pos = -1
        while first < last:
            middle = (first + last) // 2
            if val == array[middle]:
                first = middle
                last = first
                result_ok = True
                pos = middle
            else:
                if val > array[middle]:
                    first = middle + 1
                else:
                    last = middle - 1

        if result_ok:
            print(f'element {val} was found in position {pos}')
        else:
            print(f'element was not found')
