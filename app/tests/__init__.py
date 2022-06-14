from fastapi.testclient import TestClient

from main.__init__ import switch_to_test_mode, TORTOISE_ORM

switch_to_test_mode()

from main.__init__ import schema, app
