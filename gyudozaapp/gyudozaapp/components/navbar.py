import pynecone as pc


def navbar():
    return pc.box(
        pc.hstack(
            pc.hstack(
                pc.image(src="/favicon.ico", width="50px"),
                pc.heading("gyudozaapp", font_size="1em"),
                pc.flex(
                    pc.badge("Hello world", color_scheme="blue"),
                ),
            ),
            pc.menu(
                pc.menu_button("Menu", bg="black", color="white", border_radius="md", px=4, py=1, font_size="0.5em"),
                pc.menu_list(
                    pc.link(pc.menu_item("Home (index.py)"), href="/", font_size="0.5em"),
                    pc.link(pc.menu_item("Door (door.py)"), href="/door", font_size="0.5em"),
                    pc.menu_divider(),
                    pc.link(
                        pc.menu_item(pc.hstack(pc.text("20Dataset"), pc.icon(tag="DownloadIcon"), font_size="0.5em")),
                        href="https://media.geeksforgeeks.org/wp-content/uploads/nba.csv",
                    ),
                ),
            ),
            justify="space-between",
            border_bottom="0.2em solid #F0F0F0",
            padding_x="2em",
            padding_y="1em",
            bg="rgba(255,255,255, 0.97)",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
    )
