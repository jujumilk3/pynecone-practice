import pynecone as pc
from gyudozaapp.components.navbar import navbar

def door():
    return pc.center(
        pc.vstack(
            navbar(),
            pc.heading("This is Door", font_size="2em"),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )
