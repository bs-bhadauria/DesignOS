from app.knowledge.manager import KnowledgeManager


def main():

    manager = KnowledgeManager()

    print("=" * 60)
    print("Available Knowledge")
    print("=" * 60)

    for item in manager.list():
        print(item)

    print()

    print("=" * 60)
    print("Identity")
    print("=" * 60)

    identity = manager.get("identity")

    print(identity.content[:500])

    print()

    print("=" * 60)
    print("Design Principles")
    print("=" * 60)

    principles = manager.get("design_principles")

    print(principles.content[:500])

    print()

    print("=" * 60)
    print("Design Language")
    print("=" * 60)

    language = manager.get("design_language")

    print(language.content[:500])

    print()

    print("=" * 60)
    print("Information Architecture")
    print("=" * 60)

    architecture = manager.get("information_architecture")

    print(architecture.content[:500])


if __name__ == "__main__":
    main()