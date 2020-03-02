# Copyright 2019 actsnclass software
# Author: Emille E. O. Ishida
#         Based on initial prototype developed by the CRP #4 team
#
# created on 7 August 2019
#
# Licensed GNU General Public License v3.0;
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/gpl-3.0.en.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools


setuptools.setup(
    name='RESSPECT',
    version='0.1',
    packages=setuptools.find_packages(),
    py_modules=['classifiers',
                'data_base',
                'fit_lightcurves',
                'learn_loop',
                'metrics',
                'plot_results',
                'query_strategies',
                'time_domain'],
    scripts=[],
    url='https://github.com/COINtoolbox/RESSPECT',
    license='GNU3',
    author='The RESSPECT team',
    author_email='emille@cosmostatistics-initiative.org',
    description='Recommendation System for Spectroscopic follow-up'
)
