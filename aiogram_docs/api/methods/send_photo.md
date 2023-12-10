# sendPhoto

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_photo
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_photo(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_photo import SendPhoto`
-   alias: `from aiogram.methods import SendPhoto`

#### With specific bot

``` python
result: Message = await bot(SendPhoto(...))
```

#### As reply into Webhook in handler

``` python
return SendPhoto(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_photo`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_photo`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_photo`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_photo_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_photo`{.interpreted-text
    role="meth"}
