# Chat action sender

## Sender

::: {.autoclass members="__init__,running,typing,upload_photo,record_video,upload_video,record_voice,upload_voice,upload_document,choose_sticker,find_location,record_video_note,upload_video_note"}
aiogram.utils.chat_action.ChatActionSender
:::

### Usage

``` python
async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
    # Do something...
    # Perform some long calculations
    await message.answer(result)
```

## Middleware

::: autoclass
aiogram.utils.chat_action.ChatActionMiddleware
:::

### Usage

Before usa should be registered for the [message]{.title-ref} event

``` python
<router or dispatcher>.message.middleware(ChatActionMiddleware())
```

After this action all handlers which works longer than
[initial_sleep]{.title-ref} will produce the \'[typing]{.title-ref}\'
chat action.

Also sender can be customized via flags feature for particular handler.

Change only action type:

``` python
@router.message(...)
@flags.chat_action("sticker")
async def my_handler(message: Message): ...
```

Change sender configuration:

``` python
@router.message(...)
@flags.chat_action(initial_sleep=2, action="upload_document", interval=3)
async def my_handler(message: Message): ...
```
