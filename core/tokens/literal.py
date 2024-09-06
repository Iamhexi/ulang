"""Module with literal tokens, such as a number, string, duration, and so on."""
import re
from typing import Self

class Number:
    """
    Literal token of a number type.
     
    Literal numeric token constructed, either of `int` or of `float`.
    Evaluated always as `float`.
    """
    def __init__(self, value: str) -> None:
        self.value = value

    def eval(self) -> float:
        """
        Evaluate value of a number.

        Returns
        -------
        float
            Value of a number.
        """
        return float(self.value)

    def __str__(self) -> str:
        return self.value

class String:
    """Class representing literal of type `string`."""
    def __init__(self, value: str) -> None:
        self.value: str = value.replace('"', '')

    def eval(self) -> str:
        """
        Evaluate value of a literal token of type `string`.

        Returns
        -------
        str
            Literal value of a string.
        """
        return self.value
    
class Duration:
    """Class for literal token representing time spans."""
    def __init__(self, value: str) -> None:
        match = re.match(r'(?:(\d+)h)?(?:(\d+)m)?', value)
        if match:
            self.hours = int(match.group(1)) if match.group(1) else 0  # Default to 0 if not present
            self.minutes = int(match.group(2)) if match.group(2) else 0  # Default to 0 if not present
        else:
            raise ValueError("Invalid duration format.")
        
    def __repr__(self) -> str:
        output = ''
        if self.hours > 0:
            output += str(self.hours) + 'h'
        if self.minutes > 0: 
            output += str(self.minutes) + 'm'
        
        if not output:
            return '0m'
        return output
    
    def __str__(self) -> str:
        return self.__repr__()

    def eval(self) -> Self:
        return self
            

class Time:
    """Class representing time in 24-hour format."""

    def __init__(self, value: str) -> None:
        parts = value.split(':')
        self.hours = int(parts[0])
        self.minutes = int(parts[1])

        if self.hours > 24:
            raise ValueError("Number of hours in time cannot exceed 24.")
        if self.minutes > 60:
            raise ValueError("Number of minutes in time cannot exceed 60.")

    def __sub__(self, other: 'Time') -> Duration:
        minutes_in_hour = 60

        left_in_minutes = self.hours * minutes_in_hour + self.minutes
        right_in_minutes = other.hours * minutes_in_hour + other.minutes
        difference = left_in_minutes - right_in_minutes

        hours, minutes = divmod(difference, minutes_in_hour)
        duration_format = f'{hours}h{minutes}m'
        return Duration(duration_format)

    def __str__(self) -> str:
        return f'{self.hours}:{self.minutes}'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Time):
            return self.hours == other.hours and self.minutes == other.minutes
        return NotImplemented

    def eval(self) -> Self:
        """
        Evaluate time by returing itself.

        Returns
        -------
        Self
            Current instance of `Time` class.
        """
        return self