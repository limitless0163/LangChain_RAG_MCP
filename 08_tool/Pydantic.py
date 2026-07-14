from pydantic import BaseModel, ValidationError, StrictInt


class User(BaseModel):
    id: StrictInt   # 改用严格整数类型，拒绝类型转换
    name: str
    age: int = 0    # 默认值

try:
    u = User(id=42, name="z3")
except ValidationError as e:
    print(e)

print()

# 传错类型就报错 id: StrictInt
try:
    User(id="abc", name="Bob")
except ValidationError as e:
    print(e)
