# coding=utf-8

"""Dismount.

Copyright (c) 2020 The Dismount Authors.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys

from . import flask
from . import logger

class Application(object):
    """Create class-based Flask application."""

    def __init__(self, name, environment="default", ):
        """Constructor.

        :param (class) self
            The representation of the instantiated Class Instance
        :param (str) name
            The name of the application
        :param (str) environment
            The name of the enviornment in which to load the application
        """
        self.name = name
        self.environment = environment

        """Create our base Flask application
        """
        logger.info('Starting Dismount')
        app = flask.Flask(__name__, static_url_path='/static')

        self.app = app

        """Import configuration based on environment.
        """
        logger.info('Opening environment configuration file')
        _config = ('../config/%s.json') % (environment)

        """Parse the JSON configuration file content.
        """
        logger.info('Loading environment variables from configuration file')
        self.app.config.from_json(_config)

        logger.info('Dismount exited with 0.')