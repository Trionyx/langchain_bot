# answerShippingQuery

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.answer_shipping_query
:::

## Usage

### As bot method

``` 
result: bool = await bot.answer_shipping_query(...)
```

### Method as object

Imports:

-   `from aiogram.methods.answer_shipping_query import AnswerShippingQuery`
-   alias: `from aiogram.methods import AnswerShippingQuery`

#### With specific bot

``` python
result: bool = await bot(AnswerShippingQuery(...))
```

#### As reply into Webhook in handler

``` python
return AnswerShippingQuery(...)
```

### As shortcut from received object

-   `aiogram.types.shipping_query.ShippingQuery.answer`{.interpreted-text
    role="meth"}
