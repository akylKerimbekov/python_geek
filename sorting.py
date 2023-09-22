from __future__ import annotations

from abc import ABC, abstractmethod


class Sorting:

    def __init__(self, strategy: SortingStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> SortingStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: SortingStrategy) -> None:
        self._strategy = strategy

    def process(self, raw_list: list) -> list:
        return self._strategy.sorting(raw_list)


class SortingStrategy(ABC):
    @abstractmethod
    def sorting(self, raw: list) -> list:
        pass


class BubbleSorting(SortingStrategy):
    def sorting(self, raw: list) -> list:
        array = raw[:]
        array_length = len(array) - 1
        for i in range(0, array_length):
            for j in range(array_length):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array


class SelectionSorting(SortingStrategy):
    def sorting(self, raw: list) -> list:
        array = raw[:]
        n = len(array)
        for i in range(n - 1):
            min_value_index = i

            for j in range(i + 1, n):
                if array[j] < array[min_value_index]:
                    min_value_index = j

            if min_value_index != i:
                temp = array[i]
                array[i] = array[min_value_index]
                array[min_value_index] = temp

        return array

