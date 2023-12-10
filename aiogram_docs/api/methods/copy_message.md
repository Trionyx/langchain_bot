# copyMessage

Returns: `MessageId`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.copy_message
:::

## Usage

### As bot method

``` 
result: MessageId = await bot.copy_message(...)
```

### Method as object

Imports:

-   `from aiogram.methods.copy_message import CopyMessage`
-   alias: `from aiogram.methods import CopyMessage`

#### With specific bot

``` python
result: MessageId = await bot(CopyMessage(...))
```

#### As reply into Webhook in handler

``` python
return CopyMessage(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.copy_to`{.interpreted-text
    role="meth"}
