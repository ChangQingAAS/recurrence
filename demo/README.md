# 代码简介



4 agents（红色）： 结伴飞行

trainer: 基于A-C网络的ddpg算法

4障碍物（蓝色）： 分布在不同区域、静态

任务描述：agents从起点飞到目的点，不碰撞障碍物

设计方式：agents的奖惩函数，

```
主线reward： 有多么靠近目的点；
```


```
辅助reward:有多么远离障碍物
```


改进方向：有点多，略