.. pyinterpolate documentation master file, created by
   sphinx-quickstart on Tue Oct 13 13:48:47 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pyinterpolate
=============

PyInterpolate is designed as the Python library for geostatistics. It's role is to provide access to spatial statistics tools used in a wide range of studies. If you're:

- GIS expert,
- geologist,
- mining engineer,
- ecologist,
- public health specialist,
- data scientist.

Then this package may be useful for you. You may use it for:

- spatial interpolation and spatial prediction,
- alone or with machine learning libraries,
- for point and areal datasets.

Package was tested in commercial and research projects:

- Tick-borne Disease Detector (prediction of areas of infection risk), research project funded by European Space Agency,
- commercial project related to the prediction of demand for specific flu medications,
- commercial project related to the large-scale infrastructure maintenance.

Pyinterpolate allows you to perform:

- Ordinary Kriging and Simple Kriging (spatial interpolation from points),
- Centroid-based Kriging of Polygons (spatial interpolation from blocks and areas),
- Area-to-area and Area-to-point Poisson Kriging of Polygons (spatial interpolation and data deconvolution from areas to points).

In the future new interpolation techniques will be introduced.


Contents:
---------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Calculate Distances
===================

.. automodule:: pyinterpolate.calculations.distances.calculate_distances
   :members:

Data Processing
===============

.. automodule:: pyinterpolate.data_processing.data_preparation.get_points_within_area
   :members:

.. automodule:: pyinterpolate.data_processing.data_preparation.prepare_areal_shapefile
   :members:

.. automodule:: pyinterpolate.data_processing.data_preparation.read_data
   :members:

Data Transformation
===================

.. automodule:: pyinterpolate.data_processing.data_transformation.get_areal_centroids
   :members:

.. automodule:: pyinterpolate.data_processing.data_transformation.prepare_kriging_data
   :members:

Data Visualization
==================

.. automodule:: pyinterpolate.data_visualization.interpolate_raster
   :members:

Kriging - Areal Kriging
=======================

.. automodule:: pyinterpolate.kriging.areal_poisson_kriging.areal_kriging
   :members:

.. automodule:: pyinterpolate.kriging.areal_poisson_kriging.centroid_based.centroid_poisson_kriging
   :members:

Kriging - Point Kriging
=======================

.. automodule:: pyinterpolate.kriging.point_kriging.kriging
   :members:

Semivariance - Semivariogram Deconvolution
==========================================

.. automodule:: pyinterpolate.semivariance.semivariogram_deconvolution.regularize_semivariogram
   :members:

Semivariance - Semivariogram Estimation
=======================================

.. automodule:: pyinterpolate.semivariance.semivariogram_estimation.calculate_semivariance
   :members:

Semivariance - Fit Semivariogram
================================

.. automodule:: pyinterpolate.semivariance.semivariogram_fit.fit_semivariance
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
