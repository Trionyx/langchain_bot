# sendContact

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_contact
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_contact(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_contact import SendContact`
-   alias: `from aiogram.methods import SendContact`

#### With specific bot

``` python
result: Message = await bot(SendContact(...))
```

#### As reply into Webhook in handler

``` python
return SendContact(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_contact`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_contact`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_contact`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_contact_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_contact`{.interpreted-text
    role="meth"}
