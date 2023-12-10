# Storages

## Storages out of the box

### MemoryStorage

::: {.autoclass members="__init__" member-order="bysource"}
aiogram.fsm.storage.memory.MemoryStorage
:::

### RedisStorage

::: {.autoclass members="__init__, from_url" member-order="bysource"}
aiogram.fsm.storage.redis.RedisStorage
:::

Keys inside storage can be customized via key builders:

::: {.autoclass members="" member-order="bysource"}
aiogram.fsm.storage.redis.KeyBuilder
:::

::: {.autoclass members="" member-order="bysource"}
aiogram.fsm.storage.redis.DefaultKeyBuilder
:::

## Writing own storages

::: {.autoclass members="" member-order="bysource"}
aiogram.fsm.storage.base.BaseStorage
:::
