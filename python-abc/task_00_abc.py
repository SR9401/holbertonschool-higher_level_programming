#!/usr/bin/env python3
"""Abstract Base Classes (ABCs)"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """class animal"""
    @abstractmethod
    def sound(self):
        """declare an abstract method named sound"""

        pass


class Dog(Animal):
    """class dog inherits from abstract class animal  """
    def sound(self):
        """astarct method for dog"""
        return "Bark"


class Cat(Animal):
    """class cat inherits from abstarct class Animal """
    def sound(self):
        """abstarct method for cat"""
        return "Meow"
