import os

# mysql 版本
mysql_version = "latest"

# 当前所有的镜像
mysql_images = {}


# docker image 类
class DockerImage:

    def __init__(self, repository, tag, image_id, created, size):
        self.repository = repository
        self.tag = tag
        self.image_id = image_id
        self.created = created
        self.size = size

    def __str__(self):
        strs = 'repository：%s  tag：%s  image_id:%s  created:%s  size:%s'(self.repository, self.tag, self.image_id,
                                                                         self.created, self.size)
        return strs


# 检查系统是否已经安装了docker
def check_docker():
    check_docker_command = "docker --version"
    check_docker_result_f = os.popen(check_docker_command, "r")
    check_docker_result = check_docker_result_f.read()
    print(check_docker_result)
    if len(check_docker_result.strip()) == 0:
        return 0
    else:
        return 1


# 选择拉取mysql镜像版本
def pull_mysql_version():
    temp_mysql_version = "latest"
    print("开始拉取mysql镜像")
    temp_mysql_version_flag = input("默认将拉取最新版本 mysql镜像，是否指定镜像版本 y/n：")
    if temp_mysql_version_flag == "Y" or temp_mysql_version_flag == "y":
        temp_mysql_version = input("请输入需要选择的版本：")
    elif temp_mysql_version_flag == "N" or temp_mysql_version_flag == "n":
        print("您将选择默认的最新版本进行安装")
    else:
        print("输入错误")
        exit()
    return temp_mysql_version


# 拉取mysql
def pull_mysql(temp_mysql_version):
    pull_mysql_command = "docker pull mysql"

    print("开始拉取mysql")

    pull_mysql_command = pull_mysql_command + ":" + temp_mysql_version
    os.system(pull_mysql_command)


def analysis_images(all_mysql_images_str_list):
    for mysql_images_str in all_mysql_images_str_list:
        if len(mysql_images_str.strip()) != 0:
            mysql_images_info = list(filter(None, mysql_images_str.split("  ")))
            image = DockerImage(mysql_images_info[0], mysql_images_info[1], mysql_images_info[2],
                                mysql_images_info[3], mysql_images_info[4])
            mysql_images[mysql_images_info[1].strip()] = image
    print(mysql_images)


# 初始化镜像字典
def init_mysql():
    mysql_images_command = "docker images mysql"
    mysql_images_result_f = os.popen(mysql_images_command, "r")
    mysql_images_result = mysql_images_result_f.read()
    all_mysql_images_str_list = mysql_images_result.split("\n")
    all_mysql_images_str_list.pop(0)
    analysis_images(all_mysql_images_str_list)


# 查询镜像是否存在
def check_mysql(temp_mysql_version, temp_mysql_images):
    image = temp_mysql_images.get(temp_mysql_version)
    if image is not None:
        return 1
    else:
        return 0


# 安装启动
def run_mysql():
    base_mysql_path = "~/local/mysql/"
    log_path = base_mysql_path + "logs"
    config_path = base_mysql_path + "conf"
    data_path = base_mysql_path + "data"

    run_mysql_command = "docker run --name mysql -p 3306:3306 -v " \
                        + data_path + ":/var/lib/mysql -v " \
                        + config_path + ":/etc/mysql/conf.d -v " \
                        + log_path + ":/var/log/mysql  -e MYSQL_ROOT_PASSWORD=123456 -d mysql:" \
                        + mysql_version
    if not os.path.exists(base_mysql_path):
        os.makedirs(base_mysql_path)
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    if not os.path.exists(config_path):
        os.makedirs(config_path)
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    os.system(run_mysql_command)


# 判断docker是否安装
if check_docker() == 1:
    print("已经安装docker，程序继续执行")
else:
    print("当前系统还未安装docker")
    exit()
print(mysql_images)
# 初始化一次mysql镜像列表
init_mysql()
# 选择mysql版本
mysql_version = pull_mysql_version()
if check_mysql(mysql_version, mysql_images) == 1:
    print("镜像已经存在，不再进行拉取")
else:
    print("开始拉取镜像 mysql:" + mysql_version)
    pull_mysql(mysql_version)
init_mysql()

run_mysql()
