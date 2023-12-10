# setWebhook

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_webhook
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_webhook(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_webhook import SetWebhook`
-   alias: `from aiogram.methods import SetWebhook`

#### With specific bot

``` python
result: bool = await bot(SetWebhook(...))
```

#### As reply into Webhook in handler

``` python
return SetWebhook(...)
```
