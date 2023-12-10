# answerWebAppQuery

Returns: `SentWebAppMessage`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.answer_web_app_query
:::

## Usage

### As bot method

``` 
result: SentWebAppMessage = await bot.answer_web_app_query(...)
```

### Method as object

Imports:

-   `from aiogram.methods.answer_web_app_query import AnswerWebAppQuery`
-   alias: `from aiogram.methods import AnswerWebAppQuery`

#### With specific bot

``` python
result: SentWebAppMessage = await bot(AnswerWebAppQuery(...))
```

#### As reply into Webhook in handler

``` python
return AnswerWebAppQuery(...)
```
