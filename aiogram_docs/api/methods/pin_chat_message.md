# pinChatMessage

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.pin_chat_message
:::

## Usage

### As bot method

``` 
result: bool = await bot.pin_chat_message(...)
```

### Method as object

Imports:

-   `from aiogram.methods.pin_chat_message import PinChatMessage`
-   alias: `from aiogram.methods import PinChatMessage`

#### With specific bot

``` python
result: bool = await bot(PinChatMessage(...))
```

#### As reply into Webhook in handler

``` python
return PinChatMessage(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.pin_message`{.interpreted-text role="meth"}
-   `aiogram.types.message.Message.pin`{.interpreted-text role="meth"}
