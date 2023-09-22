
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


sns.set_theme(style="whitegrid")

# PromptNER https://arxiv.org/pdf/2305.15444.pdf
GPT3_5 = [
    00.00,  # Movie
    00.00,  # Restaurant
    20.30,  # Politics
    31.30,  # Literature
    24.50,  # Music
    40.70,  # AI
    40.60,  # Science
]

# Instruct UIE https://arxiv.org/pdf/2304.08085.pdf
InstructUIE = [
    63.00,  # Movie
    20.99,  # Restaurant
    49.00,  # Politics
    47.21,  # Literature
    53.16,  # Music
    48.15,  # AI
    49.30,  # Science
]

CoLLIE = [
    63.30,  # Movie
    41.52,  # Restaurant
    56.44,  # Politics
    61.00,  # Literature
    67.65,  # Music
    58.47,  # AI
    54.66,  # Science
]


def main():
    fig, ax = plt.subplots(1, 7, figsize=(12, 4), sharey=True, layout="constrained")

    TASK_NAMES = ["Movie", "Restaurant", "Politics", "Literature", "Music", "AI", "Music"]

    for i, (gpt, iuie, collie, name) in enumerate(zip(GPT3_5, InstructUIE, CoLLIE, TASK_NAMES)):
        rect = ax[i].bar(
            [1],
            [np.round(gpt)],
            width=1.0,
            label="GPT-3",
            # color="#a40e26",
            color=sns.color_palette("crest", 3)[0],
            hatch="//",
        )
        if gpt:
            ax[i].bar_label(rect, padding=3, fontsize=12)

        rect = ax[i].bar(
            [2],
            [np.round(iuie)],
            width=1.0,
            label="Instruct-UIE",
            # color="#6639ba",
            color=sns.color_palette("crest", 3)[1],
            hatch="/",
        )
        ax[i].bar_label(rect, padding=3, fontsize=12)

        rect = ax[i].bar(
            [3],
            [np.round(collie)],
            width=1.0,
            label="CoLLIE",
            # color="#0a3069"
            color=sns.color_palette("crest", 3)[2],
        )
        ax[i].bar_label(rect, padding=3, fontsize=12)

        ax[i].set_xticks([1, 2, 3])
        ax[i].set_yticklabels([])
        ax[i].set_xticklabels(["", name, ""], fontsize=14)
        # ax[i].set_title(name)
        ax[i].grid(False)
        ax[i].spines["top"].set_visible(False)
        ax[i].spines["right"].set_visible(False)
        ax[i].spines["bottom"].set_visible(False)
        ax[i].spines["left"].set_visible(False)

    fig.legend(["GPT-3.5", "Instruct-UIE", "GoLLIE"], loc="outside upper center", ncol=3, fontsize=14, frameon=False)
    # ax[3].legend(["GPT-3", "Instruct-UIE", "CoLLIE"], fontsize=12, ncol=3, bbox_to_anchor=(1.00, 1.15), loc="lower center")

    # plt.tight_layout()
    plt.savefig("assets/plots/zero_shot_results.pdf", dpi=300)


if __name__ == "__main__":
    main()
