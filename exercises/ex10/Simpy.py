"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730566154"


class Simpy:
    """Simpy Class with methods."""

    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, values: list[float]):
        """Set a value to a float."""
        self.values = values
        
    def __str__(self) -> str:
        """Will return a string value."""
        return f"Simpy({self.values})"
    
    def fill(self, value: float, count: int) -> None:
        """Allow Simpy's values to be a specific number that repeats values."""
        self.values = [value] * count
        
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Allow the values attribute to be a range."""
        assert step != 0.0, "Step argument cannot be zero."
        # self.values = [i for i in list(float(i) for i in range(int((stop-start)/step))) if i*step < stop-start] + [stop-1e-10]
        if start >= 0:
            while start < stop:
                self.values.append(start)
                start += step
        while start > stop:
            self.values.append(start)
            start += step
        # for i in range(len(self.values)):
        #     self.values[i] += start
            
    def sum(self) -> float:
        """Return the sum of all items in values."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Allow for the use of addition operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for x in self.values:
                result.values.append(x + rhs)
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Simpy objects must have the same length."
            for x in range(len(self.values)):
                new_value = self.values[x] + rhs.values[x]
                result.values.append(new_value)
        else:
            raise TypeError("Unsupported operand type for +")
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Allow for the use of power operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for x in self.values:
                result.values.append(x ** rhs)
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Simpy objects must have the same length."
            for x in range(len(self.values)):
                new = self.values[x] ** rhs.values[x]
                result.values.append(new)
        else:
            raise TypeError("Unsupported operand type for **")
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Allow you to set things equal to one another."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for i in self.values:
                if i == rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Test for the greater than opertaor."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in self.values:
                if i > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allow for subscription notation."""
        if isinstance(rhs, int):
            for i in range(len(self.values)):
                if self.values[i] == self.values[rhs]:
                    return self.values[i]
        else:
            assert len(self.values) == len(rhs)
            result: Simpy = Simpy([]) 
            for i in range(len(self.values)):
                if rhs[i]:
                    result.values.append(self.values[i])
                else:
                    continue
            return result