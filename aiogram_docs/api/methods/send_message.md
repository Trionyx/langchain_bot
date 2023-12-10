# sendMessage

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_message
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_message(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_message import SendMessage`
-   alias: `from aiogram.methods import SendMessage`

#### With specific bot

``` python
result: Message = await bot(SendMessage(...))
```

#### As reply into Webhook in handler

``` python
return SendMessage(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply`{.interpreted-text role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer`{.interpreted-text
    role="meth"}
