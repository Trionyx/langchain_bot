# getUserProfilePhotos

Returns: `UserProfilePhotos`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.get_user_profile_photos
:::

## Usage

### As bot method

``` 
result: UserProfilePhotos = await bot.get_user_profile_photos(...)
```

### Method as object

Imports:

-   `from aiogram.methods.get_user_profile_photos import GetUserProfilePhotos`
-   alias: `from aiogram.methods import GetUserProfilePhotos`

#### With specific bot

``` python
result: UserProfilePhotos = await bot(GetUserProfilePhotos(...))
```

### As shortcut from received object

-   `aiogram.types.user.User.get_profile_photos`{.interpreted-text
    role="meth"}
