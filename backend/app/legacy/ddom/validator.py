from app.ddom.models import DDOM


class DDOMValidator:
    """
    Validates a DDOM before it reaches the Renderer.

    This validator guarantees that the internal document
    satisfies the minimum architectural requirements.

    It NEVER modifies the DDOM.
    It ONLY validates it.
    """

    @staticmethod
    def validate(ddom: DDOM) -> None:
        """
        Validate the DDOM.

        Raises
        ------
        ValueError
            If any required part of the DDOM is missing.
        """

        if not ddom.metadata.title:
            raise ValueError("Document title is missing.")

        if not ddom.metadata.document_type:
            raise ValueError("Document type is missing.")

        if len(ddom.slides) == 0:
            raise ValueError("DDOM contains no slides.")

        for slide in ddom.slides:

            if not slide.title:
                raise ValueError("Slide title is missing.")

            if not slide.component:
                raise ValueError(
                    f"Slide '{slide.id}' has no component."
                )

            if len(slide.components) == 0:
                raise ValueError(
                    f"Slide '{slide.id}' contains no components."
                )

            for component in slide.components:

                if not component.type:
                    raise ValueError(
                        f"Component in '{slide.id}' has no type."
                    )

        return