# unpinChatMessage

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.unpin_chat_message
:::

## Usage

### As bot method

``` 
result: bool = await bot.unpin_chat_message(...)
```

### Method as object

Imports:

-   `from aiogram.methods.unpin_chat_message import UnpinChatMessage`
-   alias: `from aiogram.methods import UnpinChatMessage`

#### With specific bot

``` python
result: bool = await bot(UnpinChatMessage(...))
```

#### As reply into Webhook in handler

``` python
return UnpinChatMessage(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.unpin_message`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.unpin`{.interpreted-text role="meth"}
