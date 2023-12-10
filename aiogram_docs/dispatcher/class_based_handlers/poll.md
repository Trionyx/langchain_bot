# PollHandler

There is base class for poll handlers.

## Simple usage

``` python
from aiogram.handlers import PollHandler

...

@router.poll()
class MyHandler(PollHandler):
    async def handle(self) -> Any: ...
```

## Extension

This base handler is subclass of
`BaseHandler <cbh-base-handler>`{.interpreted-text role="ref"} with some
extensions:

-   `self.question` is alias for `self.event.question`
-   `self.options` is alias for `self.event.options`
