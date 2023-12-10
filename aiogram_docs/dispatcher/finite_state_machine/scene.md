# Scenes Wizard {#Scenes}

::: versionadded
3.2
:::

::: warning
::: title
Warning
:::

This feature is experimental and may be changed in future versions.
:::

**aiogram\'s** basics API is easy to use and powerful, allowing the
implementation of simple interactions such as triggering a command or
message for a response. However, certain tasks require a dialogue
between the user and the bot. This is where Scenes come into play.

## Understanding Scenes

A Scene in **aiogram** is like an abstract, isolated namespace or room
that a user can be ushered into via the code. When a user is within a
Scene, most other global commands or message handlers are bypassed,
unless they are specifically designed to function outside of the Scenes.
This helps in creating an experience of focused interactions. Scenes
provide a structure for more complex interactions, effectively isolating
and managing contexts for different stages of the conversation. They
allow you to control and manage the flow of the conversation in a more
organized manner.

### Scene Lifecycle

Each Scene can be \"entered\", \"left\" of \"exited\", allowing for
clear transitions between different stages of the conversation. For
instance, in a multi-step form filling interaction, each step could be a
Scene -the bot guides the user from one Scene to the next as they
provide the required information.

### Scene Listeners

Scenes have their own hooks which are command or message listeners that
only act while the user is within the Scene. These hooks react to user
actions while the user is \'inside\' the Scene, providing the responses
or actions appropriate for that context. When the user is ushered from
one Scene to another, the actions and responses change accordingly as
the user is now interacting with the set of listeners inside the new
Scene. These \'Scene-specific\' hooks or listeners, detached from the
global listening context, allow for more streamlined and organized
bot-user interactions.

### Scene Interactions

Each Scene is like a self-contained world, with interactions defined
within the scope of that Scene. As such, only the handlers defined
within the specific Scene will react to user\'s input during the
lifecycle of that Scene.

### Scene Benefits

Scenes can help manage more complex interaction workflows and enable
more interactive and dynamic dialogs between the user and the bot. This
offers great flexibility in handling multi-step interactions or
conversations with the users.

## How to use Scenes

For example we have a quiz bot, which asks the user a series of
questions and then displays the results.

Lets start with the data models, in this example simple data models are
used to represent the questions and answers, in real life you would
probably use a database to store the data.

::: {.literalinclude language="python" lines="25-101" caption="Questions list"}
../../../examples/quiz_scene.py
:::

Then, we need to create a Scene class that will represent the quiz game
scene:

::: note
::: title
Note
:::

Keyword argument passed into class definition describes the scene name -
is the same as state of the scene.
:::

::: {.literalinclude language="python" pyobject="QuizScene" emphasize-lines="1" lines="-7" caption="Quiz Scene"}
../../../examples/quiz_scene.py
:::

Also we need to define a handler that helps to start the quiz game:

::: {.literalinclude language="python" caption="Start command handler" lines="260-262"}
../../../examples/quiz_scene.py
:::

Once the scene is defined, we need to register it in the SceneRegistry:

::: {.literalinclude language="python" pyobject="create_dispatcher" caption="Registering the scene"}
../../../examples/quiz_scene.py
:::

So, now we can implement the quiz game logic, each question is sent to
the user one by one, and the user\'s answer is checked at the end of all
questions.

Now we need to write an entry point for the question handler:

::: {.literalinclude language="python" caption="Question handler entry point" pyobject="QuizScene.on_enter"}
../../../examples/quiz_scene.py
:::

Once scene is entered, we should expect the user\'s answer, so we need
to write a handler for it, this handler should expect the text message,
save the answer and retake the question handler for the next question:

::: {.literalinclude language="python" caption="Answer handler" pyobject="QuizScene.answer"}
../../../examples/quiz_scene.py
:::

When user answer with unknown message, we should expect the text message
again:

::: {.literalinclude language="python" caption="Unknown message handler" pyobject="QuizScene.unknown_message"}
../../../examples/quiz_scene.py
:::

When all questions are answered, we should show the results to the user,
as you can see in the code below, we use [await
self.wizard.exit()]{.title-ref} to exit from the scene when questions
list is over in the [QuizScene.on_enter]{.title-ref} handler.

Thats means that we need to write an exit handler to show the results to
the user:

::: {.literalinclude language="python" caption="Show results handler" pyobject="QuizScene.on_exit"}
../../../examples/quiz_scene.py
:::

Also we can implement a actions to exit from the quiz game or go back to
the previous question:

::: {.literalinclude language="python" caption="Exit handler" pyobject="QuizScene.exit"}
../../../examples/quiz_scene.py
:::

::: {.literalinclude language="python" caption="Back handler" pyobject="QuizScene.back"}
../../../examples/quiz_scene.py
:::

Now we can run the bot and test the quiz game:

::: {.literalinclude language="python" caption="Run the bot" lines="291-"}
../../../examples/quiz_scene.py
:::

Complete them all

::: {.literalinclude language="python" caption="Quiz Example"}
../../../examples/quiz_scene.py
:::

## Components

-   `aiogram.fsm.scene.Scene`{.interpreted-text role="class"} -
    represents a scene, contains handlers
-   `aiogram.fsm.scene.SceneRegistry`{.interpreted-text role="class"} -
    container for all scenes in the bot, used to register scenes and
    resolve them by name
-   `aiogram.fsm.scene.ScenesManager`{.interpreted-text role="class"} -
    manages scenes for each user, used to enter, leave and resolve
    current scene for user
-   `aiogram.fsm.scene.SceneConfig`{.interpreted-text role="class"} -
    scene configuration, used to configure scene
-   `aiogram.fsm.scene.SceneWizard`{.interpreted-text role="class"} -
    scene wizard, used to interact with user in scene from active scene
    handler
-   Markers - marker for scene handlers, used to mark scene handlers

::: {.autoclass members=""}
aiogram.fsm.scene.Scene
:::

::: {.autoclass members=""}
aiogram.fsm.scene.SceneRegistry
:::

::: {.autoclass members=""}
aiogram.fsm.scene.ScenesManager
:::

::: {.autoclass members=""}
aiogram.fsm.scene.SceneConfig
:::

::: {.autoclass members=""}
aiogram.fsm.scene.SceneWizard
:::

### Markers

Markers are similar to the Router event registering mechanism, but they
are used to mark scene handlers in the Scene class.

It can be imported from `from aiogram.fsm.scene import on` and should be
used as decorator.

Allowed event types:

-   message
-   edited_message
-   channel_post
-   edited_channel_post
-   inline_query
-   chosen_inline_result
-   callback_query
-   shipping_query
-   pre_checkout_query
-   poll
-   poll_answer
-   my_chat_member
-   chat_member
-   chat_join_request

Each event type can be filtered in the same way as in the Router.

Also each event type can be marked as scene entry point, exit point or
leave point.

If you want to mark the scene can be entered from message or inline
query, you should use `on.message` or `on.inline_query` marker:

``` python
class MyScene(Scene, name="my_scene"):
    @on.message.enter()
    async def on_enter(self, message: types.Message):
        pass

    @on.callback_query.enter()
    async def on_enter(self, callback_query: types.CallbackQuery):
        pass
```

Scene has only tree points for transitions:

-   enter point - when user enters to the scene
-   leave point - when user leaves the scene and the enter another scene
-   exit point - when user exits from the scene
