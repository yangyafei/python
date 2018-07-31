#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os,sys

# os.access(path, mode) 检测是否有访问权限的路径
# mode: os.F_OK path是否存在
# mode: os.R_OK path是否可读
# mode: os.W_OK path是否可写
# mode: os.X_OK path是否可执行
print('access mode:F_OK path是否存在', os.access('ttt.txt', os.F_OK))
print('access mode:F_OK path是否可读', os.access('ttt.txt', os.R_OK))
print('access mode:F_OK path是否可写', os.access('ttt.txt', os.W_OK))
print('access mode:F_OK path是否可执行', os.access('ttt.txt', os.X_OK))

# os.chdir 改变当前工作目录到指定的路径
path = 'D:\python_space'
retval = os.getcwd()
print("当前工作目录为: ", retval)
os.chdir(path)
retval = os.getcwd()
print("目录修改为: ", retval)

# chflags(path, flags) 设置路径的标记为数字标记，多个标记可以用OR来组合起来
# 只有UNIX下可以使用
# flags值：
# stat.UF_NODUMP: 非转储文件
# stat.UF_IMMUTABLE: 文件是只读的
# stat.UF_APPEND: 文件只能追加内容
# stat.UF_NOUNLINK: 文件不可删除
# stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
# stat.SF_ARCHIVED: 可存档文件(超级用户可设)
# stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
# stat.SF_APPEND: 文件只能追加内容(超级用户可设)
# stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
# stat.SF_SNAPSHOT: 快照文件(超级用户可设)
import os,stat
path = 'D:\python_space\demo\ttt.txt'
# retval = os.chflags(path, flags)
# print("chflags文件标记修改", retval)

# os.chmod(path,mode) 修改权限 UNIX才能使用 木有返回值
# mode:可以用以下选项按位或操作生成，目录的读权限表示可以获取目录里文件名列表
# 执行权限表示可以把工作目录切换到此目录，删除添加目录里的文化必须同时具有写和执行的权限
# 文件权限以用户id-组id-其他顺序检验，最先匹配的允许或者禁止权限被应用
# stat.S_IXOTH: 其他用户有执行权0o001
# stat.S_IWOTH: 其他用户有写权限0o002
# stat.S_IROTH: 其他用户有读权限0o004
# stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
# stat.S_IXGRP: 组用户有执行权限0o010
# stat.S_IWGRP: 组用户有写权限0o020
# stat.S_IRGRP: 组用户有读权限0o040
# stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
# stat.S_IXUSR: 拥有者具有执行权限0o100
# stat.S_IWUSR: 拥有者具有写权限0o200
# stat.S_IRUSR: 拥有者具有读权限0o400
# stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
# stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
# stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
# stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
# stat.S_IREAD: windows下设为只读
# stat.S_IWRITE: windows下取消只读
import os,stat,sys
# os.chmod('/tmp/foo.txt', stat.S_IXGRP)
# os.chmod('/tmp/foo.txt', stat.S_IWOTH)
print("chmod 权限修改")

# chown(path,uid,gid) 更改文件所有者 若不修改设置为-1, 只支持UNIX
# os.chown('/tmp/foo.txt',100,-1)
print("chown 所有者修改")

# os.chroot(path) 更改当前进程的跟目录为指定的目录 UNIX下root权限
# os.chroot('/tmp')
print("chroot 更改当前进程的根目录")

# os.close 关闭文件的描述符
# os.close(f)
print("close 关闭文件的描述符")

# os.closerange(fd_low, fd_high) 关闭所有文件描述符
# fd_low包含 fd_high不包含
# os.closerange(f,f)
print("chosechange 关闭文件描述符")

# os.dup(fd) 复制文件描述符
# fd2 = os.dup(fd)
print("os.dup 复制文件描述符")

# os.dup2(fd, fd2) 将文件描述符fd复制到fd2 unix,window都可以使用
# os.dup2(fd, fd2)
print('os.dup2 文件描述符从fd复制到fd2')

# os.fchdir通过文件描述符改变当前工作目录 unix,window
# os.fchdir(fd)
print("fchdir 通过文件描述符改变当前工作目录")

# os.fchmod(fd, mode) 改变文件的访问权限
# os.fchmod(fd, stat.S_IWOTH)
print("fchmod 更改文件的访问权限")

# os.fchown(fd, uid, gid)改为文件所有者 unix
# os.fchown(fd, 100, -1)
print("fchown 改变文件所有者")

# os.fdatasync(fd) 强制将文件写入磁盘 但不更新文件的状态信息
# 如果需要刷新缓存区可以使用该方法 unix
# os.fdatasync(fd)
print("fdatasync 强势将文件写入磁盘 刷新缓存区")

print("其他OS操作见文档吧~")