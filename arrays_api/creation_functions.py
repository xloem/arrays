def arange(start, /, stop=None, step=1, *, dtype=None, device=None):
    """Returns evenly spaced values within the half-open interval ``[start,
    stop)`` as a one-dimensional array.
    Parameters
    **********
    
    *   **start**: *Union[ int, float ]*
    
        *   if ``stop`` is specified, the start of interval (inclusive);
            otherwise, the end of the interval (exclusive). If ``stop`` is
            not specified, the default starting value is ``0``.
    
    *   **stop**: *Optional[ Union[ int, float ] ]*
    
        *   the end of the interval. Default: ``None``.
    
    Note: This function cannot guarantee that the interval does not include
        the ``stop`` value in those cases where ``step`` is not an integer
        and floating-point rounding errors affect the length of the output
        array.
    
    *   **step**: *Union[ int, float ]*
    
        *   the distance between two adjacent elements (``out[i+1] -
            out[i]``). Must not be ``0``; may be negative, this results in
            an empty array if ``stop >= start``. Default: ``1``.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be inferred from ``start``, ``stop`` and
            ``step``. If those are all integers, the output array dtype
            must be the default integer dtype; if one or more have type
            ``float``, then the output array dtype must be the default
            floating-point data type. Default: ``None``.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. Default: ``None``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   a one-dimensional array containing evenly spaced values. The
            length of the output array must be ``ceil((stop-start)/step)``
            if ``stop - start`` and ``step`` have the same sign, and
            length 0 otherwise."""
    raise NotImplementedError

def asarray(obj, /, *, dtype=None, device=None, copy=None):
    """Convert the input to an array.
    Parameters
    **********
    
    *   **obj**: *Union[ <array>, bool, int, float, NestedSequence[ bool |
        int | float ], SupportsDLPack, SupportsBufferProtocol ]*
    
        *   Object to be converted to an array. Can be a Python scalar, a
            (possibly nested) sequence of Python scalars, or an object
            supporting DLPack or the Python buffer protocol.
    
        Tip: An object supporting DLPack has ``__dlpack__`` and
            ``__dlpack_device__`` methods. An object supporting the buffer
            protocol can be turned into a memoryview through
            ``memoryview(obj)``.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be inferred from the data type(s) in
            ``obj``. If all input values are Python scalars, then if
            they’re all ``bool`` the output dtype will be ``bool``; if
            they’re a mix of ``bool``s and ``int`` the output dtype will
            be the default integer data type; if they contain ``float``s
            the output dtype will be the default floating-point data type.
            Default: ``None``.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. If ``device`` is
            ``None`` and ``x`` is either an array or an object supporting
            DLPack, the output array device must be inferred from ``x``.
            Default: ``None``.
    
    *   **copy**: *Optional[ bool ]*
    
        *   Whether or not to make a copy of the input. If ``True``,
            always copies. If ``False``, never copies for input which
            supports DLPack or the buffer protocol, and raises
            ``ValueError`` in case that would be necessary. If ``None``,
            reuses existing memory buffer if possible, copies otherwise.
            Default: ``None``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   An array containing the data from ``obj``."""
    raise NotImplementedError

def empty(shape, *, dtype=None, device=None):
    """Returns an uninitialized array having a specified ``shape``.
    Parameters
    **********
    
    *   **shape**: *Union[ int, Tuple[ int, … ] ]*
    
        *   output array shape.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be the default floating-point data type.
            Default: ``None``.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. Default: ``None``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing uninitialized data."""
    raise NotImplementedError

def empty_like(x, /, *, dtype=None, device=None):
    """Returns an uninitialized array with the same ``shape`` as an input
    array ``x``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array from which to derive the output array shape.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be inferred from ``x``. Default:
            ``None``.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. If ``device`` is
            ``None``, the output array device must be inferred from ``x``.
            Default: ``None``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array having the same shape as ``x`` and containing
            uninitialized data."""
    raise NotImplementedError

def eye(n_rows, n_cols=None, /, *, k=0, dtype=None, device=None):
    """Returns a two-dimensional array with ones on the ``k``th diagonal and
    zeros elsewhere.
    Parameters
    **********
    
    *   **n_rows**: *int*
    
        *   number of rows in the output array.
    
    *   **n_cols**: *Optional[ int ]*
    
        *   number of columns in the output array. If ``None``, the
            default number of columns in the output array is equal to
            ``n_rows``. Default: ``None``.
    
    *   **k**: *int*
    
        *   index of the diagonal. A positive value refers to an upper
            diagonal, a negative value to a lower diagonal, and ``0`` to
            the main diagonal. Default: ``0``.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be the default floating-point data type.
            Default: ``None``.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. Default: ``None``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array where all elements are equal to zero, except for the
            ``k``th diagonal, whose values are equal to one."""
    raise NotImplementedError

