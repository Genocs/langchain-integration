
from typing import Dict, Union, Any, List
from langchain.callbacks.base import BaseCallbackHandler, AgentFinish
from rabbitmq_client import RabbitMQSender


class RabbitMQCallbackHandler(BaseCallbackHandler):
    """The callback handler that will be used to handle callbacks from langchain.

        This class is used to send the response to RabbitMQ."""

    def __init__(self, **kwargs) -> None:
        """Initialize the callback handler."""

        super().__init__(**kwargs)
        self._rabbitmq_sender = RabbitMQSender(namespace='Genocs.Fiscanner.Contracts.LLMs', message_name='LLMResponse')

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"My custom handler, token: {token}")

    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> Any:
        """Run when LLM finish running."""

        """Run on agent end."""
        self._rabbitmq_sender.send_message(finish.log)


# class MyCallbackHandler(BaseCallbackHandler):
# """Base callback handler that can be used to handle callbacks from langchain."""
##
# def on_llm_start(
# self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
# ) -> Any:
# """Run when LLM starts running."""
##
# def on_chat_model_start(
# self, serialized: Dict[str, Any], messages: List[List[BaseMessage]], **kwargs: Any
# ) -> Any:
# """Run when Chat Model starts running."""
##
# def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
# """Run on new LLM token. Only available when streaming is enabled."""
##
# def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
# """Run when LLM ends running."""
##
# def on_llm_error(
# self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
# ) -> Any:
# """Run when LLM errors."""
##
# def on_chain_start(
# self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
# ) -> Any:
# """Run when chain starts running."""
##
# def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> Any:
# """Run when chain ends running."""
##
# def on_chain_error(
# self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
# ) -> Any:
# """Run when chain errors."""
##
# def on_tool_start(
# self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
# ) -> Any:
# """Run when tool starts running."""
##
# def on_tool_end(self, output: str, **kwargs: Any) -> Any:
# """Run when tool ends running."""
##
# def on_tool_error(
# self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
# ) -> Any:
# """Run when tool errors."""
##
# def on_text(self, text: str, **kwargs: Any) -> Any:
# """Run on arbitrary text."""
##
# def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
# """Run on agent action."""
##
# def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> Any:
# """Run on agent end."""