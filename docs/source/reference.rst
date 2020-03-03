***************
Reference / API
***************

.. currentmodule:: resspect

Pre-processing
==============

Light curve analysis
-------------------------

*Performing feature extraction for 1 light curve*

.. autosummary::
   :toctree: api

   fit_lightcurves.LightCurve
   fit_lightcurves.LightCurve.check_queryable
   fit_lightcurves.LightCurve.evaluate_bazin
   fit_lightcurves.LightCurve.load_plasticc_lc
   fit_lightcurves.LightCurve.load_resspect_lc
   fit_lightcurves.LightCurve.load_snpcc_lc
   fit_lightcurves.LightCurve.fit_bazin
   fit_lightcurves.LightCurve.fit_bazin_all
   fit_lightcurves.LightCurve.plot_bazin_fit

*Fitting an entire data set*

.. autosummary::
   :toctree: api

   fit_plasticc_bazin
   fit_resspect_bazin


Build time domain data base
===========================

*For PLAsTiCC data*

.. autosummary::
   :toctree: api

   PLAsTiCCPhotometry
   PLAsTiCCPhotometry.build_one_epoch
   PLAsTiCCPhotometry.create_all_daily_files
   PLAsTiCCPhotometry.create_daily_file
   PLAsTiCCPhotometry.fit_one_lc
   PLAsTiCCPhotometry.read_metadata
   PLAsTiCCPhotometry.write_bazin_to_file


DataBase
========

*Object upon which the learning process is performed*

.. autosummary::
   :toctree: api

    DataBase
    DataBase.build_samples
    DataBase.classify
    DataBase.evaluate_classification
    DataBase.load_bazin_features
    DataBase.load_features
    DataBase.load_plasticc_mjd
    DataBase.make_query
    DataBase.update_samples
    DataBase.save_metrics
    DataBase.save_queried_sample


Classifiers
===========

.. autosummary::
   :toctree: api

   classifiers.knn


Query strategies
================

.. autosummary::
   :toctree: api

   query_strategies.percentile_sampling


Active Learning loop
====================

*Full light curve*

.. autosummary::
   :toctree: api

    learn_loop

*Time domain*

.. autosummary::
   :toctree: api

    get_original_training
    time_domain_loop.time_domain_loop


Plotting
========

.. autosummary::
   :toctree: api

    Canvas.load_diagnostics
    Canvas.set_plot_dimensions
    Canvas.plot_diagnostics

