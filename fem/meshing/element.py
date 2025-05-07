from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class ElementType(Enum):
    Point         = auto()
    Segment       = auto()
    Triangle      = auto()
    Quadrilateral = auto()
    Tetrahedron   = auto()
    Hexahedron    = auto()

@dataclass
class Element(ABC):
    @abstractmethod
    def get_element_type(self) -> ElementType:
        pass

    @abstractmethod
    def get_vertices(self) -> List[int]:
        pass

    @abstractmethod
    def set_vertices(self, vertices: List[int]):
        pass

    @abstractmethod
    def get_n_vertices(self) -> int:
        pass

    @abstractmethod
    def get_n_edges(self) -> int:
        pass

    @abstractmethod
    def get_edge_vertices(self, edge_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_n_faces(self) -> int:
        pass

    @abstractmethod
    def get_n_face_vertices(self, face_id: int) -> int:
        pass

    @abstractmethod
    def get_face_vertices(self, face_id: int) -> List[int]:
        pass