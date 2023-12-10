# setChatPermissions

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_chat_permissions
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_chat_permissions(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_chat_permissions import SetChatPermissions`
-   alias: `from aiogram.methods import SetChatPermissions`

#### With specific bot

``` python
result: bool = await bot(SetChatPermissions(...))
```

#### As reply into Webhook in handler

``` python
return SetChatPermissions(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.set_permissions`{.interpreted-text
    role="meth"}
