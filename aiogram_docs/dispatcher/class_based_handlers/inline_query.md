# InlineQueryHandler

There is base class for inline query handlers.

## Simple usage

``` python
from aiogram.handlers import InlineQueryHandler

...

@router.inline_query()
class MyHandler(InlineQueryHandler):
    async def handle(self) -> Any: ...
```

## Extension

This base handler is subclass of
`BaseHandler <cbh-base-handler>`{.interpreted-text role="ref"} with some
extensions:

-   `self.chat` is alias for `self.event.chat`
-   `self.query` is alias for `self.event.query`
