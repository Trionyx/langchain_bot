# deleteChatStickerSet

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.delete_chat_sticker_set
:::

## Usage

### As bot method

``` 
result: bool = await bot.delete_chat_sticker_set(...)
```

### Method as object

Imports:

-   `from aiogram.methods.delete_chat_sticker_set import DeleteChatStickerSet`
-   alias: `from aiogram.methods import DeleteChatStickerSet`

#### With specific bot

``` python
result: bool = await bot(DeleteChatStickerSet(...))
```

#### As reply into Webhook in handler

``` python
return DeleteChatStickerSet(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.delete_sticker_set`{.interpreted-text
    role="meth"}
