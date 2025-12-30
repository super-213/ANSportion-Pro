#!/bin/bash

# ANSportion Mac 安装脚本
# 用于在 macOS 上安装和配置 ANSportion

echo "========================================"
echo "  ANSportion Mac 安装脚本"
echo "========================================"
echo ""

# 检查是否安装了 Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误：未找到 Python 3"
    echo "请先安装 Python 3.11 或更高版本："
    echo "  brew install python@3.11"
    exit 1
fi

# 显示 Python 版本
echo "✅ Python 版本："
python3 --version
echo ""

# 检查 pip3
if ! command -v pip3 &> /dev/null; then
    echo "❌ 错误：未找到 pip3"
    exit 1
fi

echo "📦 开始安装依赖库..."
echo "-----------------------------------"

# 检查是否需要创建虚拟环境
if [ ! -d "venv" ]; then
    echo "创建虚拟环境..."
    python3 -m venv venv
    if [ $? -eq 0 ]; then
        echo "  ✅ 虚拟环境创建成功"
    else
        echo "  ❌ 虚拟环境创建失败"
        exit 1
    fi
fi

# 激活虚拟环境并安装依赖
echo "激活虚拟环境并安装依赖..."
source venv/bin/activate

# 核心依赖库列表（排除 Windows 专用库）
PACKAGES=(
    "requests"
    "validators"
    "urllib3"
    "tqdm"
    "psutil"
    "ipaddress"
    "colorama"
    "cryptography"
    "Pillow"
    "pyfiglet"
)

# 安装每个包
for package in "${PACKAGES[@]}"; do
    echo "正在安装 $package..."
    pip install "$package" --quiet
    if [ $? -eq 0 ]; then
        echo "  ✅ $package 安装成功"
    else
        echo "  ⚠️  $package 安装失败"
    fi
done

echo ""
echo "-----------------------------------"
echo "📝 可选依赖："
echo ""

# pywifi（Mac 上功能受限）
read -p "是否安装 pywifi？(Mac 上功能受限) [y/N]: " install_pywifi
if [[ $install_pywifi =~ ^[Yy]$ ]]; then
    echo "正在安装 pywifi..."
    pip3 install pywifi
    if [ $? -eq 0 ]; then
        echo "  ✅ pywifi 安装成功"
    else
        echo "  ⚠️  pywifi 安装失败（这在 Mac 上是正常的）"
    fi
fi

echo ""
echo "========================================"
echo "  ✅ 安装完成！"
echo "========================================"
echo ""
echo "📖 使用方法："
echo "  1. 激活虚拟环境："
echo "     source venv/bin/activate"
echo ""
echo "  2. 运行程序："
echo "     普通模式：python3 ANSportion.py"
echo "     管理员模式：sudo venv/bin/python3 ANSportion.py"
echo ""
echo "⚠️  注意事项："
echo "  1. 每次使用前需要激活虚拟环境"
echo "  2. WiFi 相关功能需要管理员权限"
echo "  3. 某些攻击功能需要使用 sudo 运行"
echo "  4. 请确保防火墙允许 Python 的网络访问"
echo ""
echo "📚 查看完整文档：cat MAC_COMPATIBILITY_GUIDE.md"
echo ""
