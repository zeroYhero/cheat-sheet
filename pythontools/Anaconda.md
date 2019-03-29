管理python包环境很烦人，用这个软件能省事不少。

常用命令行命令：
```python
conda create -n learn python=3
```
创建一个名为learn并以python3+解释器为基础。
```python
activate
```
切换到base环境
```python
activate learn
```
切换到learn环境
```python
conda create -n learn python=3
```
创建一个名为learn的环境并指定python版本为3(的最新版本)
```python
conda env list
```
列出conda管理的所有环境
```python
conda list
```
列出当前环境的所有包
```
conda install requests
```
安装requests包
```
conda remove requests
```
卸载requets包
```
conda remove -n learn --all
```
删除learn环境及下属所有包
```
conda update requests
```
更新requests包
```
conda env export > environment.yaml
```
导出当前环境的包信息
```
conda env create -f environment.yaml
```
用配置文件创建新的虚拟环境
