# deleteMessage

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.delete_message
:::

## Usage

### As bot method

``` 
result: bool = await bot.delete_message(...)
```

### Method as object

Imports:

-   `from aiogram.methods.delete_message import DeleteMessage`
-   alias: `from aiogram.methods import DeleteMessage`

#### With specific bot

``` python
result: bool = await bot(DeleteMessage(...))
```

#### As reply into Webhook in handler

``` python
return DeleteMessage(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.delete_message`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.delete`{.interpreted-text
    role="meth"}
