# Base libraries
import numpy as np

# Pyinterpolate libraries
from pyinterpolate.kriging.semivariance_areal import ArealSemivariance
from pyinterpolate.kriging.semivariance_base import Semivariance


def calculate_semivariogram_deviation(data_based_semivariogram, theoretically_regularized_semivariogram):
    """Function calculates deviation between experimental and theoretical semivariogram
    over given lags.
    
    INPUT:
    :param data_based_semivariogram: data based semivariogram in the form of numpy array:
    [[lag 0, value 0],
     [lag i, value i],
     [lag z, value z]]
    
    :param theoretically_regularized_semivariogram: array in the same for as data_based_semivariogram,
    where first column represents the same lags as the first column of the data_based_semivariogram array.
    
    OUTPUT:
    :return deviation: scalar which describes deviation between semivariograms.
     """
    
    array_length = len(data_based_semivariogram)
    
    if array_length == len(theoretically_regularized_semivariogram):
        if (data_based_semivariogram[:, 0] == theoretically_regularized_semivariogram[:, 0]).any():
            print('Start of deviation calculation')
            deviation = np.abs(theoretically_regularized_semivariogram[:, 1] - data_based_semivariogram[:, 1])
            deviation = deviation / data_based_semivariogram[:, 1]
            deviation = sum(deviation) / array_length
            print('Calculated deviation is:', deviation)
            return deviation
        else:
            raise ValueError('Semivariograms have a different lags')
    else:
        raise ValueError('Length of data based semivariogram is different than length of theoretical semivariogram')


class DeconvolutedModel:
    """Class is a pipeline for deconvolution of areal data"""

    def __init__(self):
        
        # Models
        self.initial_point_support_model = None
        self.optimal_point_support_model = None
        self.optimal_regularized_model = None
        self.optimal_difference_statistics = None
        self.weights = 0

        # Loop parameters
        self.iteration_number = 0
        self.sill_of_areal_data = None
        self.difference_statistics_ratio = 1
        self.difference_statistics_limit = 0.01
        self.difference_statistics_decrease_number = 3
        
        # Areal Semivariance models
        self.within_block_semivariogram = None
        self.semivariogram_between_blocks = None
        
        # Additional
        self.centroid_distances = None
        self.areal_distances = None


    def regularize(self, areal_data_file, areal_lags, areal_step_size, data_column,
                 population_data_file, population_value_column, population_lags, population_step_size,
                 id_column_name):

        areal_semivariance = ArealSemivariance(areal_data_file, areal_lags, areal_step_size, data_column,
                 population_data_file, population_value_column, population_lags, population_step_size,
                 id_column_name)
        
        # Point support model
        centroids_semivar = Semivariance(areal_data_file, lags=population_lags,
                                          step_size=population_step_size,
                                          id_field=id_column_name)
        self.initial_point_support_model = centroids_semivar.centroids_semivariance(data_column='LB RATES 2')
        self.centroid_distances = centroids_semivar.distances
        self.optimal_point_support_model = self.initial_point_support_model.copy()
        
        
        # Regularized Model
        regularized = areal_semivariance.blocks_semivariance()
        self.areal_distances = areal_semivariance.areal_distances
        self.within_block_semivariogram = areal_semivariance.within_block_semivariogram
        self.semivariogram_between_blocks = areal_semivariance.semivariogram_between_blocks
        self.optimal_regularized_model = regularized
        
        # Deviation
        deviation = calculate_semivariogram_deviation(self.optimal_point_support_model, regularized)
        self.optimal_difference_statistics = deviation
        
        return self.optimal_point_support_model, self.optimal_regularized_model