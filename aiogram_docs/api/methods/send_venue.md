# sendVenue

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_venue
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_venue(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_venue import SendVenue`
-   alias: `from aiogram.methods import SendVenue`

#### With specific bot

``` python
result: Message = await bot(SendVenue(...))
```

#### As reply into Webhook in handler

``` python
return SendVenue(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_venue`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_venue`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_venue`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_venue_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_venue`{.interpreted-text
    role="meth"}
