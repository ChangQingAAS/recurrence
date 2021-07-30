# File name : agent_uav_anti_tank.py

from mozi_ai_sdk.agents import base_agent
from mozi_ai_sdk.rlmodel.ddpg import train
from mozi_ai_sdk.rlmodel.ddpg import buffer
import etc
import numpy as np


class Agent(base_agent.BaseAgent):
    def __init__(self, env, start_epoch=0):
        super(Agent, self).__init__()

        S_DIM = env.state_space
        A_DIM = env.action_space
        A_MAX = env.action_max

        #start_episode = 0
        self.episodes = start_epoch

        ram = buffer.MemoryBuffer(etc.MAX_BUFFER)
        trainer = train.Trainer(S_DIM, A_DIM, A_MAX, ram, etc.device, None,
                                int(start_epoch), etc.MODELS_PATH)

        self.trainer = trainer
        self.ram = ram
        self.env = env
        self.train_step = 0

    def reset(self):
        '''
        重置
        '''
        self.trainer.save_model(self.episodes, etc.MODELS_PATH)
        self.episodes += 1

    def setup(self, state_space, action_space):
        '''
        设置
        '''
        self.state_space = state_space
        self.action_space = action_space

    def step(self, observation):
        '''
        step函数
        '''
        super(Agent, self).step(observation)
        state = np.float32(observation)

        if self.episodes % 5 == 0:
            action = self.trainer.get_exploitation_action(state)
        else:
            action = self.trainer.get_exploration_action(state)

        new_observation, reward, done, info = self.env.step(action)

        if done:
            new_state = None
        else:
            new_state = np.float32(new_observation)
            self.ram.add(state, action, reward, new_state)

        observation = new_observation
        self.trainer.optimize(self.train_step)
        self.train_step += 1

        return observation, reward, done, info
