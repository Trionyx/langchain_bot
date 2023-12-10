# editMessageReplyMarkup

Returns: `Union[Message, bool]`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.edit_message_reply_markup
:::

## Usage

### As bot method

``` 
result: Union[Message, bool] = await bot.edit_message_reply_markup(...)
```

### Method as object

Imports:

-   `from aiogram.methods.edit_message_reply_markup import EditMessageReplyMarkup`
-   alias: `from aiogram.methods import EditMessageReplyMarkup`

#### With specific bot

``` python
result: Union[Message, bool] = await bot(EditMessageReplyMarkup(...))
```

#### As reply into Webhook in handler

``` python
return EditMessageReplyMarkup(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.edit_reply_markup`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.delete_reply_markup`{.interpreted-text
    role="meth"}
