# Command

## Usage

1.  Filter single variant of commands: `Command("start")`
2.  Handle command by regexp pattern:
    `Command(re.compile(r"item_(\d+)"))`
3.  Match command by multiple variants:
    `Command("item", re.compile(r"item_(\d+)"))`
4.  Handle commands in public chats intended for other bots:
    `Command("command", ignore_mention=True)`
5.  Use `aiogram.types.bot_command.BotCommand`{.interpreted-text
    role="class"} object as command reference
    `Command(BotCommand(command="command", description="My awesome command")`

::: warning
::: title
Warning
:::

Command cannot include spaces or any whitespace
:::

::: {.autoclass members="__init__" member-order="bysource" undoc-members="False"}
aiogram.filters.command.Command
:::

When filter is passed the
`aiogram.filters.command.CommandObject`{.interpreted-text role="class"}
will be passed to the handler argument `command`

::: {.autoclass members="" member-order="bysource" undoc-members="False"}
aiogram.filters.command.CommandObject
:::

## Allowed handlers

Allowed update types for this filter:

-   [message]{.title-ref}
-   [edited_message]{.title-ref}
