from typing import Union
from pydantic import BaseModel, validator


# without type hinting
# def daily_average(temperatures):
#     return sum(temperatures) / len(temperatures)
# average_temperature = daily_average([22.8, 19.6, 25.9])

# dict_temps = {1: 22.8, 2: 19.6, 3: 25.9}
# sum(dict_temps)
# len(dict_temps)
# average_temperature = daily_average(dict_temps)


# add types
def daily_average(temperatures: list[float]) -> float:
    return sum(temperatures) / len(temperatures)


def sum_ab(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


# daily_average({2: 1, 3: 5})
# causes an error when we run mypy

from datetime import date
from pydantic import BaseModel



class Song(BaseModel):
    id: int
    name: str
    release: date
    genres: list[str]

    # validators to convert fields to lower cases
    @validator('genres', pre=True, always=True)
    def to_lower_case(cls, v):
        return [genre.lower() for genre in v]

    @validator('genres')
    def no_duplicates_in_genre(cls, v):
        if len(set(v)) != len(v):
            raise ValueError(
                'No duplicates allowed in genre.'
            )
        return v

song = Song(
    id=101,
    name='Bohemian Rhapsody',
    release='1975-10-31',
    genres=[
        'Hard Rock',
        # the next line will cause an exception of duplication
        # 'Hard Rock',
        'Progressive Rock'
    ]
)
print(song)

# this will cause an error
# Pydantic is a runtime type checker
song = Song(
    id=101,
    name='Bohemian Rhapsody',
    release='1975-12-31',
    # release='1975-13-31',
    genres=[
        'Hard Rock',
        'Progressive Rock'
    ]
)
print(song)

from typeguard import typechecked

# you can also run typeguard with pytest as well
@typechecked
def f(a: int, b: str, c: float) -> float:
    print(a, b)
    return c

f("d", 1, 2)


@typechecked
class Song3:

    def __init__(
            self,
            id: int,
            name: str,
            release: date,
            genres: list[str]

    ) -> None:
        self.id = id
        self.name = name
        self.release = release
        self.genres = genres


song = Song3(
    id=101,
    name='Bohemian Rhapsody',
    release=date(1975, 10, 31),
    genres={
        'Hard Rock',
        'Progressive Rock',
    }
)
print(song)
