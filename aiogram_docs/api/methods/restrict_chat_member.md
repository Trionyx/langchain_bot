# restrictChatMember

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.restrict_chat_member
:::

## Usage

### As bot method

``` 
result: bool = await bot.restrict_chat_member(...)
```

### Method as object

Imports:

-   `from aiogram.methods.restrict_chat_member import RestrictChatMember`
-   alias: `from aiogram.methods import RestrictChatMember`

#### With specific bot

``` python
result: bool = await bot(RestrictChatMember(...))
```

#### As reply into Webhook in handler

``` python
return RestrictChatMember(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.restrict`{.interpreted-text role="meth"}
