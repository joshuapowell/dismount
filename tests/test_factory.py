#!/usr/bin/env python

"""Dismount.

Copyright (c) 2020 The Dismount Authors.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from dismount import application

def test_config():

    assert not application.Application(
        name=__name__
    ).app.testing
    assert application.Application(
        name=__name__,
        environment="testing"
    ).app.testing
