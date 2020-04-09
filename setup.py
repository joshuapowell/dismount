#!/usr/bin/env python

"""Dismount.

Copyright (c) 2020 The Dismount Authors.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from setuptools import find_packages
from setuptools import setup

setup(
    name='dismount',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe = False,
    install_requires=[
        'flask',
    ],
)