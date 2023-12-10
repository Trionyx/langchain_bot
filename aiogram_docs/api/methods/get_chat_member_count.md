# getChatMemberCount

Returns: `int`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.get_chat_member_count
:::

## Usage

### As bot method

``` 
result: int = await bot.get_chat_member_count(...)
```

### Method as object

Imports:

-   `from aiogram.methods.get_chat_member_count import GetChatMemberCount`
-   alias: `from aiogram.methods import GetChatMemberCount`

#### With specific bot

``` python
result: int = await bot(GetChatMemberCount(...))
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.get_member_count`{.interpreted-text
    role="meth"}
