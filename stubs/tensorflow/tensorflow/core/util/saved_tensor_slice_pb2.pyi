"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
A checkpoint file is an sstable. The value for each record is a serialized
SavedTensorSlices message (defined below).

Each checkpoint file has a record with the empty key (""), which corresponds
to a SavedTensorSlices message that contains a "meta", that serves as a
table of contents on all the tensor slices saved in this file. Since the key
is "", it's always the first record in each file.

Each of the rest of the records in a checkpoint stores the raw data of a
particular tensor slice, in SavedSlice format. The corresponding key is an
ordered code that encodes the name of the tensor and the slice
information. The name is also stored in the SaveSlice message for ease of
debugging and manual examination.
"""
import builtins
import collections.abc
import sys

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.core.framework.tensor_pb2
import tensorflow.core.framework.tensor_shape_pb2
import tensorflow.core.framework.tensor_slice_pb2
import tensorflow.core.framework.types_pb2
import tensorflow.core.framework.versions_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class SavedSliceMeta(google.protobuf.message.Message):
    """Metadata describing the set of slices of the same tensor saved in a
    checkpoint file.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    SLICE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the tensor."""
    @property
    def shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto:
        """Shape of the tensor"""
    type: tensorflow.core.framework.types_pb2.DataType.ValueType
    """Type of the tensor"""
    @property
    def slice(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.framework.tensor_slice_pb2.TensorSliceProto]:
        """Explicit list of slices saved in the checkpoint file."""
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        type: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        slice: collections.abc.Iterable[tensorflow.core.framework.tensor_slice_pb2.TensorSliceProto] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["shape", b"shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "shape", b"shape", "slice", b"slice", "type", b"type"]) -> None: ...

global___SavedSliceMeta = SavedSliceMeta

@typing_extensions.final
class SavedTensorSliceMeta(google.protobuf.message.Message):
    """Metadata describing the set of tensor slices saved in a checkpoint file.
    It is always stored at the beginning of each checkpoint file.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TENSOR_FIELD_NUMBER: builtins.int
    VERSIONS_FIELD_NUMBER: builtins.int
    @property
    def tensor(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SavedSliceMeta]:
        """Each SavedSliceMeta describes the slices for one tensor."""
    @property
    def versions(self) -> tensorflow.core.framework.versions_pb2.VersionDef:
        """Compatibility version of this checkpoint.  See core/public/version.h
        for version history.
        """
    def __init__(
        self,
        *,
        tensor: collections.abc.Iterable[global___SavedSliceMeta] | None = ...,
        versions: tensorflow.core.framework.versions_pb2.VersionDef | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["versions", b"versions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["tensor", b"tensor", "versions", b"versions"]) -> None: ...

global___SavedTensorSliceMeta = SavedTensorSliceMeta

@typing_extensions.final
class SavedSlice(google.protobuf.message.Message):
    """Saved tensor slice: it stores the name of the tensors, the slice, and the
    raw data.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    SLICE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the tensor that this slice belongs to. This must be identical to
    the name used to encode the key for this record.
    """
    @property
    def slice(self) -> tensorflow.core.framework.tensor_slice_pb2.TensorSliceProto:
        """Extent of the slice.  Must have one entry for each of the dimension of the
        tensor that this slice belongs to.
        """
    @property
    def data(self) -> tensorflow.core.framework.tensor_pb2.TensorProto:
        """The raw data of the slice is stored as a TensorProto. Only raw data are
        stored (we don't fill in fields such as dtype or tensor_shape).
        """
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        slice: tensorflow.core.framework.tensor_slice_pb2.TensorSliceProto | None = ...,
        data: tensorflow.core.framework.tensor_pb2.TensorProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data", b"data", "slice", b"slice"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "name", b"name", "slice", b"slice"]) -> None: ...

global___SavedSlice = SavedSlice

@typing_extensions.final
class SavedTensorSlices(google.protobuf.message.Message):
    """Each record in a v3 checkpoint file is a serialized SavedTensorSlices
    message.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> global___SavedTensorSliceMeta:
        """This is only present at the first item of each checkpoint file and serves
        as a table of contents, listing all the tensor slices saved in this file.
        """
    @property
    def data(self) -> global___SavedSlice:
        """This exists in all but the first item of each checkpoint file."""
    def __init__(
        self,
        *,
        meta: global___SavedTensorSliceMeta | None = ...,
        data: global___SavedSlice | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data", b"data", "meta", b"meta"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "meta", b"meta"]) -> None: ...

global___SavedTensorSlices = SavedTensorSlices
