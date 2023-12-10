# setMyDescription

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_my_description
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_my_description(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_my_description import SetMyDescription`
-   alias: `from aiogram.methods import SetMyDescription`

#### With specific bot

``` python
result: bool = await bot(SetMyDescription(...))
```

#### As reply into Webhook in handler

``` python
return SetMyDescription(...)
```
