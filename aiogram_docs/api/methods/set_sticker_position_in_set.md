# setStickerPositionInSet

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_sticker_position_in_set
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_sticker_position_in_set(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_sticker_position_in_set import SetStickerPositionInSet`
-   alias: `from aiogram.methods import SetStickerPositionInSet`

#### With specific bot

``` python
result: bool = await bot(SetStickerPositionInSet(...))
```

#### As reply into Webhook in handler

``` python
return SetStickerPositionInSet(...)
```

### As shortcut from received object

-   `aiogram.types.sticker.Sticker.set_position_in_set`{.interpreted-text
    role="meth"}
