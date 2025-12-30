# 🚀 ANSportion Mac 快速开始（3步）

## ✅ 已修复的问题
- ✅ 修复了依赖安装问题（使用虚拟环境）
- ✅ 修复了语法警告（转义序列）
- ✅ 程序现在可以完美运行！

## 第一步：安装依赖

```bash
bash install_mac.sh
```

这会自动：
1. 创建 Python 虚拟环境
2. 安装所有必需的依赖库
3. 配置好运行环境

## 第二步：运行程序

### 方法 A：使用启动脚本（推荐）

```bash
# 普通模式
bash run_ansportion.sh

# 管理员模式（WiFi、DOS 攻击等功能需要）
bash run_ansportion.sh sudo
```

### 方法 B：手动激活虚拟环境

```bash
# 1. 激活虚拟环境
source venv/bin/activate

# 2. 运行程序
python3 ANSportion.py

# 3. 使用完毕后退出虚拟环境
deactivate
```

### 方法 C：直接使用虚拟环境的 Python

```bash
# 普通模式
venv/bin/python3 ANSportion.py

# 管理员模式
sudo venv/bin/python3 ANSportion.py
```

## 第三步：开始使用

启动后输入命令：

```
help      # 查看所有命令
check     # 检查 IP 地址
port      # 扫描端口
crawler   # 爬取网页
exit      # 退出程序
```

## 📝 常用命令

### 测试功能
```bash
# 启动程序
bash run_ansportion.sh

# 在程序中输入：
check     # 进入 check 模块
1         # 查看你的 IP 地址
```

### 需要管理员权限的功能
```bash
# 使用 sudo 启动
bash run_ansportion.sh sudo

# 在程序中输入：
wifi      # WiFi 功能
attack    # 某些攻击功能
```

## ⚠️ 重要提示

1. **虚拟环境**：依赖已安装在 `venv/` 目录中
2. **每次使用**：使用 `run_ansportion.sh` 脚本或手动激活虚拟环境
3. **管理员权限**：WiFi 和某些攻击功能需要 sudo
4. **法律警告**：仅用于授权测试

## 🎯 功能测试清单

- [ ] 运行 `bash run_ansportion.sh`
- [ ] 输入 `help` 查看帮助
- [ ] 输入 `check` → `1` 查看 IP
- [ ] 输入 `port` → `2` 测试端口
- [ ] 输入 `crawler` → `2` 测试爬虫

## 🆘 遇到问题？

### 问题：提示找不到模块
**解决**：确保使用虚拟环境运行
```bash
bash run_ansportion.sh
```

### 问题：权限不足
**解决**：使用 sudo 运行
```bash
bash run_ansportion.sh sudo
```

### 问题：虚拟环境损坏
**解决**：删除并重新创建
```bash
rm -rf venv
bash install_mac.sh
```

## 📚 更多帮助

- **完整指南**：`开始使用_Mac.md`
- **技术文档**：`MAC_COMPATIBILITY_GUIDE.md`
- **问题报告**：QQ 群 991478664

---

**现在就开始吧！**

```bash
bash run_ansportion.sh
```

🎉 祝你使用愉快！
