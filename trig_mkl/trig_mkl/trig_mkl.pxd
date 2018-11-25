# Copyright (c) 2016-2017 LCODE team <team@lcode.info>.

# LCODE is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# LCODE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with LCODE.  If not, see <http://www.gnu.org/licenses/>.

# cython: language_level=3, unraisable_tracebacks=True, profile=True

from mkl_types cimport MKL_INT
from mkl_dfti cimport DFTI_DESCRIPTOR_HANDLE

cdef class TrigTransform:
    cdef MKL_INT n
    cdef MKL_INT tt_type
    cdef int num_threads
    cdef MKL_INT **ipar
    cdef double *dpar
    cdef DFTI_DESCRIPTOR_HANDLE *handles

    cpdef double[:] dst_1d(TrigTransform self, double[:] x)
    cpdef double[:] dct_1d(TrigTransform self, double[:] x)
    cpdef double[:, :] dst_2d(TrigTransform self, double[:, :] x)
    cpdef double[:, :] dct_2d(TrigTransform self, double[:, :] x)
    cpdef double[:, :] idct_2d(TrigTransform self, double[:, :] x)

    cdef MKL_INT _forward(self, double *data, int thread) nogil
    cdef MKL_INT _backward(self, double *data, int thread) nogil
    #cdef MKL_INT _commit(self, double *data, int thread) nogil
