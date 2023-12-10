# addStickerToSet

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.add_sticker_to_set
:::

## Usage

### As bot method

``` 
result: bool = await bot.add_sticker_to_set(...)
```

### Method as object

Imports:

-   `from aiogram.methods.add_sticker_to_set import AddStickerToSet`
-   alias: `from aiogram.methods import AddStickerToSet`

#### With specific bot

``` python
result: bool = await bot(AddStickerToSet(...))
```

#### As reply into Webhook in handler

``` python
return AddStickerToSet(...)
```
