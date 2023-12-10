# setStickerSetTitle

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_sticker_set_title
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_sticker_set_title(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_sticker_set_title import SetStickerSetTitle`
-   alias: `from aiogram.methods import SetStickerSetTitle`

#### With specific bot

``` python
result: bool = await bot(SetStickerSetTitle(...))
```

#### As reply into Webhook in handler

``` python
return SetStickerSetTitle(...)
```
