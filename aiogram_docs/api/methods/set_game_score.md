# setGameScore

Returns: `Union[Message, bool]`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_game_score
:::

## Usage

### As bot method

``` 
result: Union[Message, bool] = await bot.set_game_score(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_game_score import SetGameScore`
-   alias: `from aiogram.methods import SetGameScore`

#### With specific bot

``` python
result: Union[Message, bool] = await bot(SetGameScore(...))
```

#### As reply into Webhook in handler

``` python
return SetGameScore(...)
```
