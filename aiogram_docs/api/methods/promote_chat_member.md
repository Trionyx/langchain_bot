# promoteChatMember

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.promote_chat_member
:::

## Usage

### As bot method

``` 
result: bool = await bot.promote_chat_member(...)
```

### Method as object

Imports:

-   `from aiogram.methods.promote_chat_member import PromoteChatMember`
-   alias: `from aiogram.methods import PromoteChatMember`

#### With specific bot

``` python
result: bool = await bot(PromoteChatMember(...))
```

#### As reply into Webhook in handler

``` python
return PromoteChatMember(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.promote`{.interpreted-text role="meth"}
