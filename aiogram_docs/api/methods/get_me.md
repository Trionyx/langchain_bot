# getMe

Returns: `User`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.get_me
:::

## Usage

### As bot method

``` 
result: User = await bot.get_me(...)
```

### Method as object

Imports:

-   `from aiogram.methods.get_me import GetMe`
-   alias: `from aiogram.methods import GetMe`

#### With specific bot

``` python
result: User = await bot(GetMe(...))
```
