# createNewStickerSet

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.create_new_sticker_set
:::

## Usage

### As bot method

``` 
result: bool = await bot.create_new_sticker_set(...)
```

### Method as object

Imports:

-   `from aiogram.methods.create_new_sticker_set import CreateNewStickerSet`
-   alias: `from aiogram.methods import CreateNewStickerSet`

#### With specific bot

``` python
result: bool = await bot(CreateNewStickerSet(...))
```

#### As reply into Webhook in handler

``` python
return CreateNewStickerSet(...)
```
