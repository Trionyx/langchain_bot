# sendSticker

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_sticker
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_sticker(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_sticker import SendSticker`
-   alias: `from aiogram.methods import SendSticker`

#### With specific bot

``` python
result: Message = await bot(SendSticker(...))
```

#### As reply into Webhook in handler

``` python
return SendSticker(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_sticker`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_sticker`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_sticker`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_sticker_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_sticker`{.interpreted-text
    role="meth"}
