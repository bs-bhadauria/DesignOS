from app.ddom.models import (
    Component,
    DDOM,
    Metadata,
    Page,
    Slide,
    Theme,
    Typography,
)


class DDOMBuilder:
    """
    Builds the internal DesignOS Document Object Model (DDOM)
    from Planner and Designer outputs.
    """

    @staticmethod
    def build(plan: dict, design: dict) -> DDOM:

        metadata = Metadata(
            document_type=plan["document_type"],
            title=plan["title"],
            audience=plan["audience"],
            objective=plan["objective"],
        )

        page = Page(**design["page"])

        theme = Theme(
            primary_color=design["theme"]["primary_color"],
            secondary_color=design["theme"]["secondary_color"],
            background_color=design["theme"].get(
                "background_color",
                design["theme"].get("background", "#ffffff"),
            ),
            text_color=design["theme"].get(
                "text_color",
                "#111111",
            ),
        )

        typography = Typography(
            heading_font=design["typography"]["heading_font"],
            body_font=design["typography"]["body_font"],
            heading_size=design["typography"]["heading_size"],
            body_size=design["typography"]["body_size"],
        )

        slides = []

        planner_sections = plan["sections"]
        designer_sections = design["sections"]

        for index, (plan_section, design_section) in enumerate(
            zip(planner_sections, designer_sections),
            start=1,
        ):

            component_data = {
                **design_section,
                "purpose": plan_section["purpose"],
            }

            slide = Slide(
                id=f"slide_{index}",
                title=plan_section["title"],
                purpose=plan_section["purpose"],
                component=design_section["component"],
                components=[
                    Component(
                        type=design_section["component"],
                        data=component_data,
                    )
                ],
            )

            slides.append(slide)

        from app.ddom.models import Layout
        layout = Layout(**design.get("layout", {}))

        return DDOM(
            metadata=metadata,
            page=page,
            theme=theme,
            typography=typography,
            layout=layout,
            slides=slides,
        )