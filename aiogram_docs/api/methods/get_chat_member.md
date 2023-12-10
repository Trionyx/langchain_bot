# getChatMember

Returns:
`Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned]`{.interpreted-text
role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.get_chat_member
:::

## Usage

### As bot method

``` 
result: Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned] = await bot.get_chat_member(...)
```

### Method as object

Imports:

-   `from aiogram.methods.get_chat_member import GetChatMember`
-   alias: `from aiogram.methods import GetChatMember`

#### With specific bot

``` python
result: Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned] = await bot(GetChatMember(...))
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.get_member`{.interpreted-text role="meth"}