def from_dlpack(x, /):
    """Returns a new array containing the data from another (array) object
    with a ``__dlpack__`` method.
    Parameters
    **********
    
    *   **x**: *object*
    
        *   input (array) object.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the data in ``x``.
    
            Note: The returned array may be either a copy or a view. See
                data-interchange for details."""
    raise NotImplementedError

def full(shape, fill_value, *, dtype=None, device=None):
    """Returns a new array having a specified ``shape`` and filled with
    ``fill_value``.
    Parameters
    **********
    
    *   **shape**: *Union[ int, Tuple[ int, … ] ]*
    
        *   output array shape.
    
    *   **fill_value**: *Union[ int, float ]*
    
        *   fill value.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be inferred from ``fill_value``. If the
            fill value is an ``int``, the output array data type must be
            the default integer data type. If the fill value is a
            ``float``, the output array data type must be the default
            floating-point data type. If the fill value is a ``bool``, the
            output array must have boolean data type. Default: ``None``.
    
            Note: If ``dtype`` is ``None`` and the ``fill_value`` exceeds
                the precision of the resolved default output array data
                type, behavior is left unspecified and, thus,
                implementation-defined.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. Default: ``None``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array where every element is equal to ``fill_value``."""
    raise NotImplementedError

def full_like(x, /, fill_value, *, dtype=None, device=None):
    """Returns a new array filled with ``fill_value`` and having the same
    ``shape`` as an input array ``x``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array from which to derive the output array shape.
    
    *   **fill_value**: *Union[ int, float ]*
    
        *   fill value.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be inferred from ``x``. Default:
            ``None``.
    
            Note: If ``dtype`` is ``None`` and the ``fill_value`` exceeds
                the precision of the resolved output array data type,
                behavior is unspecified and, thus, implementation-defined.
    
            Note: If ``dtype`` is ``None`` and the ``fill_value`` has a data
                type (``int`` or ``float``) which is not of the same data
                type kind as the resolved output array data type (see
                `Type Promotion Rules <#type-promotion>`_), behavior is
                unspecified and, thus, implementation-defined.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. If ``device`` is
            ``None``, the output array device must be inferred from ``x``.
            Default: ``None``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array having the same shape as ``x`` and where every
            element is equal to ``fill_value``."""
    raise NotImplementedError

def linspace(start, stop, /, num, *, dtype=None, device=None, endpoint=True):
    """Returns evenly spaced numbers over a specified interval.
    Parameters
    **********
    
    *   **start**: *Union[ int, float ]*
    
        *   the start of the interval.
    
    *   **stop**: *Union[ int, float ]*
    
        *   the end of the interval. If ``endpoint`` is ``False``, the
            function must generate a sequence of ``num+1`` evenly spaced
            numbers starting with ``start`` and ending with ``stop`` and
            exclude the ``stop`` from the returned array such that the
            returned array consists of evenly spaced numbers over the
            half-open interval ``[start, stop)``. If ``endpoint`` is
            ``True``, the output array must consist of evenly spaced
            numbers over the closed interval ``[start, stop]``. Default:
            ``True``.
    
            Note: The step size changes when ``endpoint`` is ``False``.
    
    *   **num**: *int*
    
        *   number of samples. Must be a non-negative integer value;
            otherwise, the function must raise an exception.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be the default floating-point data type.
            Default: ``None``.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. Default: ``None``.
    
    *   **endpoint**: *bool*
    
        *   boolean indicating whether to include ``stop`` in the
            interval. Default: ``True``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   a one-dimensional array containing evenly spaced values."""
    raise NotImplementedError

def meshgrid(*arrays, indexing='xy'):
    """Returns coordinate matrices from coordinate vectors.
    Parameters
    **********
    
    *   **arrays**: *<array>*
    
        *   an arbitrary number of one-dimensional arrays representing
            grid coordinates. Must have numeric data types.
    
    *   **indexing**: *str*
    
        *   Cartesian ‘xy’ or matrix ‘ij’ indexing of output. If provided
            zero or one one-dimensional vector(s) (i.e., the zero- and
            one-dimensional cases, respectively), the ``indexing`` keyword
            has no effect and should be ignored. Default: ``'xy'``.
    Returns
    *******
    
    *   **out**: *List[ <array>, … ]*
    
        *   list of N arrays, where ``N`` is the number of provided
            one-dimensional input arrays. Each returned array must have
            rank ``N``. For ``N`` one-dimensional arrays having lengths
            ``Ni = len(xi)``,
    
            *   if matrix indexing ``ij``, then each returned array must
                have the shape ``(N1, N2, N3, ..., Nn)``.
    
            *   if Cartesian indexing ``xy``, then each returned array
                must have shape ``(N2, N1, N3, ..., Nn)``.
    
            Accordingly, for the two-dimensional case with input
            one-dimensional arrays of length ``M`` and ``N``, if matrix
            indexing ``ij``, then each returned array must have shape
            ``(M, N)``, and, if Cartesian indexing ``xy``, then each
            returned array must have shape ``(N, M)``.
    
            Similarly, for the three-dimensional case with input
            one-dimensional arrays of length ``M``, ``N``, and ``P``, if
            matrix indexing ``ij``, then each returned array must have
            shape ``(M, N, P)``, and, if Cartesian indexing ``xy``, then
            each returned array must have shape ``(N, M, P)``.
    
            The returned arrays must have a numeric data type determined
            by `Type Promotion Rules <#type-promotion>`_."""
    raise NotImplementedError

