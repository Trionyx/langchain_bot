# setChatStickerSet

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_chat_sticker_set
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_chat_sticker_set(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_chat_sticker_set import SetChatStickerSet`
-   alias: `from aiogram.methods import SetChatStickerSet`

#### With specific bot

``` python
result: bool = await bot(SetChatStickerSet(...))
```

#### As reply into Webhook in handler

``` python
return SetChatStickerSet(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.set_sticker_set`{.interpreted-text
    role="meth"}
