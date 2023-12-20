# PowerSynth 2 Release Series Core Repository
## Repository Overview
This is the gui repository for PowerSynth 2. Refer to the [PowerSynth2-core](https://github.com/e3da/PowerSynth2-core) and other related repos for the CLI and other parts. 
This repository contains the main source code for the QT-based PowerSynth 2 the GUI. 

The UI is designed with QT designer. Currently, Qt 5.15 and PySide2 are used for the release.
Note that the GUI is not tested extensively as the CLI. Minor rendering issues exists, especially on Windows. Also, several modules are ported from earilier versions. Therefore, it is provided for users' convienience and preview. Regular users and researchers are suggested to use CLI for more stable and smoother work flow. 

# PowerSynth 2 Project Overview
PowerSynth 2 started as a research project to introduce the VLSI electronics design automation algorithms for power electronic applications. It is developed originally by the [E3DA Lab](https://e3da.csce.uark.edu/) as a POETS project and then jointly by [MSCAD Lab](https://mscad.uark.edu/), at University of Arkansas. 

PowerSynth 2 was first developed as an enhanced layout engine for PowerSynth 1 to handle design constraints in complicated layouts with efficiency improvements. The new layout engine is first previewed in PowerSynth v1.3, and then became the sole engine in v1.9. In addition, new 3D layout algorithms, electrical/thermal models are introduced in v2.0, with improved optimization algorithms introduced in v2.1.

The PowerSynth 2 project is co-directed by [Prof. Yarui Peng](https://engineering.uark.edu/directory/index/uid/yrpeng/name/Yarui+Peng/) and [Prof. Alan Mantooth](https://engineering.uark.edu/directory/index/uid/mantooth/name/Alan+Mantooth/). The research project is mainly supported by NSF through POETS ERC, ARL, and ARPA-E through a series of grants. 

The main developers of this release series include Imam Al Razi, Quang Le, Mehran Sanjabiasasi, and Tristan Evans. The initial GUI is mainly developed by Joshua Mitchener as an REU project. The codebase also received contributions from many collaborators, graduates, and undergrads.

The main features, algorithms, and experiments of PowerSynth 2 are summarized in the following papers:

* v2.0: Imam Al Razi, Quang Le, Tristan Evans, H. Alan Mantooth, and Yarui Peng, ["PowerSynth 2: Physical Design Automation for High-Density 3D Multi-Chip Power Modules"](https://doi.org/10.1109/TPEL.2022.3227300), IEEE Transactions on Power Electronics, vol. 38, no. 4, pp. 4698-4713, April 2023.
* v2.1: Mehran Sanjabiasasi, Imam Al Razi, H. Alan Mantooth, and Yarui Peng, ["A Comparative Study on Optimization Algorithms in PowerSynth 2"](https://e3da.csce.uark.edu/pub/doc/2023/M.Sanjabiasasi-Misc.Conf.DMC-2023.pdf), in Proc. IEEE Design Methodologies Conference, Sep 2023.

We welcome contributions and collaborations from the community by providing patches and reporting issues. If you find our research projects helpful, please attribute this work in your publications and presentations as appropriate.
