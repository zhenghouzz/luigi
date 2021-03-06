# Copyright (c) 2012 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from distutils.core import setup

setup(name='luigi',
      version='1.0',
      description='Workflow mgmgt + task scheduling + dependency resolution',
      author='Erik Bernhardsson',
      author_email='erikbern@spotify.com',
      packages=[
        'luigi'
        ],
      package_data={
        'luigi': ['static/*']
        },
      )
