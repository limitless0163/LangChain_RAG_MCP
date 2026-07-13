from typing import Annotated, TypedDict


# Annotated 本身不具备运行时校验能力
Age = Annotated[int, "年龄，范围0-150"]

class Person(TypedDict):
    name: str
    age: int
    age2: Age

p = Person(name="z3", age=111, age2=188)
print(p)

