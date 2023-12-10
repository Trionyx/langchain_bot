# setChatPhoto

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_chat_photo
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_chat_photo(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_chat_photo import SetChatPhoto`
-   alias: `from aiogram.methods import SetChatPhoto`

#### With specific bot

``` python
result: bool = await bot(SetChatPhoto(...))
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.set_photo`{.interpreted-text role="meth"}
