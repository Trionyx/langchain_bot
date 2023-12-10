# sendMediaGroup

Returns: `List[Message]`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_media_group
:::

## Usage

### As bot method

``` 
result: List[Message] = await bot.send_media_group(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_media_group import SendMediaGroup`
-   alias: `from aiogram.methods import SendMediaGroup`

#### With specific bot

``` python
result: List[Message] = await bot(SendMediaGroup(...))
```

#### As reply into Webhook in handler

``` python
return SendMediaGroup(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_media_group`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_media_group`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_media_group`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_media_group_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_media_group`{.interpreted-text
    role="meth"}
