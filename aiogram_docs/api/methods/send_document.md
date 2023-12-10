# sendDocument

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_document
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_document(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_document import SendDocument`
-   alias: `from aiogram.methods import SendDocument`

#### With specific bot

``` python
result: Message = await bot(SendDocument(...))
```

#### As reply into Webhook in handler

``` python
return SendDocument(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_document`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_document`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_document`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_document_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_document`{.interpreted-text
    role="meth"}
