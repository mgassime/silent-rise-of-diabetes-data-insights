"""
Generate all diabetes insight figures used in the README.

Run:
    python make_all_figures.py

This will save PNG files in the ./figures directory.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

FIG_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG_DIR, exist_ok=True)


def fig1_global_prevalence():
    years = [1990, 2022]
    people_millions = [200, 830]

    fig, ax = plt.subplots()
    ax.plot(years, people_millions, marker="o")
    ax.set_xlabel("Year")
    ax.set_ylabel("People with diabetes (millions)")
    ax.set_title("Global Diabetes: Adults with Diabetes (1990 vs 2022)")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig1_global_prevalence.png"))
    plt.close(fig)


def fig2_region_burden():
    regions = [
        "Global", "Europe", "MENA",
        "SE Asia", "W. Pacific", "Africa"
    ]

    adults_millions = [589, 66, 85, 107, 215, 25]

    x = np.arange(len(regions))
    fig, ax = plt.subplots()
    ax.bar(x, adults_millions)
    ax.set_xticks(x)
    ax.set_xticklabels(regions, rotation=45, ha="right")
    ax.set_ylabel("Adults with diabetes (millions)")
    ax.set_title("Adults with Diabetes by Region (2024)")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig2_region_burden.png"))
    plt.close(fig)


def fig3_projection():
    years = [2024, 2050]
    adults_millions = [589, 853]

    fig, ax = plt.subplots()
    ax.bar([str(y) for y in years], adults_millions)
    ax.set_xlabel("Year")
    ax.set_ylabel("Adults with diabetes (millions)")
    ax.set_title("Projected Global Adults with Diabetes (2024 vs 2050)")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig3_projection.png"))
    plt.close(fig)


def fig4_undiagnosed():
    categories = ["Global", "Africa", "Europe"]
    proportion_percent = [43, 73, 25]

    x = np.arange(len(categories))
    fig, ax = plt.subplots()
    ax.bar(x, proportion_percent)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylabel("Undiagnosed proportion (%)")
    ax.set_title("Share of Diabetes Cases that are Undiagnosed")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig4_undiagnosed.png"))
    plt.close(fig)


def fig5_treatment_coverage():
    labels = ["On treatment", "Not on treatment"]
    values_percent = [50, 50]

    fig, ax = plt.subplots()
    ax.pie(values_percent, labels=labels, autopct="%1.0f%%")
    ax.set_title("Global Diabetes Treatment Coverage (Approximate)")
    fig.savefig(os.path.join(FIG_DIR, "fig5_treatment_coverage.png"))
    plt.close(fig)


def fig6_income_groups():
    groups = ["Low", "Lower-middle", "Upper-middle", "High"]
    prevalence_percent = [5.5, 9.1, 11.1, 11.1]
    adults_millions = [20.9, 211.2, 279.2, 73.7]

    x = np.arange(len(groups))
    width = 0.35

    fig, ax1 = plt.subplots()
    ax1.bar(x - width/2, prevalence_percent, width, label="Prevalence (%)")
    ax1.set_ylabel("Prevalence (%)")
    ax1.set_xticks(x)
    ax1.set_xticklabels(groups, rotation=45, ha="right")

    ax2 = ax1.twinx()
    ax2.bar(x + width/2, adults_millions, width, label="Adults (millions)")
    ax2.set_ylabel("Adults with diabetes (millions)")

    fig.suptitle("Diabetes by Income Group (2021)")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig6_income_groups.png"))
    plt.close(fig)


def fig7_regions_prevalence():
    regions = [
        "MENA", "N. America & Caribbean", "Europe",
        "S. & Central America", "SE Asia",
        "W. Pacific", "Africa"
    ]

    prevalence_percent = [17.6, 13.0, 9.8, 9.5, 11.0, 11.0, 5.0]

    x = np.arange(len(regions))
    fig, ax = plt.subplots()
    ax.bar(x, prevalence_percent)
    ax.set_xticks(x)
    ax.set_xticklabels(regions, rotation=45, ha="right")
    ax.set_ylabel("Prevalence (% of adults)")
    ax.set_title("Diabetes Prevalence by Region")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig7_regions_prevalence.png"))
    plt.close(fig)


def fig8_mortality():
    categories = [
        "Deaths attributable to diabetes (2024)",
        "Direct diabetes deaths (2021)",
        "Deaths incl. kidney disease (2021)"
    ]
    deaths_millions = [3.4, 1.6, 2.0]

    x = np.arange(len(categories))
    fig, ax = plt.subplots()
    ax.bar(x, deaths_millions)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45, ha="right")
    ax.set_ylabel("Deaths (millions)")
    ax.set_title("Diabetes-Related Mortality (Approximate)")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig8_mortality.png"))
    plt.close(fig)


def fig9_economic():
    categories = ["Global (2024)", "Africa", "US"]
    values_billion_usd = [1015, 10, 400]

    x = np.arange(len(categories))
    fig, ax = plt.subplots()
    ax.bar(x, values_billion_usd)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45, ha="right")
    ax.set_ylabel("Spending (billion USD)")
    ax.set_title("Economic Impact of Diabetes")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig9_economic.png"))
    plt.close(fig)


def fig10_hip():
    categories = [
        "Hyperglycemia in pregnancy",
        "Gestational diabetes only"
    ]
    prevalence_percent = [20, 17]

    x = np.arange(len(categories))
    fig, ax = plt.subplots()
    ax.bar(x, prevalence_percent)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45, ha="right")
    ax.set_ylabel("Prevalence (% of pregnancies)")
    ax.set_title("Hyperglycemia and Gestational Diabetes in Pregnancy")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, "fig10_hip.png"))
    plt.close(fig)


def main():
    fig1_global_prevalence()
    fig2_region_burden()
    fig3_projection()
    fig4_undiagnosed()
    fig5_treatment_coverage()
    fig6_income_groups()
    fig7_regions_prevalence()
    fig8_mortality()
    fig9_economic()
    fig10_hip()
    print(f"Figures saved to: {FIG_DIR}")


if __name__ == "__main__":
    main()
