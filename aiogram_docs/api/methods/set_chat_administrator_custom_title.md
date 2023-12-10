# setChatAdministratorCustomTitle

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_chat_administrator_custom_title
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_chat_administrator_custom_title(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_chat_administrator_custom_title import SetChatAdministratorCustomTitle`
-   alias: `from aiogram.methods import SetChatAdministratorCustomTitle`

#### With specific bot

``` python
result: bool = await bot(SetChatAdministratorCustomTitle(...))
```

#### As reply into Webhook in handler

``` python
return SetChatAdministratorCustomTitle(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.set_administrator_custom_title`{.interpreted-text
    role="meth"}
