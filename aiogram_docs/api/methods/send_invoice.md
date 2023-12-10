# sendInvoice

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_invoice
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_invoice(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_invoice import SendInvoice`
-   alias: `from aiogram.methods import SendInvoice`

#### With specific bot

``` python
result: Message = await bot(SendInvoice(...))
```

#### As reply into Webhook in handler

``` python
return SendInvoice(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_invoice`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_invoice`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_invoice`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_invoice_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_invoice`{.interpreted-text
    role="meth"}
