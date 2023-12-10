# setChatDescription

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_chat_description
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_chat_description(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_chat_description import SetChatDescription`
-   alias: `from aiogram.methods import SetChatDescription`

#### With specific bot

``` python
result: bool = await bot(SetChatDescription(...))
```

#### As reply into Webhook in handler

``` python
return SetChatDescription(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.set_description`{.interpreted-text
    role="meth"}
