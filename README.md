# stable_baselines3_ext

This repository is extensions of [Stable Baselines3](https://github.com/DLR-RM/stable-baselines3) which currently including algorithms:

- [AMP](https://github.com/nv-tlabs/ASE)
- SAC+TD3



## Installation

This codebase supports `IsaacLab`. Firstly, you should install anaconda virtual environment. Then, you could install `IsaacSim`, `IsaacLab`, and related packages.

<details>
<summary>IsaacSim</summary>

1. Install [IsaacSim](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_python.html)

</details>

<details>
<summary>IsaacLab</summary>

1. Install [IsaacLab](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html)

</details>

<details>
<summary>PoseLib</summary>

**STEP 0:**

```
git clone https://github.com/Evan-wyl/poselib
```

**STEP 1:**

```
cd poselib/
pip install -e .
```

</details>

<details>
<summary>IsaacUtils</summary>

**STEP 0:**

```
git clone https://github.com/Evan-wyl/isaac_utils
```

**STEP 1:**

```
cd isaac_utils/
pip install -e .
```

</details>



## References and Thanks

This project repository builds upon the shoulders of giants.

- [ProtoMotions](https://github.com/NVlabs/ProtoMotions) for reference AMP code. 
