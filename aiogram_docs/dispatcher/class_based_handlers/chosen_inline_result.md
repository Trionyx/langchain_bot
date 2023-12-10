# ChosenInlineResultHandler

There is base class for chosen inline result handlers.

## Simple usage

``` python
from aiogram.handlers import ChosenInlineResultHandler

...

@router.chosen_inline_result()
class MyHandler(ChosenInlineResultHandler):
    async def handle(self) -> Any: ...
```

## Extension

This base handler is subclass of
`BaseHandler <cbh-base-handler>`{.interpreted-text role="ref"} with some
extensions:

-   `self.chat` is alias for `self.event.chat`
-   `self.from_user` is alias for `self.event.from_user`
