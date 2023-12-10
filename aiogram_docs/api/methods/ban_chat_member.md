# banChatMember

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.ban_chat_member
:::

## Usage

### As bot method

``` 
result: bool = await bot.ban_chat_member(...)
```

### Method as object

Imports:

-   `from aiogram.methods.ban_chat_member import BanChatMember`
-   alias: `from aiogram.methods import BanChatMember`

#### With specific bot

``` python
result: bool = await bot(BanChatMember(...))
```

#### As reply into Webhook in handler

``` python
return BanChatMember(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.ban`{.interpreted-text role="meth"}
