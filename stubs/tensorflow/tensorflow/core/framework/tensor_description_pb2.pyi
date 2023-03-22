"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import tensorflow.core.framework.allocation_description_pb2
import tensorflow.core.framework.tensor_shape_pb2
import tensorflow.core.framework.types_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class TensorDescription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DTYPE_FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    ALLOCATION_DESCRIPTION_FIELD_NUMBER: builtins.int
    dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
    """Data type of tensor elements"""
    @property
    def shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto:
        """Shape of the tensor."""
    @property
    def allocation_description(self) -> tensorflow.core.framework.allocation_description_pb2.AllocationDescription:
        """Information about the size and allocator used for the data"""
    def __init__(
        self,
        *,
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        allocation_description: tensorflow.core.framework.allocation_description_pb2.AllocationDescription | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["allocation_description", b"allocation_description", "shape", b"shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allocation_description", b"allocation_description", "dtype", b"dtype", "shape", b"shape"]) -> None: ...

global___TensorDescription = TensorDescription
