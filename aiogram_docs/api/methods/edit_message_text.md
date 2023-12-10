# editMessageText

Returns: `Union[Message, bool]`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.edit_message_text
:::

## Usage

### As bot method

``` 
result: Union[Message, bool] = await bot.edit_message_text(...)
```

### Method as object

Imports:

-   `from aiogram.methods.edit_message_text import EditMessageText`
-   alias: `from aiogram.methods import EditMessageText`

#### With specific bot

``` python
result: Union[Message, bool] = await bot(EditMessageText(...))
```

#### As reply into Webhook in handler

``` python
return EditMessageText(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.edit_text`{.interpreted-text
    role="meth"}
