import dashscope
from http import HTTPStatus


input_text = "衣服的质量杠杠的"

resp = dashscope.TextEmbedding.call(
    model="text-embedding-v4",
    input=input_text,
)

if resp.status_code == HTTPStatus.OK:
    print(resp)

    