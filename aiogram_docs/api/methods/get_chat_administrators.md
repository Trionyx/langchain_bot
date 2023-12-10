# getChatAdministrators

Returns:
`List[Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned]]`{.interpreted-text
role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.get_chat_administrators
:::

## Usage

### As bot method

``` 
result: List[Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned]] = await bot.get_chat_administrators(...)
```

### Method as object

Imports:

-   `from aiogram.methods.get_chat_administrators import GetChatAdministrators`
-   alias: `from aiogram.methods import GetChatAdministrators`

#### With specific bot

``` python
result: List[Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned]] = await bot(GetChatAdministrators(...))
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.get_administrators`{.interpreted-text
    role="meth"}
