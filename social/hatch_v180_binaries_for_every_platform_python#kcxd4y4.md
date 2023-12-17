I'm not sure what the OP is exactly but you can use hatch from pdm, I think? I had to use it for some reason:

    [build-system]
    build-backend = "hatchling.build"
    requires = ["hatchling"]

    [tool.hatch.version]
    path = "xklb/__init__.py"

    [tool.hatch.build]
    exclude = [
      "tests/",
      "example_dbs/",
    ]

    [tool.hatch.build.force-include]
    "xklb/assets/" = "xklb/assets/"
