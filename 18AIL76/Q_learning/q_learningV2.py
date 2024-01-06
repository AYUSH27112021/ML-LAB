import numpy as np

# Define the environment (3x3 grid world)
grid_world = [
    ['S', '-', 'x'],
    ['-', 'x', '-'],
    ['x', '-', 'G']
]

# Define actions
actions = ['up', 'down', 'left', 'right']
num_actions = len(actions)

# Define rewards
rewards = {
    'G': 100,
    '-': -1,
    'x': -10,
    'S': 0
}

# Initialize Q-table
Q = np.zeros((9, num_actions))

# Define parameters
alpha = 0.5  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.3  # Epsilon for epsilon-greedy policy
num_episodes = 1000  # Number of episodes
max_steps_per_episode = 100  # Maximum steps per episode

# Function to get the next state after taking an action
def get_next_state(state_index, action_index):
    row = state_index // 3
    col = state_index % 3

    if actions[action_index] == 'up':
        row = max(0, row - 1)
    elif actions[action_index] == 'down':
        row = min(2, row + 1)
    elif actions[action_index] == 'left':
        col = max(0, col - 1)
    else:
        col = min(2, col + 1)

    return row, col

# Q-learning algorithm
for episode in range(num_episodes):
    state_index = 0  # Start at state 'S'
    total_reward = 0

    for step in range(max_steps_per_episode):
        # Epsilon-greedy policy for action selection
        if np.random.uniform(0, 1) < epsilon:
            action_index = np.random.randint(num_actions)  # Explore
        else:
            action_index = np.argmax(Q[state_index, :])  # Exploit

        # Simulate environment (transition to next state)
        next_row, next_col = get_next_state(state_index, action_index)
        next_state = grid_world[next_row][next_col]
        next_state_index = next_row * 3 + next_col
        reward = rewards[next_state]

        # Q-table update
        Q[state_index, action_index] += alpha * (
            reward + gamma * np.max(Q[next_state_index, :]) - Q[state_index, action_index])

        total_reward += reward
        state_index = next_state_index

        if grid_world[next_row][next_col] == 'G':
            break  # Goal reached, terminate the episode

    if (episode + 1) % 100 == 0:
        print(f"Episode {episode + 1}/{num_episodes}, Total Reward: {total_reward}")

# Trained Q-table
print("\nTrained Q-table:")
print(Q)

# Testing the trained agent
current_state_index = 0  # Start at state 'S'

print("\nAgent path:")
while grid_world[current_state_index // 3][current_state_index % 3] != 'G':
    action_index = np.argmax(Q[current_state_index, :])
    print(f"Current State: {grid_world[current_state_index // 3][current_state_index % 3]}")
    print(f"Action Taken: {actions[action_index]}")
    
    next_row, next_col = get_next_state(current_state_index, action_index)
    current_state_index = next_row * 3 + next_col

    print("---------")

print(f"Reached Goal: {grid_world[current_state_index // 3][current_state_index % 3]}")