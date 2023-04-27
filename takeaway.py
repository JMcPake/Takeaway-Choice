import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

takeaway_options = ["Kebab", "Pizza", "Sushi", "Curry", "Chinese"]
colors = ['#E71D36', '#FF9F1C', '#2EC4B6', '#0077B6', '#F8D210']

plt.rcParams.update({'font.family': 'Comic Sans MS', 'font.size': 20})
fig, ax = plt.subplots(figsize=(8,6))

def update(num):
    ax.clear()
    ax.set_facecolor('#F6D167')
    ax.set_xlabel('Takeaway Options', fontsize=24, fontweight='bold', color='white')
    ax.set_ylabel('Probability', fontsize=24, fontweight='bold', color='white')
    ax.set_title('FAST FOOD TAKEAWAY', fontsize=32, fontweight='bold', color='black', pad=20)
    ax.tick_params(axis='x', labelsize=18, colors='white')
    ax.tick_params(axis='y', labelsize=18, colors='white')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    pattern = np.array([[0, 1], [1, 0]])
    ax.imshow(pattern, cmap='gray', extent=[-0.5, 4.5, -0.5, 1.5], alpha=0.2, aspect='auto')

    probabilities = np.random.exponential(scale=1.0, size=len(takeaway_options))
    prob_sum = sum(probabilities)
    probabilities = [prob/prob_sum for prob in probabilities]

    ax.bar(takeaway_options, probabilities, color=colors, edgecolor='black', linewidth=1.5)

    if num == 10:
        chosen_takeaway = random.choices(takeaway_options, probabilities)[0]
        ax.text(takeaway_options.index(chosen_takeaway), probabilities[takeaway_options.index(chosen_takeaway)], ":)", ha="center", va="bottom", fontsize=50, fontweight='bold', color='white')

        # Add colored box with statistical information
        ax.text(1.05, 0.8, f"Experiment Metrics:\n\nTotal Probability: {prob_sum:.2f}\nMax Probability: {max(probabilities):.2f}\nMin Probability: {min(probabilities):.2f}\nVariance: {np.var(probabilities):.2f}\nChosen Takeaway: {chosen_takeaway}", fontsize=14, fontweight='bold', color='white', bbox=dict(facecolor='#222222', edgecolor='#222222', boxstyle='round'))

ani = animation.FuncAnimation(fig, update, frames=range(11), interval=50, repeat=False)

plt.show()
