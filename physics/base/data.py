from abc import ABC, abstractmethod
import jax.numpy as jnp

class FunctionBase(ABC):
    @abstractmethod
    def get_state(self, physics, x, t):
        pass

class BoundaryConditionBase(ABC):
    @abstractmethod
    def get_boundary_state(self, physics, UqI, normals, x, t):
        pass

    @abstractmethod
    def get_boundary_flux(self, physics, UqI, normals, x, t, gUq=None):
        pass

class BoundaryConditionWeakRiemann(BoundaryConditionBase):
    def get_boundary_flux(self, physics, UqI, normals, x, t, gUq=None):
        pass

class BoundaryConditionWeakPrescribed(BoundaryConditionBase):
    def get_boundary_flux(self, physics, UqI, normals, x, t, gUq=None):
        pass

class SourceBase(ABC):
    def __init__(self, kwargs=None):
        if kwargs:
            self.source_treatment = kwargs['source_treatment']
        else:
            self.source_treatment = 'Implicit'

    @abstractmethod
    def get_source(self, physics, Uq, x, t):
        pass

    @abstractmethod
    def get_jacobian(self, physics, Uq, x, t):
        pass

class ConvNumFluxBase(ABC):
    def __init__(self, Uq=None):
        super().__init__()

    def alloc_helpers(self, Uq):
        self.__init__(Uq)

    @abstractmethod
    def compute_flux(self, physics, UqL, UqR, normals):
        pass

class DiffNumFluxBase(ABC):
    def __init__(self, Uq=None):
        super().__init__()

    def alloc_helpers(self, Uq):
        self.__init__(Uq)

    @abstractmethod
    def compute_flux(self, physics, UqL, UqR, normals):
        pass
