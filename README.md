### 这是一个简单 Docker demo

W：**将tornado应用运行在Docker中**

**环境**： ubuntu16.04   python2.7
使用daocloud的python镜像(ths daocloud~),  该镜像提供一个python环境，就不用再安装了

运行该项目请按照如下流程:
1. 克隆项目到本地
2. `cd docker_tornado_demo`
3. `docker build -t tornado_demo . `
4. `docker run --name tornado_service -b -p8000:8000 tornado_demo `
5. 到浏览器访问 *localhost:8000* , 返回hello world就表示成功了~ 

查看docker容器运行状态： `docker ps ` ,如需查看所有的容器(包括停止的) + '-a' 参数，`docker ps -a`

停止该容器： `docker stop tornado_service`

停止后重启可直接输入： `docker start tornado_service`
