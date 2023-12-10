# answerPreCheckoutQuery

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.answer_pre_checkout_query
:::

## Usage

### As bot method

``` 
result: bool = await bot.answer_pre_checkout_query(...)
```

### Method as object

Imports:

-   `from aiogram.methods.answer_pre_checkout_query import AnswerPreCheckoutQuery`
-   alias: `from aiogram.methods import AnswerPreCheckoutQuery`

#### With specific bot

``` python
result: bool = await bot(AnswerPreCheckoutQuery(...))
```

#### As reply into Webhook in handler

``` python
return AnswerPreCheckoutQuery(...)
```

### As shortcut from received object

-   `aiogram.types.pre_checkout_query.PreCheckoutQuery.answer`{.interpreted-text
    role="meth"}
