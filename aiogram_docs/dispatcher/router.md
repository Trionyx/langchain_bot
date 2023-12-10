# Router {#Router}

Usage:

``` python
from aiogram import Router
from aiogram.types import Message

my_router = Router(name=__name__)

@my_router.message()
async def message_handler(message: Message) -> Any:
    await message.answer('Hello from my router!')
```

::: {.autoclass members="__init__, include_router, include_routers, resolve_used_update_types" show-inheritance=""}
aiogram.dispatcher.router.Router
:::

## Event observers {#Event observers}

::: warning
::: title
Warning
:::

All handlers always should be asynchronous. The name of the handler
function is not important. The event argument name is also not important
but it is recommended to not overlap the name with contextual data in
due to function can not accept two arguments with the same name.
:::

Here is the list of available observers and examples of how to register
handlers

In these examples only decorator-style registering handlers are used,
but if you don\'t like \@decorators just use
`<event type>.register(...)`{.interpreted-text role="obj"} method
instead.

### Message

::: attention
::: title
Attention
:::

Be attentive with filtering this event

You should expect that this event can be with different sets of
attributes in different cases

(For example text, sticker and document are always of different content
types of message)

Recommended way to check field availability before usage, for example
via `magic filter <magic-filters>`{.interpreted-text role="ref"}:
`F.text` to handle text, `F.sticker` to handle stickers only and etc.
:::

``` python
@router.message()
async def message_handler(message: types.Message) -> Any: pass
```

### Edited message

``` python
@router.edited_message()
async def edited_message_handler(edited_message: types.Message) -> Any: pass
```

### Channel post

``` python
@router.channel_post()
async def channel_post_handler(channel_post: types.Message) -> Any: pass
```

### Edited channel post

``` python
@router.edited_channel_post()
async def edited_channel_post_handler(edited_channel_post: types.Message) -> Any: pass
```

### Inline query

``` python
@router.inline_query()
async def inline_query_handler(inline_query: types.InlineQuery) -> Any: pass
```

### Chosen inline query

``` python
@router.chosen_inline_result()
async def chosen_inline_result_handler(chosen_inline_result: types.ChosenInlineResult) -> Any: pass
```

### Callback query

``` python
@router.callback_query()
async def callback_query_handler(callback_query: types.CallbackQuery) -> Any: pass
```

### Shipping query

``` python
@router.shipping_query()
async def shipping_query_handler(shipping_query: types.ShippingQuery) -> Any: pass
```

### Pre checkout query

``` python
@router.pre_checkout_query()
async def pre_checkout_query_handler(pre_checkout_query: types.PreCheckoutQuery) -> Any: pass
```

### Poll

``` python
@router.poll()
async def poll_handler(poll: types.Poll) -> Any: pass
```

### Poll answer

``` python
@router.poll_answer()
async def poll_answer_handler(poll_answer: types.PollAnswer) -> Any: pass
```

### Errors

``` python
@router.errors()
async def error_handler(exception: ErrorEvent) -> Any: pass
```

Is useful for handling errors from other handlers, error event described
`here <error-event>`{.interpreted-text role="ref"}

## Nested routers {#Nested routers}

::: warning
::: title
Warning
:::

Routers by the way can be nested to an another routers with some limitations:

:   1.  Router **CAN NOT** include itself
    2.  Routers **CAN NOT** be used for circular including (router 1
        include router 2, router 2 include router 3, router 3 include
        router 1)
:::

Example:

``` {#module_1 .python caption="module_1.py"}
router2 = Router()

@router2.message()
...
```

``` {#module_2 .python caption="module_2.py"}
from module_2 import router2


router1 = Router()
router1.include_router(router2)
```

### Update

``` python
@dispatcher.update()
async def message_handler(update: types.Update) -> Any: pass
```

::: warning
::: title
Warning
:::

The only root Router (Dispatcher) can handle this type of event.
:::

::: note
::: title
Note
:::

Dispatcher already has default handler for this event type, so you can
use it for handling all updates that are not handled by any other
handlers.
:::

### How it works?

For example, dispatcher has 2 routers, the last router also has one
nested router:

![Nested routers example](../_static/nested_routers_example.png)

In this case update propagation flow will have form:

![Nested routers example](../_static/update_propagation_flow.png)
