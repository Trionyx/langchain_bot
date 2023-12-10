# getWebhookInfo

Returns: `WebhookInfo`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.get_webhook_info
:::

## Usage

### As bot method

``` 
result: WebhookInfo = await bot.get_webhook_info(...)
```

### Method as object

Imports:

-   `from aiogram.methods.get_webhook_info import GetWebhookInfo`
-   alias: `from aiogram.methods import GetWebhookInfo`

#### With specific bot

``` python
result: WebhookInfo = await bot(GetWebhookInfo(...))
```
