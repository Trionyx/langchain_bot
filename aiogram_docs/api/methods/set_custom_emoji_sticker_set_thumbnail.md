# setCustomEmojiStickerSetThumbnail

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_custom_emoji_sticker_set_thumbnail
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_custom_emoji_sticker_set_thumbnail(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_custom_emoji_sticker_set_thumbnail import SetCustomEmojiStickerSetThumbnail`
-   alias:
    `from aiogram.methods import SetCustomEmojiStickerSetThumbnail`

#### With specific bot

``` python
result: bool = await bot(SetCustomEmojiStickerSetThumbnail(...))
```

#### As reply into Webhook in handler

``` python
return SetCustomEmojiStickerSetThumbnail(...)
```
