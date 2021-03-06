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

__all__ = ['learn_loop']

from resspect import DataBase


def learn_loop(nloops: int, strategy: str, path_to_features: str,
               output_diag_file: str, output_queried_file: str,
               features_method='Bazin', classifier='RandomForest',
               training='original', batch=1, screen=True, survey='DES',
               perc=0.1, nclass=2):
    """Perform the active learning loop. All results are saved to file.

    Parameters
    ----------
    nloops: int
        Number of active learning loops to run.
    strategy: str
        Query strategy. Options are 'UncSampling' and 'RandomSampling'.
    path_to_features: str or dict
        Complete path to input features file.
        if dict, keywords should be 'train' and 'test', 
        and values must contain the path for separate train 
        and test sample files.
    output_diag_file: str
        Full path to output file to store diagnostics of each loop.
    output_queried_file: str
        Full path to output file to store the queried sample.
    features_method: str (optional)
        Feature extraction method. Currently only 'Bazin' is implemented.
    classifier: str (optional)
        Machine Learning algorithm.
        Currently only 'RandomForest' is implemented.
    training: str or int (optional)
        Choice of initial training sample.
        If 'original': begin from the train sample flagged in the file
        If int: choose the required number of samples at random,
        ensuring that at least half are SN Ia
        Default is 'original'.
    batch: int (optional)
        Size of batch to be queried in each loop. Default is 1.
    screen: bool (optional)
        If True, print on screen number of light curves processed.
    survey: str (optional)
        'DES' or 'LSST'. Default is 'DES'.
        Name of the survey which characterizes filter set.
    perc: float in [0,1] (optioal)
        Percentile chosen to identify the new query. 
        Only used for PercentileSampling. 
        Default is 0.1.
    nclass: int (optional)
        Number of classes to consider in the classification
        Currently only nclass == 2 is implemented.    
    """

    ## This module will need to be expanded for RESSPECT

    # initiate object
    data = DataBase()

    # load features
    if isinstance(path_to_features, str):
        data.load_features(path_to_features, method=features_method,
                           screen=screen, survey=survey)

        # separate training and test samples
        data.build_samples(initial_training=training, nclass=nclass)

    else:
        data.load_features(path_to_features['train'], method=features_method,
                           screen=screen, survey=survey, sample='train')
        data.load_features(path_to_features['test'], method=features_method,
                           screen=screen, survey=survey, sample='test')

        data.build_samples(initial_training=training, nclass=nclass,
                           screen=screen, sep_files=True)
        
    for loop in range(nloops):

        if screen:
            print('Processing... ', loop)

        # classify
        data.classify(method=classifier)

        # calculate metrics
        data.evaluate_classification()

        # choose object to query
        indx = data.make_query(strategy=strategy, batch=batch, perc=perc)

        # update training and test samples
        data.update_samples(indx, loop=loop)

        # save diagnostics for current state
        data.save_metrics(loop=loop, output_metrics_file=output_diag_file,
                          batch=batch, epoch=loop)

        # save query sample to file
        data.save_queried_sample(output_queried_file, loop=loop,
                                 full_sample=False)


def main():
    return None


if __name__ == '__main__':
    main()
