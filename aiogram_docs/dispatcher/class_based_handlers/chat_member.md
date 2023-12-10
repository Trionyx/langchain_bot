# ChatMemberHandler

There is base class for chat member updated events.

## Simple usage

``` python
from aiogram.handlers import ChatMemberHandler

...

@router.chat_member()
@router.my_chat_member()
class MyHandler(ChatMemberHandler):
    async def handle(self) -> Any: ...
```

## Extension

This base handler is subclass of
`BaseHandler <cbh-base-handler>`{.interpreted-text role="ref"} with some
extensions:

-   `self.chat` is alias for `self.event.chat`
