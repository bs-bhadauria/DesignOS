from app.ddom.builder import DDOMBuilder
from app.ddom.validator import DDOMValidator


def main():

    planner_output = {
        "document_type": "Pitch Deck",
        "title": "AI Education Platform",
        "objective": "Secure investment",
        "audience": "Investors",
        "sections": [
            {
                "title": "Introduction",
                "purpose": "Introduce the company",
            },
            {
                "title": "Problem",
                "purpose": "Explain the market problem",
            },
            {
                "title": "Solution",
                "purpose": "Present the solution",
            },
            {
                "title": "Business Model",
                "purpose": "Explain revenue generation",
            },
        ],
    }

    designer_output = {
        "page": {
            "size": "A4",
            "orientation": "portrait",
            "margin": "normal",
        },
        "theme": {
            "primary_color": "#2563eb",
            "secondary_color": "#f8fafc",
            "background": "#ffffff",
        },
        "typography": {
            "heading_font": "Inter",
            "body_font": "Inter",
            "heading_size": 32,
            "body_size": 16,
        },
        "sections": [
            {
                "component": "hero",
            },
            {
                "component": "content_focus",
            },
            {
                "component": "feature_showcase",
            },
            {
                "component": "data_summary",
            },
        ],
    }

    ddom = DDOMBuilder.build(
        planner_output,
        designer_output,
    )

    DDOMValidator.validate(ddom)

    print("=" * 60)
    print("DDOM VALIDATION")
    print("=" * 60)

    print("SUCCESS")

    print()

    print("=" * 60)
    print("Document Metadata")
    print("=" * 60)

    print(ddom.metadata)

    print()

    print("=" * 60)
    print("Theme")
    print("=" * 60)

    print(ddom.theme)

    print()

    print("=" * 60)
    print("Typography")
    print("=" * 60)

    print(ddom.typography)

    print()

    print("=" * 60)
    print("Slides")
    print("=" * 60)

    for slide in ddom.slides:

        print()

        print(f"ID         : {slide.id}")
        print(f"Title      : {slide.title}")
        print(f"Purpose    : {slide.purpose}")
        print(f"Component  : {slide.component}")

        print("Components :")

        for component in slide.components:
            print(
                f"    - {component.type}"
            )


if __name__ == "__main__":
    main()