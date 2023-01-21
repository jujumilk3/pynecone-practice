"""Welcome to Pynecone! This file outlines the steps to create a basic app."""


import pynecone as pc

from gyudozaapp.pages import door, index


class State(pc.State):
    """The app state."""

    pass


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index.index)
app.add_page(door.door)

app.compile()
