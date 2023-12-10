# Finite State Machine {#Finite State Machine}

> A finite-state machine (FSM) or finite-state automaton (FSA, plural:
> automata), finite automaton, or simply a state machine, is a
> mathematical model of computation.
>
> It is an abstract machine that can be in exactly one of a finite
> number of states at any given time. The FSM can change from one state
> to another in response to some inputs; the change from one state to
> another is called a transition.
>
> An FSM is defined by a list of its states, its initial state, and the
> inputs that trigger each transition.
>
> ```{=html}
> <hr>
> ```
> Source: [WikiPedia](wiki)

## Usage example

Not all functionality of the bot can be implemented as single handler,
for example you will need to collect some data from user in separated
steps you will need to use FSM.

![FSM Example](../../_static/fsm_example.png)

Let\'s see how to do that step-by-step

### Step by step

Before handle any states you will need to specify what kind of states
you want to handle

::: {.literalinclude pyobject="Form"}
../../../examples/finite_state_machine.py
:::

And then write handler for each state separately from the start of
dialog

Here is dialog can be started only via command `/start`, so lets handle
it and make transition user to state `Form.name`

::: {.literalinclude pyobject="command_start"}
../../../examples/finite_state_machine.py
:::

After that you will need to save some data to the storage and make
transition to next step.

::: {.literalinclude pyobject="process_name"}
../../../examples/finite_state_machine.py
:::

At the next steps user can make different answers, it can be
[yes]{.title-ref}, [no]{.title-ref} or any other

Handle `yes` and soon we need to handle `Form.language` state

::: {.literalinclude pyobject="process_like_write_bots"}
../../../examples/finite_state_machine.py
:::

Handle `no`

::: {.literalinclude pyobject="process_dont_like_write_bots"}
../../../examples/finite_state_machine.py
:::

And handle any other answers

::: {.literalinclude pyobject="process_unknown_write_bots"}
../../../examples/finite_state_machine.py
:::

All possible cases of [like_bots]{.title-ref} step was covered, let\'s
implement finally step

::: {.literalinclude pyobject="process_language"}
../../../examples/finite_state_machine.py
:::

::: {.literalinclude pyobject="show_summary"}
../../../examples/finite_state_machine.py
:::

And now you have covered all steps from the image, but you can make
possibility to cancel conversation, lets do that via command or text

::: {.literalinclude pyobject="cancel_handler"}
../../../examples/finite_state_machine.py
:::

### Complete example

::: {.literalinclude language="python" linenos=""}
../../../examples/finite_state_machine.py
:::

## Read more

::: toctree
storages scene
:::
