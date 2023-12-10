# sendChatAction

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_chat_action
:::

## Usage

### As bot method

``` 
result: bool = await bot.send_chat_action(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_chat_action import SendChatAction`
-   alias: `from aiogram.methods import SendChatAction`

#### With specific bot

``` python
result: bool = await bot(SendChatAction(...))
```

#### As reply into Webhook in handler

``` python
return SendChatAction(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.do`{.interpreted-text role="meth"}
