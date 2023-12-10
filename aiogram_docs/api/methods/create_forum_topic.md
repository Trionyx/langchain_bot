# createForumTopic

Returns: `ForumTopic`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.create_forum_topic
:::

## Usage

### As bot method

``` 
result: ForumTopic = await bot.create_forum_topic(...)
```

### Method as object

Imports:

-   `from aiogram.methods.create_forum_topic import CreateForumTopic`
-   alias: `from aiogram.methods import CreateForumTopic`

#### With specific bot

``` python
result: ForumTopic = await bot(CreateForumTopic(...))
```

#### As reply into Webhook in handler

``` python
return CreateForumTopic(...)
```
