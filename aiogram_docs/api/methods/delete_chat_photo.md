# deleteChatPhoto

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.delete_chat_photo
:::

## Usage

### As bot method

``` 
result: bool = await bot.delete_chat_photo(...)
```

### Method as object

Imports:

-   `from aiogram.methods.delete_chat_photo import DeleteChatPhoto`
-   alias: `from aiogram.methods import DeleteChatPhoto`

#### With specific bot

``` python
result: bool = await bot(DeleteChatPhoto(...))
```

#### As reply into Webhook in handler

``` python
return DeleteChatPhoto(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.delete_photo`{.interpreted-text
    role="meth"}
