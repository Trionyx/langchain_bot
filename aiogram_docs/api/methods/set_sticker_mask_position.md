# setStickerMaskPosition

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_sticker_mask_position
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_sticker_mask_position(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_sticker_mask_position import SetStickerMaskPosition`
-   alias: `from aiogram.methods import SetStickerMaskPosition`

#### With specific bot

``` python
result: bool = await bot(SetStickerMaskPosition(...))
```

#### As reply into Webhook in handler

``` python
return SetStickerMaskPosition(...)
```
