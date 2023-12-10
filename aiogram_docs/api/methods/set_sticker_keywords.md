# setStickerKeywords

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_sticker_keywords
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_sticker_keywords(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_sticker_keywords import SetStickerKeywords`
-   alias: `from aiogram.methods import SetStickerKeywords`

#### With specific bot

``` python
result: bool = await bot(SetStickerKeywords(...))
```

#### As reply into Webhook in handler

``` python
return SetStickerKeywords(...)
```
