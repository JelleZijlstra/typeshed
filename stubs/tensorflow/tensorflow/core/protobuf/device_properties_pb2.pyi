"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2017 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class DeviceProperties(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class EnvironmentEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: builtins.str | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    TYPE_FIELD_NUMBER: builtins.int
    VENDOR_FIELD_NUMBER: builtins.int
    MODEL_FIELD_NUMBER: builtins.int
    FREQUENCY_FIELD_NUMBER: builtins.int
    NUM_CORES_FIELD_NUMBER: builtins.int
    ENVIRONMENT_FIELD_NUMBER: builtins.int
    NUM_REGISTERS_FIELD_NUMBER: builtins.int
    L1_CACHE_SIZE_FIELD_NUMBER: builtins.int
    L2_CACHE_SIZE_FIELD_NUMBER: builtins.int
    L3_CACHE_SIZE_FIELD_NUMBER: builtins.int
    SHARED_MEMORY_SIZE_PER_MULTIPROCESSOR_FIELD_NUMBER: builtins.int
    MEMORY_SIZE_FIELD_NUMBER: builtins.int
    BANDWIDTH_FIELD_NUMBER: builtins.int
    type: builtins.str
    """Device type (CPU, GPU, ...)"""
    vendor: builtins.str
    """Vendor (Intel, nvidia, ...)"""
    model: builtins.str
    """Model (Haswell, K40, ...)"""
    frequency: builtins.int
    """Core Frequency in Mhz"""
    num_cores: builtins.int
    """Number of cores"""
    @property
    def environment(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Version of the tools and libraries used with this device (e.g. gcc 4.9,
        cudnn 5.1)
        """
    num_registers: builtins.int
    """Number of registers per core."""
    l1_cache_size: builtins.int
    """L1 cache size in bytes"""
    l2_cache_size: builtins.int
    """L2 cache size in bytes"""
    l3_cache_size: builtins.int
    """L3 cache size in bytes"""
    shared_memory_size_per_multiprocessor: builtins.int
    """Shared memory size per multiprocessor in bytes. This field is
    applicable to GPUs only.
    """
    memory_size: builtins.int
    """Memory size in bytes"""
    bandwidth: builtins.int
    """Memory bandwidth in KB/s"""
    def __init__(
        self,
        *,
        type: builtins.str | None = ...,
        vendor: builtins.str | None = ...,
        model: builtins.str | None = ...,
        frequency: builtins.int | None = ...,
        num_cores: builtins.int | None = ...,
        environment: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        num_registers: builtins.int | None = ...,
        l1_cache_size: builtins.int | None = ...,
        l2_cache_size: builtins.int | None = ...,
        l3_cache_size: builtins.int | None = ...,
        shared_memory_size_per_multiprocessor: builtins.int | None = ...,
        memory_size: builtins.int | None = ...,
        bandwidth: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bandwidth", b"bandwidth", "environment", b"environment", "frequency", b"frequency", "l1_cache_size", b"l1_cache_size", "l2_cache_size", b"l2_cache_size", "l3_cache_size", b"l3_cache_size", "memory_size", b"memory_size", "model", b"model", "num_cores", b"num_cores", "num_registers", b"num_registers", "shared_memory_size_per_multiprocessor", b"shared_memory_size_per_multiprocessor", "type", b"type", "vendor", b"vendor"]) -> None: ...

global___DeviceProperties = DeviceProperties

@typing_extensions.final
class NamedDevice(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def properties(self) -> global___DeviceProperties: ...
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        properties: global___DeviceProperties | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["properties", b"properties"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "properties", b"properties"]) -> None: ...

global___NamedDevice = NamedDevice
