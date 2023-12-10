# createInvoiceLink

Returns: `str`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.create_invoice_link
:::

## Usage

### As bot method

``` 
result: str = await bot.create_invoice_link(...)
```

### Method as object

Imports:

-   `from aiogram.methods.create_invoice_link import CreateInvoiceLink`
-   alias: `from aiogram.methods import CreateInvoiceLink`

#### With specific bot

``` python
result: str = await bot(CreateInvoiceLink(...))
```

#### As reply into Webhook in handler

``` python
return CreateInvoiceLink(...)
```