def ones(shape, *, dtype=None, device=None):
    """Returns a new array having a specified ``shape`` and filled with ones.
    Parameters
    **********
    
    *   **shape**: *Union[ int, Tuple[ int, … ] ]*
    
        *   output array shape.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be the default floating-point data type.
            Default: ``None``.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. Default: ``None``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing ones."""
    raise NotImplementedError

def ones_like(x, /, *, dtype=None, device=None):
    """Returns a new array filled with ones and having the same ``shape`` as
    an input array ``x``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array from which to derive the output array shape.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be inferred from ``x``. Default:
            ``None``.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. If ``device`` is
            ``None``, the output array device must be inferred from ``x``.
            Default: ``None``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array having the same shape as ``x`` and filled with ones."""
    raise NotImplementedError

def tril(x, /, *, k=0):
    """Returns the lower triangular part of a matrix (or a stack of matrices)
    ``x``.
    Note: The lower triangular part of the matrix is defined as the elements
        on and below the specified diagonal ``k``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array having shape ``(..., M, N)`` and whose innermost
            two dimensions form ``MxN`` matrices.
    
    *   **k**: *int*
    
        *   diagonal above which to zero elements. If ``k = 0``, the
            diagonal is the main diagonal. If ``k < 0``, the diagonal is
            below the main diagonal. If ``k > 0``, the diagonal is above
            the main diagonal. Default: ``0``.
    
            Note: The main diagonal is defined as the set of indices ``{(i,
                i)}`` for ``i`` on the interval ``[0, min(M, N) - 1]``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the lower triangular part(s). The returned
            array must have the same shape and data type as ``x``. All
            elements above the specified diagonal ``k`` must be zeroed.
            The returned array should be allocated on the same device as
            ``x``."""
    raise NotImplementedError

def triu(x, /, *, k=0):
    """Returns the upper triangular part of a matrix (or a stack of matrices)
    ``x``.
    Note: The upper triangular part of the matrix is defined as the elements
        on and above the specified diagonal ``k``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array having shape ``(..., M, N)`` and whose innermost
            two dimensions form ``MxN`` matrices.
    
    *   **k**: *int*
    
        *   diagonal below which to zero elements. If ``k = 0``, the
            diagonal is the main diagonal. If ``k < 0``, the diagonal is
            below the main diagonal. If ``k > 0``, the diagonal is above
            the main diagonal. Default: ``0``.
    
            Note: The main diagonal is defined as the set of indices ``{(i,
                i)}`` for ``i`` on the interval ``[0, min(M, N) - 1]``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing the upper triangular part(s). The returned
            array must have the same shape and data type as ``x``. All
            elements below the specified diagonal ``k`` must be zeroed.
            The returned array should be allocated on the same device as
            ``x``."""
    raise NotImplementedError

def zeros(shape, *, dtype=None, device=None):
    """Returns a new array having a specified ``shape`` and filled with
    zeros.
    Parameters
    **********
    
    *   **shape**: *Union[ int, Tuple[ int, … ] ]*
    
        *   output array shape.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be the default floating-point data type.
            Default: ``None``.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. Default: ``None``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array containing zeros."""
    raise NotImplementedError

def zeros_like(x, /, *, dtype=None, device=None):
    """Returns a new array filled with zeros and having the same ``shape`` as
    an input array ``x``.
    Parameters
    **********
    
    *   **x**: *<array>*
    
        *   input array from which to derive the output array shape.
    
    *   **dtype**: *Optional[ <dtype> ]*
    
        *   output array data type. If ``dtype`` is ``None``, the output
            array data type must be inferred from ``x``. Default:
            ``None``.
    
    *   **device**: *Optional[ <device> ]*
    
        *   device on which to place the created array. If ``device`` is
            ``None``, the output array device must be inferred from ``x``.
            Default: ``None``.
    Returns
    *******
    
    *   **out**: *<array>*
    
        *   an array having the same shape as ``x`` and filled with zeros."""
    raise NotImplementedError

