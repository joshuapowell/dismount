
#!/usr/bin/env python

"""Dismount.

Copyright (c) 2020 The Dismount Authors.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import tempfile
import pytest

from dismount import application

# from dismount.db import get_db
# from dismount.db import init_db

# with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
#     _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    # db_fd, db_path = tempfile.mkstemp()

    # app = create_application({
    #     'TESTING': True,
    #     'DATABASE': db_path,
    # })

    app = application.Application(
        name=__name__,
        environment="testing"
    )

    # with app.app_context():
    #     init_db()
    #     get_db().executescript(_data_sql)

    # yield app

    # os.close(db_fd)
    # os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()