# Copyright 2020 RESSPECT software
# Author: The RESSPECT team
#         Initial skeleton from ActSNClass
#
# created on 2 March 2020
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

from actsnclass.bazin import *
from actsnclass.build_snpcc_canonical import *
from actsnclass.build_snpcc_canonical import *
from actsnclass.classifiers import *
from actsnclass.learn_loop import *
from actsnclass.metrics import *
from actsnclass.query_strategies import *
from actsnclass.plot_results import *
from actsnclass.scripts.build_canonical import main as build_canonical
from actsnclass.scripts.build_time_domain import main as build_time_domain
from actsnclass.scripts.fit_dataset import main as fit_dataset
from actsnclass.scripts.make_diagnostic_plots import main as make_diagnostic_plots
from actsnclass.scripts.run_loop import main as run_loop
from actsnclass.scripts.run_time_domain import main as run_time_domain
from actsnclass.time_domain import *
from actsnclass.time_domain_loop import get_original_training

from .database import *
from .fit_lightcurves import *
from .time_domain_PLAsTiCC import *


__all__ = ['accuracy',
           'bazin',
           'build_canonical',
           'build_snpcc_canonical',
           'Canonical',
           'Canvas',
           'DataBase',
           'efficiency',
           'fit_dataset',
           'fit_scipy',
           'fit_snpcc_bazin',
           'fit_plasticc_bazin',
           'fit_resspect_bazin',
           'fom',
           'get_snpcc_metric',
           'learn_loop',
           'LightCurve',
           'make_diagnostic_plots',
           'PLAsTiCCPhotometry',
           'plot_snpcc_train_canonical',
           'purity',
           'random_forest',
           'knn',
           'random_sampling',
           'run_loop',
           'run_time_domain',
           'SNPCCPhotometry',
           'uncertainty_sampling']
