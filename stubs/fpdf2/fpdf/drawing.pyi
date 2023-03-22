import decimal
from _typeshed import Incomplete
from collections import OrderedDict
from collections.abc import Callable, Generator, Iterator
from contextlib import contextmanager
from re import Pattern
from typing import Any, ClassVar, NamedTuple, TypeVar
from typing_extensions import Self, TypeAlias

from .syntax import Name, Raw

__pdoc__: dict[str, bool]

_CallableT = TypeVar("_CallableT", bound=Callable[..., Any])

def force_nodocument(item: _CallableT) -> _CallableT: ...
def force_document(item: _CallableT) -> _CallableT: ...

Number: TypeAlias = int | float | decimal.Decimal
NumberClass: tuple[type, ...]
WHITESPACE: frozenset[str]
EOL_CHARS: frozenset[str]
DELIMITERS: frozenset[str]
STR_ESC: Pattern[str]
STR_ESC_MAP: dict[str, str]

class GraphicsStateDictRegistry(OrderedDict[Raw, Name]):
    def register_style(self, style: GraphicsStyle) -> Name | None: ...

def number_to_str(number) -> str: ...
def render_pdf_primitive(primitive) -> Raw: ...

class _DeviceRGBBase(NamedTuple):
    r: Number
    g: Number
    b: Number
    a: Number | None

class DeviceRGB(_DeviceRGBBase):
    OPERATOR: ClassVar[str]
    def __new__(cls, r: Number, g: Number, b: Number, a: Number | None = ...) -> Self: ...
    @property
    def colors(self) -> tuple[Number, Number, Number]: ...
    def serialize(self) -> str: ...

class _DeviceGrayBase(NamedTuple):
    g: Number
    a: Number | None

class DeviceGray(_DeviceGrayBase):
    OPERATOR: ClassVar[str]
    def __new__(cls, g: Number, a: Number | None = ...) -> Self: ...
    @property
    def colors(self) -> tuple[Number]: ...
    def serialize(self) -> str: ...

class _DeviceCMYKBase(NamedTuple):
    c: Number
    m: Number
    y: Number
    k: Number
    a: Number | None

class DeviceCMYK(_DeviceCMYKBase):
    OPERATOR: ClassVar[str]
    def __new__(cls, c: Number, m: Number, y: Number, k: Number, a: Number | None = ...) -> Self: ...
    @property
    def colors(self) -> tuple[Number, Number, Number, Number]: ...
    def serialize(self) -> str: ...

def rgb8(r, g, b, a: Incomplete | None = ...) -> DeviceRGB: ...
def gray8(g, a: Incomplete | None = ...) -> DeviceGray: ...
def cmyk8(c, m, y, k, a: Incomplete | None = ...) -> DeviceCMYK: ...
def color_from_hex_string(hexstr) -> DeviceRGB: ...
def color_from_rgb_string(rgbstr) -> DeviceRGB: ...

class Point(NamedTuple):
    x: Number
    y: Number
    def render(self): ...
    def dot(self, other): ...
    def angle(self, other): ...
    def mag(self): ...
    def __add__(self, other): ...
    def __sub__(self, other): ...
    def __neg__(self): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __truediv__(self, other): ...
    def __floordiv__(self, other): ...
    def __matmul__(self, other): ...

class Transform(NamedTuple):
    a: Number
    b: Number
    c: Number
    d: Number
    e: Number
    f: Number
    @classmethod
    def identity(cls): ...
    @classmethod
    def translation(cls, x, y): ...
    @classmethod
    def scaling(cls, x, y: Incomplete | None = ...): ...
    @classmethod
    def rotation(cls, theta): ...
    @classmethod
    def rotation_d(cls, theta_d): ...
    @classmethod
    def shearing(cls, x, y: Incomplete | None = ...): ...
    def translate(self, x, y): ...
    def scale(self, x, y: Incomplete | None = ...): ...
    def rotate(self, theta): ...
    def rotate_d(self, theta_d): ...
    def shear(self, x, y: Incomplete | None = ...): ...
    def about(self, x, y): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __matmul__(self, other): ...
    def render(self, last_item): ...

