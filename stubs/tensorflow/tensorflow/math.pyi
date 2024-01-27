from _typeshed import Incomplete
from collections.abc import Iterable
from typing import TypeVar, overload
from typing_extensions import TypeAlias

from tensorflow import IndexedSlices, RaggedTensor, Tensor
from tensorflow._aliases import _DTypeLike, _ShapeLike, _TensorCompatible
from tensorflow.sparse import SparseTensor

_TensorCompatibleT = TypeVar("_TensorCompatibleT", bound=_TensorCompatible)
_SparseTensorCompatible: TypeAlias = _TensorCompatible | SparseTensor

# Most operations support RaggedTensor. Documentation for them is here,
# https://www.tensorflow.org/api_docs/python/tf/ragged.
# Most operations do not support SparseTensor. Operations often don't document
# whether they support SparseTensor and it is best to test them manually. Typically
# if an operation outputs non-zero value for a zero input, it will not support
# SparseTensors. Binary operations with ragged tensors usually only work
# if both operands are ragged.
@overload
def abs(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def abs(x: SparseTensor, name: str | None = None) -> SparseTensor: ...
@overload
def abs(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def sin(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def sin(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def cos(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def cos(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def exp(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def exp(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def sinh(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def sinh(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def cosh(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def cosh(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def tanh(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def tanh(x: SparseTensor, name: str | None = None) -> SparseTensor: ...
@overload
def tanh(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def expm1(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def expm1(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def log(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def log(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def log1p(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def log1p(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def negative(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def negative(x: SparseTensor, name: str | None = None) -> SparseTensor: ...
@overload
def negative(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def sigmoid(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def sigmoid(x: SparseTensor, name: str | None = None) -> SparseTensor: ...
@overload
def add(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def add(x: RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def add_n(inputs: Iterable[_TensorCompatible | IndexedSlices], name: str | None = None) -> Tensor: ...
@overload
def add_n(inputs: Iterable[RaggedTensor], name: str | None = None) -> RaggedTensor: ...
@overload
def subtract(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def subtract(x: _TensorCompatible | RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def subtract(
    x: _TensorCompatible | RaggedTensor, y: _TensorCompatible | RaggedTensor, name: str | None = None
) -> Tensor | RaggedTensor: ...
@overload
def multiply(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def multiply(x: RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def multiply_no_nan(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def multiply_no_nan(x: RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def divide(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def divide(x: RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def divide_no_nan(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def divide_no_nan(x: RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def floormod(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def floormod(x: RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def ceil(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def ceil(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def floor(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def floor(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...

# Uses isinstance on list/tuple so other Sequence types are not supported. The TypeVar is to
# behave covariantly.
def accumulate_n(
    inputs: list[_TensorCompatibleT] | tuple[_TensorCompatibleT, ...],
    shape: _ShapeLike | None = None,
    tensor_dtype: _DTypeLike | None = None,
    name: str | None = None,
) -> Tensor: ...
@overload
def pow(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def pow(x: RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def reciprocal(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def reciprocal(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def is_nan(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def is_nan(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def minimum(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def minimum(x: RaggedTensor, y: _TensorCompatible | RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def minimum(x: _TensorCompatible | RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def maximum(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def maximum(x: RaggedTensor, y: _TensorCompatible | RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def maximum(x: _TensorCompatible | RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def logical_not(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def logical_not(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def logical_and(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def logical_and(x: RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def logical_or(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def logical_or(x: RaggedTensor, y: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def logical_xor(x: _TensorCompatible, y: _TensorCompatible, name: str | None = "LogicalXor") -> Tensor: ...
@overload
def logical_xor(x: RaggedTensor, y: RaggedTensor, name: str | None = "LogicalXor") -> RaggedTensor: ...
@overload
def equal(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def equal(x: RaggedTensor, y: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
@overload
def not_equal(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def not_equal(x: RaggedTensor, y: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
@overload
def greater(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def greater(x: RaggedTensor, y: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
@overload
def greater_equal(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def greater_equal(x: RaggedTensor, y: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
@overload
def less(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def less(x: RaggedTensor, y: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
@overload
def less_equal(x: _TensorCompatible, y: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def less_equal(x: RaggedTensor, y: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
def segment_sum(data: _TensorCompatible, segment_ids: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def sign(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def sign(x: SparseTensor, name: str | None = None) -> SparseTensor: ...
@overload
def sign(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def sqrt(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def sqrt(x: SparseTensor, name: str | None = None) -> SparseTensor: ...
@overload
def sqrt(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def rsqrt(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def rsqrt(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def square(x: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def square(x: SparseTensor, name: str | None = None) -> SparseTensor: ...
@overload
def square(x: RaggedTensor, name: str | None = None) -> RaggedTensor: ...
@overload
def softplus(features: _TensorCompatible, name: str | None = None) -> Tensor: ...
@overload
def softplus(features: RaggedTensor, name: str | None = None) -> RaggedTensor: ...

# Depending on the method axis is either a rank 0 tensor or a rank 0/1 tensor.
def reduce_mean(
    input_tensor: _TensorCompatible | RaggedTensor,
    axis: _TensorCompatible | None = None,
    keepdims: bool = False,
    name: str | None = None,
) -> Tensor: ...
def reduce_sum(
    input_tensor: _TensorCompatible | RaggedTensor,
    axis: _TensorCompatible | None = None,
    keepdims: bool = False,
    name: str | None = None,
) -> Tensor: ...
def reduce_max(
    input_tensor: _TensorCompatible | RaggedTensor,
    axis: _TensorCompatible | None = None,
    keepdims: bool = False,
    name: str | None = None,
) -> Tensor: ...
def reduce_min(
    input_tensor: _TensorCompatible | RaggedTensor,
    axis: _TensorCompatible | None = None,
    keepdims: bool = False,
    name: str | None = None,
) -> Tensor: ...
def reduce_prod(
    input_tensor: _TensorCompatible | RaggedTensor,
    axis: _TensorCompatible | None = None,
    keepdims: bool = False,
    name: str | None = None,
) -> Tensor: ...
def reduce_std(
    input_tensor: _TensorCompatible | RaggedTensor,
    axis: _TensorCompatible | None = None,
    keepdims: bool = False,
    name: str | None = None,
) -> Tensor: ...
def argmax(
    input: _TensorCompatible, axis: _TensorCompatible | None = None, output_type: _DTypeLike = ..., name: str | None = None
) -> Tensor: ...
def argmin(
    input: _TensorCompatible, axis: _TensorCompatible | None = None, output_type: _DTypeLike = ..., name: str | None = None
) -> Tensor: ...

# Only for bool tensors.
def reduce_any(
    input_tensor: _TensorCompatible | RaggedTensor,
    axis: _TensorCompatible | None = None,
    keepdims: bool = False,
    name: str | None = None,
) -> Tensor: ...
def reduce_all(
    input_tensor: _TensorCompatible | RaggedTensor,
    axis: _TensorCompatible | None = None,
    keepdims: bool = False,
    name: str | None = None,
) -> Tensor: ...
def count_nonzero(
    input: _SparseTensorCompatible,
    axis: _TensorCompatible | None = None,
    keepdims: bool | None = None,
    dtype: _DTypeLike = ...,
    name: str | None = None,
) -> Tensor: ...
def __getattr__(name: str) -> Incomplete: ...
