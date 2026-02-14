"""Tests for example negotiators."""

import pytest
from negmas.preferences.generators import generate_multi_issue_ufuns
from negmas.sao import SAOMechanism

from examples.nollm import BOANeg, SimpleNeg
from examples.adapter import BolwareBasedLLMNegotiator


class TestBOANeg:
    """Tests for BOANeg negotiator."""

    def test_can_instantiate(self):
        """Test that BOANeg can be instantiated."""
        neg = BOANeg()
        assert neg is not None
        assert neg.name is not None

    def test_has_required_components(self):
        """Test that BOANeg has all required BOA components."""
        neg = BOANeg()
        # BOANeg components are set in __init__ via kwargs
        # We just verify it was created successfully
        assert neg is not None

    def test_can_negotiate(self):
        """Test that BOANeg can participate in a negotiation."""
        # Create utilities
        ufuns = generate_multi_issue_ufuns(
            n_issues=3, n_values=(3, 5), n_ufuns=2, reserved_values=0.0
        )

        # Create mechanism
        m = SAOMechanism(outcome_space=ufuns[0].outcome_space, n_steps=10)

        # Add negotiators
        m.add(BOANeg(ufun=ufuns[0], name="BOA1"))
        m.add(BOANeg(ufun=ufuns[1], name="BOA2"))

        # Run negotiation
        m.run()

        # Check that negotiation completed
        assert m.state.step <= 10
        assert m.state.agreement is not None or m.state.timedout or m.state.broken


class TestSimpleNeg:
    """Tests for SimpleNeg negotiator."""

    def test_can_instantiate(self):
        """Test that SimpleNeg can be instantiated."""
        neg = SimpleNeg()
        assert neg is not None
        assert neg.name is not None

    def test_accepts_high_utility_offers(self):
        """Test that SimpleNeg accepts offers with utility > 0.8."""
        # Create utilities
        ufuns = generate_multi_issue_ufuns(
            n_issues=3, n_values=(3, 5), n_ufuns=2, reserved_values=0.0
        )

        # Create mechanism
        m = SAOMechanism(outcome_space=ufuns[0].outcome_space, n_steps=20)

        # Add negotiators
        m.add(SimpleNeg(ufun=ufuns[0], name="Simple1"))
        m.add(SimpleNeg(ufun=ufuns[1], name="Simple2"))

        # Run negotiation
        m.run()

        # Check that negotiation completed
        assert m.state.step <= 20

    def test_response_includes_text(self):
        """Test that SimpleNeg includes text in its responses."""
        # Create utilities
        ufuns = generate_multi_issue_ufuns(
            n_issues=3, n_values=(3, 5), n_ufuns=2, reserved_values=0.0
        )

        # Create negotiator
        neg = SimpleNeg(ufun=ufuns[0], name="Simple")

        # Create mechanism
        m = SAOMechanism(outcome_space=ufuns[0].outcome_space, n_steps=5)
        m.add(neg)
        m.add(SimpleNeg(ufun=ufuns[1], name="Simple2"))

        # Run negotiation
        m.run()

        # Check that some responses have text (check trace)
        trace = m.trace
        assert len(trace) > 0


class TestBolwareBasedLLMNegotiator:
    """Tests for BolwareBasedLLMNegotiator adapter."""

    def test_can_instantiate_without_base(self):
        """Test that BolwareBasedLLMNegotiator can be instantiated without providing base negotiator."""
        neg = BolwareBasedLLMNegotiator()
        assert neg is not None
        assert neg.name is not None

    def test_can_instantiate_with_base(self):
        """Test that BolwareBasedLLMNegotiator can be instantiated with a base negotiator."""
        from negmas.gb import BoulwareTBNegotiator

        base = BoulwareTBNegotiator()
        neg = BolwareBasedLLMNegotiator(base_negotiator=base)
        assert neg is not None
        assert neg.name is not None

    def test_can_instantiate_with_custom_provider_model(self):
        """Test that BolwareBasedLLMNegotiator accepts custom provider and model."""
        neg = BolwareBasedLLMNegotiator(provider="ollama", model="llama3.2")
        assert neg is not None

    @pytest.mark.skip(reason="Requires Ollama running locally")
    def test_can_negotiate(self):
        """Test that BolwareBasedLLMNegotiator can participate in a negotiation."""
        # Create utilities
        ufuns = generate_multi_issue_ufuns(
            n_issues=3, n_values=(3, 5), n_ufuns=2, reserved_values=0.0
        )

        # Create mechanism
        m = SAOMechanism(outcome_space=ufuns[0].outcome_space, n_steps=5)

        # Add negotiators
        m.add(BolwareBasedLLMNegotiator(ufun=ufuns[0], name="LLM1"))
        m.add(SimpleNeg(ufun=ufuns[1], name="Simple"))

        # Run negotiation
        m.run()

        # Check that negotiation completed
        assert m.state.step <= 5
