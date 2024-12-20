#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unit tests for the main methods."""

from pyproject_template.main import get_greeting


def test_get_greeting() -> None:
    """Test getting the greeting string."""
    assert get_greeting().startswith("Hello")
