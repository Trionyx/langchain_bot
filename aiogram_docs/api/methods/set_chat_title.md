# setChatTitle

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_chat_title
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_chat_title(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_chat_title import SetChatTitle`
-   alias: `from aiogram.methods import SetChatTitle`

#### With specific bot

``` python
result: bool = await bot(SetChatTitle(...))
```

#### As reply into Webhook in handler

``` python
return SetChatTitle(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.set_title`{.interpreted-text role="meth"}
