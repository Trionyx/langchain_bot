# sendLocation

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_location
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_location(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_location import SendLocation`
-   alias: `from aiogram.methods import SendLocation`

#### With specific bot

``` python
result: Message = await bot(SendLocation(...))
```

#### As reply into Webhook in handler

``` python
return SendLocation(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_location`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_location`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_location`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_location_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_location`{.interpreted-text
    role="meth"}
