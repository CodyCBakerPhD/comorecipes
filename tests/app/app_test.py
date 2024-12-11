import logging

import como_recipes

if __name__ == "__main__":
    logging.basicConfig(format="(T%(msecs)d:%(name)s:%(lineno)d - %(levelname)s: %(message)s")

    # Control which modules have logging enabled (all are disabled by default)
    enable_module_logging = [
        "como_recipes.app._como_app",
        # "como_recipes.app._session_manager_frame",
    ]
    for module_name in enable_module_logging:
        logger_to_enable = logging.getLogger(name=module_name)
        logger_to_enable.disabled = False

    # Control global logging level
    logger = logging.getLogger()
    # level = logging.INFO
    level = logging.DEBUG
    logger.setLevel(level=level)

    # Launch app
    app = como_recipes.app.CoMoApp()
    logger.info("Starting CoMo app")

    app.mainloop()
    logger.info("CoMo app closed")

    logging.shutdown()
