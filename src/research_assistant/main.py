from research_assistant.agents.planner import create_research_plan

def main() -> None:
    question = "How are AI Agents changing software engineering?"

    plan = create_research_plan(question)

    print(f"\nResearch Question: {plan.question}\n")
    print("\nResearch Tasks:")

    for index, task in enumerate(plan.tasks, start=1):
        print(f"{index}. {task}")

if __name__ == "__main__":
    main()