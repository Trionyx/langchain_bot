# unbanChatMember

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.unban_chat_member
:::

## Usage

### As bot method

``` 
result: bool = await bot.unban_chat_member(...)
```

### Method as object

Imports:

-   `from aiogram.methods.unban_chat_member import UnbanChatMember`
-   alias: `from aiogram.methods import UnbanChatMember`

#### With specific bot

``` python
result: bool = await bot(UnbanChatMember(...))
```

#### As reply into Webhook in handler

``` python
return UnbanChatMember(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.unban`{.interpreted-text role="meth"}
