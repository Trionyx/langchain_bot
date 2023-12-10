# deleteWebhook

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.delete_webhook
:::

## Usage

### As bot method

``` 
result: bool = await bot.delete_webhook(...)
```

### Method as object

Imports:

-   `from aiogram.methods.delete_webhook import DeleteWebhook`
-   alias: `from aiogram.methods import DeleteWebhook`

#### With specific bot

``` python
result: bool = await bot(DeleteWebhook(...))
```

#### As reply into Webhook in handler

``` python
return DeleteWebhook(...)
```
