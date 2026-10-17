from typing import Any

from pydantic import BaseModel, ConfigDict, Field


# ============================================================
# PAGE
# ============================================================

class Page(BaseModel):
    model_config = ConfigDict(extra="allow")


# ============================================================
# THEME
# ============================================================

class Theme(BaseModel):
    model_config = ConfigDict(extra="allow")


# ============================================================
# TYPOGRAPHY
# ============================================================

class Typography(BaseModel):
    model_config = ConfigDict(extra="allow")


# ============================================================
# LAYOUT
# ============================================================

class Layout(BaseModel):
    model_config = ConfigDict(extra="allow")


# ============================================================
# COMPONENT
# ============================================================

class Component(BaseModel):

    type: str

    data: dict[str, Any] = Field(default_factory=dict)


# ============================================================
# SLIDE
# ============================================================

class Slide(BaseModel):

    model_config = ConfigDict(extra="allow")

    id: str

    title: str

    purpose: str = ""

    component: str

    components: list[Component] = Field(default_factory=list)


# ============================================================
# METADATA
# ============================================================

class Metadata(BaseModel):

    document_type: str

    title: str

    audience: str

    objective: str


# ============================================================
# DDOM
# ============================================================

class DDOM(BaseModel):

    metadata: Metadata

    page: Page

    theme: Theme

    typography: Typography

    layout: Layout

    slides: list[Slide] = Field(default_factory=list)