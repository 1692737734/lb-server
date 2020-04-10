echo "start install mysql in docker alone （开始在docker容器中安装单机版本的musql）"
echo "printf all step (下面将打印每个步骤)"

# shellcheck disable=SC2116
# shellcheck disable=SC2006
## 先判断是否已经安装了docker
# 执行命令，查询是否已经安装了docker，如果安装了继续执行，否则中断执行
DOCKER_VERSION=`docker --version`;
if [ "$DOCKER_VERSION" = "" ];then
  echo "当前还未安装docker，请安装后继续执行！！！！！"
  exit
else
  echo "当前的docker版本为：$DOCKER_VERSION"
fi

## 默认的mysql版本是5.7,根据实际需求可以变更，但是不建议变更，会造成不可预期的变化
## 后续整理支持的版本（就是说可以变更到的版本）
MYSQL_VERSION="5.7"
echo "The default installation version is $MYSQL_VERSION （默认安装版本为$MYSQL_VERSION）"
echo "Whether to change the version （Y/N） （是否需要变更版本）"

# shellcheck disable=SC2162
## 是否需要变更mysql版本
read  IF_CHANGE_VERSION

if [ "$IF_CHANGE_VERSION" = "Y" ] || [ "$IF_CHANGE_VERSION" = "y" ];then
  echo "请输入mysql版本"
  # shellcheck disable=SC2162
  read IN_MYSQL_VERSION
  # shellcheck disable=SC1068
  #修改设置的mysql版本
  MYSQL_VERSION=$IN_MYSQL_VERSION;
  echo "mysql版本已被修改为了：$MYSQL_VERSION"
elif [ "$IF_CHANGE_VERSION" = "N" ] || [ "$IF_CHANGE_VERSION" = "n" ];then
  echo "你选择了默认的版本，mysql的版本为5.7"
else
  echo "错误输入，安装结束"
  exit
fi

## 开始拉取
echo "开始拉取 mysql $MYSQL_VERSION"

# shellcheck disable=SC2006
PULL_MYSQL_RESULT=`docker pull mysql:"$MYSQL_VERSION"`