class GraphicsStyle:
    INHERIT: ClassVar[Incomplete]
    MERGE_PROPERTIES: ClassVar[tuple[str, ...]]
    TRANSPARENCY_KEYS: ClassVar[tuple[Name, ...]]
    PDF_STYLE_KEYS: ClassVar[tuple[Name, ...]]
    @classmethod
    def merge(cls, parent, child): ...
    def __init__(self) -> None: ...
    def __deepcopy__(self, memo) -> Self: ...
    @property
    def allow_transparency(self): ...
    @allow_transparency.setter
    def allow_transparency(self, new): ...
    @property
    def paint_rule(self): ...
    @paint_rule.setter
    def paint_rule(self, new) -> None: ...
    @property
    def auto_close(self): ...
    @auto_close.setter
    def auto_close(self, new) -> None: ...
    @property
    def intersection_rule(self): ...
    @intersection_rule.setter
    def intersection_rule(self, new) -> None: ...
    @property
    def fill_color(self): ...
    @fill_color.setter
    def fill_color(self, color) -> None: ...
    @property
    def fill_opacity(self): ...
    @fill_opacity.setter
    def fill_opacity(self, new) -> None: ...
    @property
    def stroke_color(self): ...
    @stroke_color.setter
    def stroke_color(self, color) -> None: ...
    @property
    def stroke_opacity(self): ...
    @stroke_opacity.setter
    def stroke_opacity(self, new) -> None: ...
    @property
    def blend_mode(self): ...
    @blend_mode.setter
    def blend_mode(self, value) -> None: ...
    @property
    def stroke_width(self): ...
    @stroke_width.setter
    def stroke_width(self, width) -> None: ...
    @property
    def stroke_cap_style(self): ...
    @stroke_cap_style.setter
    def stroke_cap_style(self, value) -> None: ...
    @property
    def stroke_join_style(self): ...
    @stroke_join_style.setter
    def stroke_join_style(self, value) -> None: ...
    @property
    def stroke_miter_limit(self): ...
    @stroke_miter_limit.setter
    def stroke_miter_limit(self, value) -> None: ...
    @property
    def stroke_dash_pattern(self): ...
    @stroke_dash_pattern.setter
    def stroke_dash_pattern(self, value) -> None: ...
    @property
    def stroke_dash_phase(self): ...
    @stroke_dash_phase.setter
    def stroke_dash_phase(self, value): ...
    def serialize(self) -> Raw | None: ...
    def resolve_paint_rule(self): ...

class Move(NamedTuple):
    pt: Point
    @property
    def end_point(self): ...
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class RelativeMove(NamedTuple):
    pt: Point
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class Line(NamedTuple):
    pt: Point
    @property
    def end_point(self): ...
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class RelativeLine(NamedTuple):
    pt: Point
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class HorizontalLine(NamedTuple):
    x: Number
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class RelativeHorizontalLine(NamedTuple):
    x: Number
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class VerticalLine(NamedTuple):
    y: Number
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class RelativeVerticalLine(NamedTuple):
    y: Number
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class BezierCurve(NamedTuple):
    c1: Point
    c2: Point
    end: Point
    @property
    def end_point(self): ...
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class RelativeBezierCurve(NamedTuple):
    c1: Point
    c2: Point
    end: Point
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class QuadraticBezierCurve(NamedTuple):
    ctrl: Point
    end: Point
    @property
    def end_point(self): ...
    def to_cubic_curve(self, start_point): ...
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class RelativeQuadraticBezierCurve(NamedTuple):
    ctrl: Point
    end: Point
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class Arc(NamedTuple):
    radii: Point
    rotation: Number
    large: bool
    sweep: bool
    end: Point
    @staticmethod
    def subdivde_sweep(sweep_angle) -> Generator[Incomplete, None, None]: ...
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class RelativeArc(NamedTuple):
    radii: Point
    rotation: Number
    large: bool
    sweep: bool
    end: Point
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class Rectangle(NamedTuple):
    org: Point
    size: Point
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class RoundedRectangle(NamedTuple):
    org: Point
    size: Point
    corner_radii: Point
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class Ellipse(NamedTuple):
    radii: Point
    center: Point
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class ImplicitClose(NamedTuple):
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class Close(NamedTuple):
    def render(self, gsd_registry, style, last_item, initial_point): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class DrawingContext:
    def __init__(self) -> None: ...
    def add_item(self, item, _copy: bool = ...) -> None: ...
    def render(self, gsd_registry, first_point, scale, height, starting_style): ...
    def render_debug(self, gsd_registry, first_point, scale, height, starting_style, debug_stream): ...

