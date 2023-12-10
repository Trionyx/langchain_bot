# setStickerEmojiList

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_sticker_emoji_list
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_sticker_emoji_list(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_sticker_emoji_list import SetStickerEmojiList`
-   alias: `from aiogram.methods import SetStickerEmojiList`

#### With specific bot

``` python
result: bool = await bot(SetStickerEmojiList(...))
```

#### As reply into Webhook in handler

``` python
return SetStickerEmojiList(...)
```
