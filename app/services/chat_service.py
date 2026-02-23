import logging

logger = logging.getLogger(__name__)

class ChatService:
    def echo(self, message: str) ->  str:
        msg = message.strip()
        if not msg:
            raise ValueError("message is empty")

        logger.info("message: %s", msg)
        return f"echo: {msg}"