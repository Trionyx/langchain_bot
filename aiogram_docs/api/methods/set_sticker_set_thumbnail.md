# setStickerSetThumbnail

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_sticker_set_thumbnail
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_sticker_set_thumbnail(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_sticker_set_thumbnail import SetStickerSetThumbnail`
-   alias: `from aiogram.methods import SetStickerSetThumbnail`

#### With specific bot

``` python
result: bool = await bot(SetStickerSetThumbnail(...))
```

#### As reply into Webhook in handler

``` python
return SetStickerSetThumbnail(...)
```
