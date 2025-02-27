# SoccerNet Jersey Number Recognition Challenge  

This repository contains the code and resources used to tackle the **SoccerNet Jersey Number Recognition Challenge**. The challenge involves recognizing athletes' jersey numbers from tracklets (frames sampled from a video) taken from football matches and provided by [SoccerNet](https://github.com/SoccerNet/sn-jersey), focusing on accurate detection and recognition of jersey numbers under various conditions like motion blur, occlusion, varying poses, and illegible text.

---

## Team members

- [Zhenbang He](https://github.com/m-iDev-0792)
- [Laura Quiroga](https://github.com/Lauraquiroga)
- [Syed Aamir Ahmed](https://github.com/aamirahmed2004)
- [Qianyu (Grace) Shang](https://github.com/GorgeousGrace)
- [Pratheek Balani](https://github.com/prateek-balani)

---

## 📁 Repository Structure  

- `/docs`: contains documentation for project development, including a progress report, and a list of useful references.
- `/replicating_results`: contains our attempts to replicate SOTA results. Also contains our teammate Zhenbang's [repository](https://github.com/m-iDev-0792/jersey-number-pipeline) as a submodule. His repository is forked from the [original general framework repo](https://github.com/mkoshkina/jersey-number-pipeline), and he fixed a lot of compatibility issues and wrote scripts to simplify the process of replicating the results.
- `/tests`: will contain all our experiments, either as Python files, or in the form of submodules in case we need to clone other repos to conduct our experiments.

### Note about Github submodules

They are essentially like a link to the original repo, frozen at the latest commit at the time of adding as a submodule. To add a submodule, use this command:

`git submodule add <repo_link> <path_to_where_it_goes>`

To update a submodule to a newer commit, use this command:

`git submodule update --remote`

**Reasoning for using submodules:** to keep the directory structure clean, and to allow us to experiment with different approaches that may require cloning other repos or may not be related to the final pipeline, without dependency issues.
