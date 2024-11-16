"""
The basic Python script used by PyInstaller to build a single file executable for the main CLI entrypoint.

The full CLI should still be used via `pip` installation, which defines more entrypoints related to DevOps.
"""

from como_recipes._command_line_interface import _como_recipes_command_line_interface_main_entrypoint

if __name__ == "__main__":
    _como_recipes_command_line_interface_main_entrypoint()

    test = "adfsdfsf"
    print(
        test
        + "abcaedfsdfdsfsfsfdsfsfdsfsfdsfsdf"
        + "143563546435635634563456436346534636534653423"
        + "354535533453453534b53454535345"
    )
