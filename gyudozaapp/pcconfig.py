import pynecone as pc


config = pc.Config(
    app_name="gyudozaapp",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)