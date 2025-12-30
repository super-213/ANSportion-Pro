# ⚡ 新 Mac 快速启动指南

## 🎯 你已经有项目文件，想在新 Mac 上运行

### 📦 第一步：传输项目

**在当前 Mac 上打包（不带虚拟环境）：**
```bash
cd /Volumes/HIKSEMI/tool/
tar --exclude='venv' -czf ANSportion-Pro.tar.gz ANSportion-Pro/
```

**传输方式：**
- AirDrop（最快）
- U盘/移动硬盘
- iCloud Drive

---

### 🚀 第二步：在新 Mac 上设置

```bash
# 1. 解压项目
tar -xzf ANSportion-Pro.tar.gz
cd ANSportion-Pro

# 2. 安装依赖（自动创建虚拟环境）
bash install_mac.sh

# 3. 运行程序
bash run_ansportion.sh
```

**就这么简单！** 🎉

---

## 📋 详细步骤

### 在新 Mac 上的操作：

#### 1️⃣ 解压项目
```bash
# 假设文件在下载文件夹
cd ~/Downloads
tar -xzf ANSportion-Pro.tar.gz
cd ANSportion-Pro
```

#### 2️⃣ 检查 Python（可选）
```bash
python3 --version
# 应该显示 Python 3.8 或更高版本
```

如果没有 Python：
```bash
# 安装 Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Python
brew install python@3.11
```

#### 3️⃣ 安装依赖
```bash
bash install_mac.sh
```

等待 1-2 分钟，看到这个就成功了：
```
✅ 安装完成！
```

#### 4️⃣ 运行程序
```bash
# 普通模式
bash run_ansportion.sh

# 管理员模式（WiFi、DOS 攻击等功能需要）
bash run_ansportion.sh sudo
```

---

## 🎮 使用方法

### 启动程序
```bash
bash run_ansportion.sh
```

### 在程序中
```
help      # 查看所有命令
check     # 检查 IP
port      # 扫描端口
exit      # 退出
```

### 需要管理员权限
```bash
bash run_ansportion.sh sudo
```

---

## 🔍 如果遇到问题

### 问题 1：找不到 Python
```bash
brew install python@3.11
```

### 问题 2：安装失败
```bash
# 删除虚拟环境重试
rm -rf venv
bash install_mac.sh
```

### 问题 3：运行出错
```bash
# 确保使用启动脚本
bash run_ansportion.sh
```

---

## 📁 项目结构

解压后应该看到：
```
ANSportion-Pro/
├── ANSportion.py           # 主程序
├── install_mac.sh          # 安装脚本
├── run_ansportion.sh       # 启动脚本
├── Code/                   # 功能模块
├── 各种 .md 文档           # 使用指南
└── venv/                   # 虚拟环境（安装后出现）
```

---

## ✅ 验证成功

运行后应该看到：
```
ANSportion-PRO $ 
```

输入 `help` 应该显示帮助信息。

---

## 🎯 完整命令流程

```bash
# === 在当前 Mac 上 ===
cd /Volumes/HIKSEMI/tool/
tar --exclude='venv' -czf ANSportion-Pro.tar.gz ANSportion-Pro/
# 传输文件到新 Mac

# === 在新 Mac 上 ===
cd ~/Downloads  # 或文件所在位置
tar -xzf ANSportion-Pro.tar.gz
cd ANSportion-Pro
bash install_mac.sh
bash run_ansportion.sh
```

---

## 💡 小贴士

1. **不要带虚拟环境**：打包时排除 `venv/` 文件夹
2. **使用启动脚本**：`bash run_ansportion.sh` 最方便
3. **保留文档**：所有 `.md` 文件都是使用指南
4. **需要 sudo**：WiFi 和某些攻击功能需要管理员权限

---

## 📚 更多帮助

- **完整迁移指南**：`迁移到新Mac指南.md`
- **使用指南**：`开始使用_Mac.md`
- **快速开始**：`快速开始_Mac.md`
- **问题解决**：`问题已解决_Mac.md`

---

**就这么简单！5 分钟搞定！** 🚀
