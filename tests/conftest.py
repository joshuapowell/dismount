#!/usr/bin/env python

"""Dismount.

Copyright (c) 2020 The Dismount Authors.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import pytest

from dismount import application

@pytest.fixture
def app():

    app = application.Application(
        name=__name__,
        environment="testing",
    )

    """A stub for when case app_context is required."""
    with app.app_context():
        pass

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()