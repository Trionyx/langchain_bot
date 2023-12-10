# setMyShortDescription

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_my_short_description
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_my_short_description(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_my_short_description import SetMyShortDescription`
-   alias: `from aiogram.methods import SetMyShortDescription`

#### With specific bot

``` python
result: bool = await bot(SetMyShortDescription(...))
```

#### As reply into Webhook in handler

``` python
return SetMyShortDescription(...)
```
