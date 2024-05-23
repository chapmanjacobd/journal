It's because of overhead.

People who create tools for software developers have to allocate their time. If they spend 20% or 30% of their time writing a GUI that means they spent their time writing a GUI instead of improving something else.

Few people are good at designing good GUIs and writing [efficient code](https://en.wikipedia.org/wiki/Instruction_pipelining) (similar to the frontend/backend web development dichotomy) so I imagine that 30% number might even be higher like 50% of their time to figure out how to create and maintain GUI frameworks, dependencies, and creating a good user interface.

The other reason is that software is notorious for having edge cases which vary in harm and specific tools like `git` have already matured really well. It's difficult to replicate `git`-like workflow saving _with the same level of robustness_ if you don't have the resources to replicate it (time + situations * willing "test subjects"). Maybe you don't need distributed synchronization or conflict resolution between multiple versions _right now_ but many people do need it to work effectively on large data projects
