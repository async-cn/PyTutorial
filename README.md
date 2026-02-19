# PyTutorial

![](https://img.shields.io/badge/License-MIT-blue)
![](https://img.shields.io/badge/Python-3.x-blue)

很久之前，Python 为我打开了一扇大门，将我带往丰富多彩的编程世界。

作为一名普普通通的高中Coder，我决定编写这套教程，希望能帮助更多的人们轻松地入门 Python。

## 项目初始化

推荐使用 [PyCharm](https://www.jetbrains.com/zh-cn/pycharm/) 进行 Python 学习（非广告）

1. 下载并安装 Git：前往[git-scm.com](https://git-scm.com/install/)安装 Git，或直接[点击此处](https://github.com/git-for-windows/git/releases/download/v2.53.0.windows.1/Git-2.53.0-64-bit.exe)下载为 64 位 Windows 系统准备的 Git 2.53.0。
2. 克隆项目：选择一个喜欢的目录（桌面，D盘等），[打开终端](https://blog.csdn.net/wxiao_xiao_miao/article/details/120228056)，执行命令：
```bash
git clone https://github.com/async-cn/PyTutorial.git
```
3. 下载并安装Python：前往[python.org](https://www.python.org/)下载任意版本不低于3的Python（推荐使用[Python 3.14.3](https://www.python.org/downloads/release/python-3143/) | [直接为Windows 64bit 下载](https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe)）
4. 安装项目依赖：在项目目录（PyTutorial）下打开终端并执行命令：
```bash
pip install -r requirements.txt
pip install packages/pyjudge-0.1.0-py3-none-any.whl
```

## 开始使用

### 非 PyCharm 用户 

5. 启动笔记本：在项目目录（PyTutorial）下打开终端并执行命令：（Windows用户直接执行notebook.cmd即可）
```bash
jupyter notebook --port 9100
```
6. 访问笔记本：在浏览器中访问[localhost:9100](http://localhost:9100)即可（初次使用请查看[README.ipynb](http://localhost:9100/notebooks/README.ipynb)）

### PyCharm 用户

PyCharm 内置Jupyter Notebook托管和渲染，直接在PyCharm内查看即可。