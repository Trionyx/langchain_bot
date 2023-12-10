# Use Custom API server

For example, if you want to use self-hosted API server:

``` python
session = AiohttpSession(
    api=TelegramAPIServer.from_base('http://localhost:8082')
)
bot = Bot(..., session=session)
```

::: {.autoclass members=""}
aiogram.client.telegram.TelegramAPIServer
:::
