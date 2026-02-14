from negmas.gb import BoulwareTBNegotiator
from negmas_llm.meta import LLMMetaNegotiator

# =============================================================================
# Default Prompt (copied from negmas_llm, customize as needed)
# =============================================================================

# System prompt for text generation in LLMMetaNegotiator
SYSTEM_PROMPT = """
You are assisting a negotiator by generating persuasive text to
accompany offers.

Your role is to:
1. Generate natural, persuasive messages that explain or justify the offer
2. Consider any messages received from the other party
3. Build rapport while advancing the negotiation
4. Keep messages concise but impactful

You will receive:
- The offer being made (or acceptance/rejection decision)
- Any text received from the other party in their last offer
- Context about the negotiation state

Respond with ONLY a JSON object:
{
    "text": "Your message to accompany the offer"
}

Keep messages brief (1-3 sentences) and professional.
"""


class BolwareBasedLLMNegotiator(LLMMetaNegotiator):
    """A simple LLM-based negotiator that adapts an existing negotiator to use LLM."""

    def __init__(
        self,
        base_negotiator: BoulwareTBNegotiator | None = None,
        provider: str = "ollama",
        model: str = "llama3.1:8b",
        **kwargs,
    ) -> None:
        """Initialize the BolwareBasedLLMNegotiator.

        Args:
            base_negotiator: The base negotiator to adapt. If None, creates a BoulwareTBNegotiator.
            provider: The LLM provider to use (default: "ollama").
            model: The LLM model to use (default: "llama3.1:8b").
            **kwargs: Additional arguments passed to LLMMetaNegotiator.
                Also supports prompt customization via system_prompt parameter.
        """
        if base_negotiator is None:
            base_negotiator = BoulwareTBNegotiator()
        super().__init__(
            base_negotiator=base_negotiator,
            provider=provider,
            model=model,
            system_prompt=SYSTEM_PROMPT,
            **kwargs,
        )
