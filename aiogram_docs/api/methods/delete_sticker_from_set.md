# deleteStickerFromSet

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.delete_sticker_from_set
:::

## Usage

### As bot method

``` 
result: bool = await bot.delete_sticker_from_set(...)
```

### Method as object

Imports:

-   `from aiogram.methods.delete_sticker_from_set import DeleteStickerFromSet`
-   alias: `from aiogram.methods import DeleteStickerFromSet`

#### With specific bot

``` python
result: bool = await bot(DeleteStickerFromSet(...))
```

#### As reply into Webhook in handler

``` python
return DeleteStickerFromSet(...)
```

### As shortcut from received object

-   `aiogram.types.sticker.Sticker.delete_from_set`{.interpreted-text
    role="meth"}