class PaintedPath:
    def __init__(self, x: int = ..., y: int = ...) -> None: ...
    def __deepcopy__(self, memo) -> Self: ...
    @property
    def style(self): ...
    @property
    def transform(self): ...
    @transform.setter
    def transform(self, tf) -> None: ...
    @property
    def auto_close(self): ...
    @auto_close.setter
    def auto_close(self, should) -> None: ...
    @property
    def paint_rule(self): ...
    @paint_rule.setter
    def paint_rule(self, style) -> None: ...
    @property
    def clipping_path(self): ...
    @clipping_path.setter
    def clipping_path(self, new_clipath) -> None: ...
    @contextmanager
    def transform_group(self, transform) -> Iterator[Self]: ...
    def add_path_element(self, item, _copy: bool = ...) -> None: ...
    def remove_last_path_element(self) -> None: ...
    def rectangle(self, x, y, w, h, rx: int = ..., ry: int = ...) -> Self: ...
    def circle(self, cx, cy, r) -> Self: ...
    def ellipse(self, cx, cy, rx, ry) -> Self: ...
    def move_to(self, x, y) -> Self: ...
    def move_relative(self, x, y) -> Self: ...
    def line_to(self, x, y) -> Self: ...
    def line_relative(self, dx, dy) -> Self: ...
    def horizontal_line_to(self, x) -> Self: ...
    def horizontal_line_relative(self, dx) -> Self: ...
    def vertical_line_to(self, y) -> Self: ...
    def vertical_line_relative(self, dy) -> Self: ...
    def curve_to(self, x1, y1, x2, y2, x3, y3) -> Self: ...
    def curve_relative(self, dx1, dy1, dx2, dy2, dx3, dy3) -> Self: ...
    def quadratic_curve_to(self, x1, y1, x2, y2) -> Self: ...
    def quadratic_curve_relative(self, dx1, dy1, dx2, dy2) -> Self: ...
    def arc_to(self, rx, ry, rotation, large_arc, positive_sweep, x, y) -> Self: ...
    def arc_relative(self, rx, ry, rotation, large_arc, positive_sweep, dx, dy) -> Self: ...
    def close(self) -> None: ...
    def render(
        self, gsd_registry, style, last_item, initial_point, debug_stream: Incomplete | None = ..., pfx: Incomplete | None = ...
    ): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class ClippingPath(PaintedPath):
    paint_rule: Incomplete
    def __init__(self, x: int = ..., y: int = ...) -> None: ...
    def render(
        self, gsd_registry, style, last_item, initial_point, debug_stream: Incomplete | None = ..., pfx: Incomplete | None = ...
    ): ...
    def render_debug(self, gsd_registry, style, last_item, initial_point, debug_stream, pfx): ...

class GraphicsContext:
    style: GraphicsStyle
    path_items: list[Incomplete]
    def __init__(self) -> None: ...
    def __deepcopy__(self, memo) -> Self: ...
    @property
    def transform(self) -> Transform | None: ...
    @transform.setter
    def transform(self, tf) -> None: ...
    @property
    def clipping_path(self) -> ClippingPath | None: ...
    @clipping_path.setter
    def clipping_path(self, new_clipath) -> None: ...
    def add_item(self, item, _copy: bool = ...) -> None: ...
    def remove_last_item(self) -> None: ...
    def merge(self, other_context) -> None: ...
    def build_render_list(
        self,
        gsd_registry,
        style,
        last_item,
        initial_point,
        debug_stream: Incomplete | None = ...,
        pfx: Incomplete | None = ...,
        _push_stack: bool = ...,
    ): ...
    def render(
        self,
        gsd_registry,
        style: DrawingContext,
        last_item,
        initial_point,
        debug_stream: Incomplete | None = ...,
        pfx: Incomplete | None = ...,
        _push_stack: bool = ...,
    ): ...
    def render_debug(
        self, gsd_registry, style: DrawingContext, last_item, initial_point, debug_stream, pfx, _push_stack: bool = ...
    ): ...
