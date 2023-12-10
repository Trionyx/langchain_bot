# forwardMessage

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.forward_message
:::

## Usage

### As bot method

``` 
result: Message = await bot.forward_message(...)
```

### Method as object

Imports:

-   `from aiogram.methods.forward_message import ForwardMessage`
-   alias: `from aiogram.methods import ForwardMessage`

#### With specific bot

``` python
result: Message = await bot(ForwardMessage(...))
```

#### As reply into Webhook in handler

``` python
return ForwardMessage(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.forward`{.interpreted-text
    role="meth"}
