# BaseHandler {#cbh-base-handler}

Base handler is generic abstract class and should be used in all other
class-based handlers.

Import: `from aiogram.handlers import BaseHandler`

By default you will need to override only method
`async def handle(self) -> Any: ...`

This class also has a default initializer and you don\'t need to change
it. The initializer accepts the incoming event and all contextual data,
which can be accessed from the handler through attributes:
`event: TelegramEvent` and `data: Dict[Any, str]`

If an instance of the bot is specified in context data or current
context it can be accessed through *bot* class attribute.

## Example

``` python
class MyHandler(BaseHandler[Message]):
    async def handle(self) -> Any:
         await self.event.answer("Hello!")
```
