# https://leetcode.com/problems/sort-the-people/

from dataclasses import dataclass
from typing import List


@dataclass
class Person:
    name: str
    height: int


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [Person(name, height) for name, height in zip(names, heights)]
        people.sort(key=lambda value: getattr(value, 'height'), reverse=True)
        return [person.name for person in people]
