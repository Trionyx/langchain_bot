# stopPoll

Returns: `Poll`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.stop_poll
:::

## Usage

### As bot method

``` 
result: Poll = await bot.stop_poll(...)
```

### Method as object

Imports:

-   `from aiogram.methods.stop_poll import StopPoll`
-   alias: `from aiogram.methods import StopPoll`

#### With specific bot

``` python
result: Poll = await bot(StopPoll(...))
```

#### As reply into Webhook in handler

``` python
return StopPoll(...)
```
