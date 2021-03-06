# Copyright 2020 RESSPECT software
# Author: The RESSPECT team
#         Initial skeleton taken from ActSNClass
#
# created on 5 March 2020
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

from actsnclass.time_domain_loop import get_original_training

__all__ = ['time_domain_loop', 'get_original_training']

from resspect import DataBase


def time_domain_loop(days: list,  output_diag_file: str,
                     output_queried_file: str,
                     path_to_features_dir: str, strategy: str,
                     batch=1, canonical = False,  classifier='RandomForest',
                     features_method='Bazin', path_to_canonical="",
                     path_to_full_lc_features="",
                     screen=True, training='original'):
    """Perform the active learning loop. All results are saved to file.

    Parameters
    ----------
    days: list
        List of 2 elements. First and last day of observations since the
        beginning of the survey.
    output_diag_file: str
        Full path to output file to store diagnostics of each loop.
    output_queried_file: str
        Full path to output file to store the queried sample.
    path_to_features_dir: str
        Complete path to directory holding features files for all days.
    strategy: str
        Query strategy. Options are 'UncSampling' and 'RandomSampling'.
    batch: int (optional)
        Size of batch to be queried in each loop. Default is 1.
    canonical: bool (optional)
        If True, restrict the search to the canonical sample.
    classifier: str (optional)
        Machine Learning algorithm.
        Currently only 'RandomForest' is implemented.
    features_method: str (optional)
        Feature extraction method. Currently only 'Bazin' is implemented.
    path_to_canonical: str (optional)
        Path to canonical sample features files.
        It is only used if "strategy==canonical".
    path_to_full_lc_features: str (optional)
        Path to full light curve features file.
        Only used if training is a number.
    screen: bool (optional)
        If True, print on screen number of light curves processed.
    training: str or int (optional)
        Choice of initial training sample.
        If 'original': begin from the train sample flagged in the file
        If int: choose the required number of samples at random,
        ensuring that at least half are SN Ia
        Default is 'original'.

    """

    ## This will need to change for RESSPECT

    # initiate object
    data = DataBase()

    # load features for the first day
    path_to_features = path_to_features_dir + 'day_' + str(int(days[0])) + '.dat'
    data.load_features(path_to_features, method=features_method,
                       screen=screen)

    # change training
    if training == 'original':
        data.build_samples(initial_training='original')
        full_lc_features = get_original_training(path_to_features=path_to_full_lc_features)
        data.train_metadata = full_lc_features.train_metadata
        data.train_labels = full_lc_features.train_labels
        data.train_features = full_lc_features.train_features

    else:
        data.build_samples(initial_training=int(training))

    # get list of canonical ids
    if canonical:
        canonical = DataBase()
        canonical.load_features(path_to_file=path_to_canonical)
        data.queryable_ids = canonical.queryable_ids


    for night in range(int(days[0]), int(days[-1]) - 1):

        if screen:
            print('Processing night: ', night)

        # cont loop
        loop = night - int(days[0])

        # classify
        data.classify(method=classifier)

        # calculate metrics
        data.evaluate_classification()

        # choose object to query
        indx = data.make_query(strategy=strategy, batch=batch)

        # update training and test samples
        data.update_samples(indx, loop=loop)

        # save diagnostics for current state
        data.save_metrics(loop=loop, output_metrics_file=output_diag_file,
                          batch=batch, epoch=night)

        # save query sample to file
        data.save_queried_sample(output_queried_file, loop=loop,
                                 full_sample=False)

        # load features for next day
        path_to_features2 = path_to_features_dir + 'day_' + str(night + 1) + '.dat'

        data_tomorrow = DataBase()
        data_tomorrow.load_features(path_to_features2, method=features_method,
                                    screen=False)

        # identify objects in the new day which must be in training
        train_flag = np.array([item in data.train_metadata['id'].values 
                              for item in data_tomorrow.metadata['id'].values])
   
        # use new data        
        data.train_metadata = data_tomorrow.metadata[train_flag]
        data.train_features = data_tomorrow.features.values[train_flag]
        data.test_metadata = data_tomorrow.metadata[~train_flag]
        data.test_features = data_tomorrow.features.values[~train_flag]

        # new labels
        data.train_labels = np.array([int(item  == 'Ia') for item in 
                                     data.train_metadata['type'].values])
        data.test_labels = np.array([int(item == 'Ia') for item in 
                                    data.test_metadata['type'].values])

        if strategy == 'canonical':
            data.queryable_ids = canonical.queryable_ids

        if  queryable:
            queryable_flag = data_tomorrow.metadata['queryable'].values
            queryable_test_flag = np.logical_and(~train_flag, queryable_flag)
            data.queryable_ids = data_tomorrow.metadata['id'].values[queryable_test_flag]
        else:
            data.queryable_ids = data_tomorrow.metadata['id'].values[~train_flag]

        if screen:
            print('Training set size: ', data.train_metadata.shape[0])
            print('Test set size: ', data.test_metadata.shape[0])


def main():
    return None


if __name__ == '__main__':
    main()
