# WebApp

Telegram Bot API 6.0 announces a revolution in the development of
chatbots using WebApp feature.

You can read more details on it in the official
[blog](https://telegram.org/blog/notifications-bots#bot-revolution) and
[documentation](https://core.telegram.org/bots/webapps).

[aiogram]{.title-ref} implements simple utils to remove headache with
the data validation from Telegram WebApp on the backend side.

## Usage

For example from frontend you will pass
`application/x-www-form-urlencoded` POST request with `_auth` field in
body and wants to return User info inside response as `application/json`

``` python
from aiogram.utils.web_app import safe_parse_webapp_init_data
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

async def check_data_handler(request: Request):
    bot: Bot = request.app["bot"]

    data = await request.post()  # application/x-www-form-urlencoded
    try:
        data = safe_parse_webapp_init_data(token=bot.token, init_data=data["_auth"])
    except ValueError:
        return json_response({"ok": False, "err": "Unauthorized"}, status=401)
    return json_response({"ok": True, "data": data.user.dict()})
```

## Functions

::: autofunction
aiogram.utils.web_app.check_webapp_signature
:::

::: autofunction
aiogram.utils.web_app.parse_webapp_init_data
:::

::: autofunction
aiogram.utils.web_app.safe_parse_webapp_init_data
:::

## Types

::: {.autoclass members="" member-order="bysource" undoc-members="True"}
aiogram.utils.web_app.WebAppInitData
:::

::: {.autoclass members="" member-order="bysource" undoc-members="True"}
aiogram.utils.web_app.WebAppUser
:::
