# deleteStickerSet

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.delete_sticker_set
:::

## Usage

### As bot method

``` 
result: bool = await bot.delete_sticker_set(...)
```

### Method as object

Imports:

-   `from aiogram.methods.delete_sticker_set import DeleteStickerSet`
-   alias: `from aiogram.methods import DeleteStickerSet`

#### With specific bot

``` python
result: bool = await bot(DeleteStickerSet(...))
```

#### As reply into Webhook in handler

``` python
return DeleteStickerSet(...)
```
