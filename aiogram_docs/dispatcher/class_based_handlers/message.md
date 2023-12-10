# MessageHandler

There is base class for message handlers.

## Simple usage

``` python
from aiogram.handlers import MessageHandler

...

@router.message()
class MyHandler(MessageHandler):
    async def handle(self) -> Any:
        return SendMessage(chat_id=self.chat.id, text="PASS")
```

## Extension

This base handler is subclass of
`BaseHandler <cbh-base-handler>`{.interpreted-text role="ref"} with some
extensions:

-   `self.chat` is alias for `self.event.chat`
-   `self.from_user` is alias for `self.event.from_user`
