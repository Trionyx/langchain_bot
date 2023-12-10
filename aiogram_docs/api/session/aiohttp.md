# aiohttp

AiohttpSession represents a wrapper-class around
[ClientSession]{.title-ref} from
[aiohttp](https://pypi.org/project/aiohttp/)

Currently [AiohttpSession]{.title-ref} is a default session used in
[aiogram.Bot]{.title-ref}

::: autoclass
aiogram.client.session.aiohttp.AiohttpSession
:::

## Usage example

``` 
from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession

session = AiohttpSession()
bot = Bot('42:token', session=session)
```

## Proxy requests in AiohttpSession

In order to use AiohttpSession with proxy connector you have to install
[aiohttp-socks](https://pypi.org/project/aiohttp-socks)

Binding session to bot:

``` 
from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession

session = AiohttpSession(proxy="protocol://host:port/")
bot = Bot(token="bot token", session=session)
```

::: note
::: title
Note
:::

Only following protocols are supported: http(tunneling), socks4(a),
socks5 as aiohttp_socks
[documentation](https://github.com/romis2012/aiohttp-socks/blob/master/README.md)
claims.
:::

### Authorization

Proxy authorization credentials can be specified in proxy URL or come as
an instance of `aiohttp.BasicAuth`{.interpreted-text role="obj"}
containing login and password.

Consider examples:

``` 
from aiohttp import BasicAuth
from aiogram.client.session.aiohttp import AiohttpSession

auth = BasicAuth(login="user", password="password")
session = AiohttpSession(proxy=("protocol://host:port", auth))
```

or simply include your basic auth credential in URL

``` 
session = AiohttpSession(proxy="protocol://user:password@host:port")
```

::: note
::: title
Note
:::

Aiogram prefers [BasicAuth]{.title-ref} over username and password in
URL, so if proxy URL contains login and password and
[BasicAuth]{.title-ref} object is passed at the same time aiogram will
use login and password from [BasicAuth]{.title-ref} instance.
:::

### Proxy chains

Since [aiohttp-socks](https://pypi.org/project/aiohttp-socks/) supports
proxy chains, you\'re able to use them in aiogram

Example of chain proxies:

``` 
from aiohttp import BasicAuth
from aiogram.client.session.aiohttp import AiohttpSession

auth = BasicAuth(login="user", password="password")
session = AiohttpSession(
    proxy={
        "protocol0://host0:port0",
        "protocol1://user:password@host1:port1",
        ("protocol2://host2:port2", auth),
    }  # can be any iterable if not set
)
```
