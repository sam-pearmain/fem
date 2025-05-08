from abc import ABC, abstractmethod
from enum import Enum

class PhysicsBase(ABC):
    @property
    @abstractmethod
    def NUM_STATE_VARS(self) -> int:
        pass

    @property
    @abstractmethod
    def NUM_DIMS(self) -> int:
        pass

    @property
    @abstractmethod
    def PHYSICS_TYPE(self) -> PhysicsType:
        pass

    @abstractmethod
    class StateVariables(Enum):
        pass

    @abstractmethod
    class AdditionalVariables(Enum):
        pass

    def set_physical_params(self):
        pass

    def set_maps(self):
        # todo
        pass

    def set_intial_condition(self, initial_condition_type, **kwargs):
        pass

    def set_boundary_condition(self, boundary, boundary_condition_type, fcn_type=None, **kwargs):
        pass

    def set_source(self, source_type):
        pass

    def set_conv_num_flux(self, conv_num_flux_type, **kwargs):
        pass

    def set_diff_num_flux(self, diff_num_flux_type, **kwargs):
        pass

    def get_state_index(self, var_name):
        return self.state.state_indices[var_name]
    
    def get_state_slice(self, var_name):
        return self.state.state_slice[var_name]
    
    def get_quadrature_order(self, order):
        return 2 * order + 1
    
    @abstractmethod
    def get_conv_flux_interior(self, Uq):
        pass

    def get_diff_flux_interior(self, Uq, gUq):
        pass

    def get_conv_flux_projected(self, Uq, normals):
        pass

    def get_conv_flux_numerical(self, UqL, UqR, normals):
        pass

    def get_diff_flux_numerical(self, UqL, UqR, gUqL, gUqR, normals):
        pass

    def get_diff_boundary_flux_numerical(self, UqI, UqB, gUq, normals):
        pass

    def eval_source_terms(self, Uq, xphys, time, Sq):
        pass

    def eval_source_term_jacobians(self, Uq, xphys, time, jac):
        pass

    def compute_variable(self, var_name, Uq, flag_non_physical=False):
        pass    

    def compute_additional_variable(self, var_name, Uq, flag_non_physical=False):
        pass