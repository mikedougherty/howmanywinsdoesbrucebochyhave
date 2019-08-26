#!/usr/bin/env python

from .__version__ import __version__
from .howmanywinsdoesbrucebochyhave import create_app

app = create_app()

__all__ = ["__version__", "app", "create_app"]
